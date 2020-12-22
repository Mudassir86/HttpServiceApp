from flask import Flask

app = Flask(__name__)


@app.route("/helloworld")
def hello_world():
    return "Hello Stranger 123"


if __name__ == '__main__':
    app.run(debug=True)
