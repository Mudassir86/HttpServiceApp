from flask import Flask, request
import re

app = Flask(__name__)


@app.route('/helloworld')
def hello_world():
    if 'name' in request.args:
        user_name = request.args.get('name')
        greetings = re.sub(r'((?<=[a-z])[A-Z]|[A-Z](?=[a-z]))', r' \1', user_name).strip()
        return 'Hello' + ' ' + greetings
    else:
        return "Hello Stranger"


if __name__ == '__main__':
    app.run(debug=True)
