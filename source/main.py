from flask import Flask, request
import logging
import requests
import re

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
    api_url = "https://api.github.com/repos"
    owner = "Mudassir86"
    repo = "HttpServiceApp"
    base_url = api_url + "/" + owner + "/" + repo

    response_api = requests.get(base_url)
    response_api_json = response_api.json()

    branch = 'master'
    commit_api_url = base_url + '/commits' + '/' + branch
    response_commit = requests.get(commit_api_url)
    response_commit_json = response_commit.json()

    return {'name': response_api_json['name'], 'last_commit_hash': response_commit_json['sha']}


if __name__ == '__main__':
    app.run(debug=True)
