from flask import Flask, request, url_for
import subprocess
import re

app = Flask(__name__)


@app.route('/')
def home():
    return "Welocme to The homepage!</h1>"


@app.route('/helloworld')
def hello_world():
    if 'name' in request.args:
        user_name = request.args.get('name')
        greetings = re.sub(r'((?<=[a-z])[A-Z]|[A-Z](?=[a-z]))', r' \1', user_name).strip()
        return 'Hello' + ' ' + greetings
    else:
        return "Hello Stranger"


@app.route("/versionz")
def versionz():
    label = subprocess.check_output(["git", "rev-parse", "--show-toplevel", "HEAD"]).strip()
    return label


with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('versionz'))


if __name__ == '__main__':
    app.run(debug=True)
