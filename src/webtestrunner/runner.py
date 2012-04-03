from nose.core import TextTestRunner
from nose.loader import TestLoader


class TestRunner(object):

    def __init__(self, *args, **kwargs):
        super(TestRunner, self).__init__(*args, **kwargs)

    @classmethod
    def run(test_name, test_module):
        test_runner = TestRunner()
        (result, err) = test_runner.load_module(test_module)
        if not result:
            return (result, err)

        (result, err) = test_runner.load_test(test_name)
        if not result:
            return (result, err)

        results = test_runner.run_test()
        return results

    def load_module(self, test_module):
        if "module" not in self:
            try:
                self.module = __import__(test_module)
            except:
                return (False, "Failed to import test module %s" % test_module)

        return (True)

    def load_test(self, test_name):
        if "loader" not in self:
            self.loader = TestLoader()

        try:
            self.suite = self.loader.loadTestsFromName(test_name, module=self.module)
        except:
            return (False, "Failed to load test %s" % test_name)

        return (True)

    def run_test(self):
        if "runner" not in self:
            self.runner = TextTestRunner()

        results = self.runner.run(self.suite)
        return results


