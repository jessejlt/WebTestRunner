from nose.core import TextTestRunner
from nose.loader import TestLoader
from StringIO import StringIO
import nose


class TestRunner(object):

    def __init__(self, *args, **kwargs):
        super(TestRunner, self).__init__(*args, **kwargs)

    def run(self, test_name, test_module):
        test_suite = TestLoader().loadTestsFromName(test_module + ":" + test_name)
        report = StringIO()
        runner = TextTestRunner(report)
        results = nose.run(suite=test_suite, testRunner=runner)

        result = {
            "pass": results,
            "error": report.getvalue()
        }

        return result


if __name__ == "__main__":
    # result = TestRunner().run("test.FlaskTests.test_add_bug", "pixelverifyserver.test")
    # result = TestRunner().run("testsuite.find_all_tests", "flask.testsuite")
    result = TestRunner().run("TestToolsTestCase.test_environ_defaults", "flask.testsuite.testing")
    print result


