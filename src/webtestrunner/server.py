from webtestrunner.test_loader import list_tests
from webtestrunner.runner import TestRunner
from flask import *
import webbrowser

app = Flask(__name__)

@app.route("/tests/<path:module_path>")
def list_tests_from_module_path(module_path):
    if not os.path.exists(module_path):
        abort(501)

    tests = list_tests(module_path)
    return jsonify(tests)

@app.route("/tests/<string:module_name>")
def list_tests_from_module_name(module_name):
    tests = list_tests(module_name)
    return jsonify(tests)

@app.route("/test/name/<test_name>/module/<test_module>")
def test(test_name, test_module):
    # nosetests --with-id test_id
    results = TestRunner.run(test_name, test_module)



if __name__ == '__main__':
    webbrowser.open("http://localhost:4050")

    # debug
    app.run(host='0.0.0.0', port=4050, debug=True)

    # release
    # app.run(host='0.0.0.0', port=4050)




