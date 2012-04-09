from subprocess import Popen, PIPE
from nose.loader import TestLoader
import os
import logging
import pickle


class WTRLoader(object):

    def __init__(self, *args, **kwargs):
        super(WTRLoader, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger(__file__)
        self.test_loader = TestLoader()

    @classmethod
    def load(name_or_path):
        loader = WTRLoader()
        tests = None

        if os.sep in name_or_path:
            # smells like a path, verify
            if os.path.exists(name_or_path):
                # yep, it's a path
                loader.logger.debug("Name specified is a path")
                if os.path.isfile(name_or_path):
                    tests = loader.test_loader.loadTestsFromFile(name_or_path)
                else:
                    tests = loader.test_loader.loadTestsFromDir(name_or_path)
        else:
            # might be a module name
            try:
                tests = loader.test_loader.loadTestsFromName(name_or_path)
                # yep, it's a module
            except:
                loader.logger.error("Specified module name cannot be found on Python's path. You have two options:\n1. Instead of supplying a module-name, you can supply a file or directory path\n2. Install the module you're interested in test, and then try to load tests via the module name again. > python setup.py develop")
                return False

        if not tests:
            # not sure how this is possible, but we cannot continue, bail out
            loader.logger.error("Failed to find any tests, bailing out early...")
            return False


def list_tests(name):
    # name = module or file or directory
    id_file = os.path.abspath(os.path.join(os.path.expanduser("~"), "test-file-ids"))
    if os.path.exists(id_file):
        os.remove(id_file)

    # this is executing tests, not sure why, just going to usurp the problem for now
    # nose.run(argv=["--collect-only", "--with-id", "--id-file=%s" % id_file, name])
    Popen(["nosetests", "--collect-only", "--with-id", "--id-file=%s" % id_file, name], stdout=PIPE, stderr=PIPE).communicate()
    fh = open(id_file, "rb")
    data = pickle.load(fh)
    fh.close()

    os.remove(id_file)

    tests = []
    ids = data["ids"]
    for id in ids.keys():
        if len(ids[id]) == 3:
            if ids[id][2]:
                test = {
                    "id": id,
                    "name": ids[id][2],
                    "module": ids[id][1]
                }
                tests.append(test)
            else:
                # ToDo
                # Why are some tests like this?
                pass

    return tests


if __name__ == "__main__":
    tests = list_tests("flask")
    print tests

