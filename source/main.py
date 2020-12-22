from flask import Flask, request

app = Flask(__name__)


@app.route('/helloworld')
def hello_world():
    if 'name' in request.args:
        greetings = request.args.get('name')
        return "Hello" + " " + greetings
    else:
        return "Hello Stranger"


if __name__ == '__main__':
    app.run(debug=True)
