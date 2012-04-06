from nose.core import TextTestRunner
from nose.loader import TestLoader
from StringIO import StringIO


class TestRunner(object):

    def __init__(self, *args, **kwargs):
        super(TestRunner, self).__init__(*args, **kwargs)

    def run(self, test_name, test_module):
        (result, err) = self.load_module(test_module)
        if not result:
            return (result, err)

        (result, err) = self.load_test(test_name)
        if not result:
            return (result, err)

        results = self.run_test()
        return results

    def load_module(self, test_module):
        if not hasattr(self, "module"):
            try:
                self.module = __import__(test_module)
            except:
                return (False, "Failed to import test module %s" % test_module)

        return (True, None)

    def load_test(self, test_name):
        if not hasattr(self, "loader"):
            self.loader = TestLoader()

        try:
            self.suite = self.loader.loadTestsFromName(test_name, module=self.module)
        except:
            return (False, "Failed to load test %s" % test_name)

        return (True, None)

    def run_test(self):
        report = StringIO()
        runner = TextTestRunner(report)
        results = runner.run(self.suite)

        result = {
            "pass": results.wasSuccessful(),
            "error": report.getvalue()
        }

        return result


if __name__ == "__main__":
    # result = TestRunner().run("test.FlaskTests.test_add_bug", "pixelverifyserver.test")
    # result = TestRunner().run("testsuite.find_all_tests", "flask.testsuite")
    result = TestRunner().run("testsuite.testing.TestToolsTestCase.test_environ_defaults", "flask.testsuite.testing")

    print result


