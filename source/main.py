from flask import Flask, request
from greeting_service import GreetingService
from version_service import VersionService
import logging


logging.basicConfig(
    filename='service.log',
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
)
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to The homepage!</h1>"


@app.route('/helloworld')
def hello_world():
    user_name = request.args.get('name')
    return GreetingService().say_hello(user_name)


@app.route('/versionz')
def versionz():
    return VersionService().versionz()


if __name__ == '__main__':
    app.run(debug=True)
