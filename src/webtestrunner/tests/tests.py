from webtestrunner.server import app
from unittest import TestCase, main
import logging
import os
import time
import json


class MockTests(TestCase):

    def setUp(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

    def test_fail(self):
        self.logger.error("About to fail")
        self.assertTrue(False, "Testing a failcase")

    def test_pass(self):
        self.logger.info("About to pass")
        self.assertTrue(True)

    def test_ensure_running(self):
        # Ensure we actually ran this test by writing a file to disk
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), "test_ensure_running.txt"))
        if os.path.exists(path):
            os.remove(path)

        self.logger.debug("Writing file to disk %s" % path)
        open(path, "w").write(time.asctime())
        self.assertTrue(os.path.exists(path))


class TestWebAPIs(TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_mock_fail(self):
        test_name = "MockTests.test_fail"
        test_module = "webtestrunner.tests.tests"
        url = "/test/name/%s/module/%s" % (test_name, test_module)
        response = self.app.get(url)
        data = json.loads(response.data)
        self.assertTrue(data["pass"] == False)

    def test_mock_pass(self):
        test_name = "MockTests.test_pass"
        test_module = "webtestrunner.tests.tests"
        url = "/test/name/%s/module/%s" % (test_name, test_module)
        response = self.app.get(url)
        data = json.loads(response.data)
        self.assertTrue(data["pass"] == True)


if __name__ == "__main__":
    main()
