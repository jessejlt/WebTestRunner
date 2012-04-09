from webtestrunner.test_loader import list_tests
from webtestrunner.runner import TestRunner
from webtestrunner import out
from flask import Flask, session, jsonify, abort, render_template
import webbrowser
import os
import sys

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
    results = TestRunner().run(test_name, test_module)
    return jsonify(results)


@app.route("/status")
def status():
    # Add any hooks necessary to determine if the test environment is ready
    # for testing
    return jsonify({"status": True, "errorMessage": None})


@app.route("/log")
def log():
    return jsonify({"log": out.getvalue()})


@app.route("/exit")
def exit():
    # TODO this is being captured by flask, need a cross-platform way to kill the server
    sys.exit(-1)


@app.route("/")
def index():
    return render_template("index.html")


def main():
    app.secret_key = """,kegk8rNQWz9)T}fvy*",*Et>:_W~\m4KxDjva%5&8LSI'WaM~RNe\.iJ6*r2J5"""
    webbrowser.open("http://localhost:4050")

    print "http://localhost:4050"

    # debug
    # app.run(host='0.0.0.0', port=4050, debug=True)

    # release
    app.run(host='0.0.0.0', port=4050)

    """
    TODO
    1. Cookie to store last used library, load on startup
    2. Dual-views for library.js, one for existing interface, another for
        modal-dialog.
    3. Switch console-log-view from modal to alert, display above table on-click
    4. Remove the library specifier on top of page, replace with
        a config-button that launches the library modal-dialog
    5. Closing browser should kill the backend server: sys.exit(1)
    6. Write tests http://flask.pocoo.org/docs/api/?highlight=flask#flask.Flask.test_client
    7. Log capture should be on by default by virtue of nose, test this theory by
        writing a failing unittest that writes stuff to the log, and verify that
        the log is made part of the failure message -- if the failure message is there,
        remove the log capture in __init__
    """


if __name__ == '__main__':
    main()
