from webtestrunner.loader import list_tests
from webtestrunner.runner import TestRunner
from flask import Flask, session, jsonify, abort, render_template
import webbrowser
import os
import signal

app = Flask(__name__)


@app.route("/tests/<path:module_path>")
def list_tests_from_module_path(module_path):
    if not os.path.exists(module_path):
        abort(501)

    tests = list_tests(module_path)
    session["tests"] = tests
    return jsonify({"tests": tests})


@app.route("/tests/<string:module_name>")
def list_tests_from_module_name(module_name):
    tests = list_tests(module_name)
    session["tests"] = tests
    return jsonify({"tests": tests})


@app.route("/tests/<string:module_name>/<int:id>")
def test_via_id(module_name, id):

    if "tests" not in session:
        abort(501)

    for sess in session["tests"]:
        if sess.get("id") == id:
            app.logger.debug("session %s, module %s" % (sess["name"], sess["module"]))
            results = TestRunner().run(sess["name"], sess["module"])
            break

    return jsonify(results)


@app.route("/test/name/<test_name>/module/<test_module>")
def test(test_name, test_module):
    # nosetests --with-id test_id
    app.logger.debug("TestRunner().run(\"%s\", \"%s\")" % (test_name, test_module))
    results = TestRunner().run(test_name, test_module)
    app.logger.debug(results)
    return jsonify(results)


@app.route("/status")
def status():
    # Add any hooks necessary to determine if the test environment is ready
    # for testing
    return jsonify({"status": True, "errorMessage": None})


@app.route("/exit")
def exit():
    if hasattr(os, "kill"):
        if hasattr(signal, "CTRL_C_EVENT"):
            os.kill(os.getpid(), signal.CTRL_C_EVENT)
        else:
            os.kill(os.getpid(), signal.SIGINT)


@app.route("/")
def index():
    return render_template("index.html")


def main():
    app.secret_key = """,kegk8rNQWz9)T}fvy*",*Et>:_W~\m4KxDjva%5&8LSI'WaM~RNe\.iJ6*r2J5"""
    webbrowser.open("http://localhost:4050")

    print "http://localhost:4050"

    # debug
    app.run(host='0.0.0.0', port=4050, debug=True)

    # release
    # app.run(host='0.0.0.0', port=4050)


if __name__ == '__main__':
    main()
