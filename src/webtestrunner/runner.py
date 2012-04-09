from nose.core import TextTestRunner
from nose.loader import TestLoader
from StringIO import StringIO


class TestRunner(object):

    def __init__(self, *args, **kwargs):
        super(TestRunner, self).__init__(*args, **kwargs)

    def run(self, test_name, test_module):
        target = "%s:%s" % (test_module, test_name)
        test_suite = TestLoader().loadTestsFromName(target)
        report = StringIO()
        runner = TextTestRunner(report)
        result = runner.run(test_suite)

        ret = {
            "pass": result.wasSuccessful()
        }

        for failure in result.failures:
            ret.update({"stack": failure[1]})
            ret.update({"log": report.getvalue()})

        for error in result.errors:
            ret.update({"error": error[1]})

        return ret


if __name__ == "__main__":
    result = TestRunner().run("TestToolsTestCase.test_environ_defaults", "flask.testsuite.testing")
    # result = TestRunner().run("MockTests.test_fail", "webtestrunner.tests.tests")
    # result = TestRunner().run("MockTests.test_ensure_running", "webtestrunner.tests.tests")
    print result



