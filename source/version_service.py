import requests


class VersionSevice:
    def versionz(self):
        api_url = "https://api.github.com/repos"
        owner = "Mudassir86"
        repo = "HttpService"
        base_url = api_url + "/" + owner + "/" + repo

        response_api = requests.get(base_url)
        response_api_json = response_api.json()

        branch = 'master'
        commit_api_url = base_url + '/commits' + '/' + branch
        response_commit = requests.get(commit_api_url)
        response_commit_json = response_commit.json()

        return {'name': response_api_json['name'], 'last_commit_hash': response_commit_json['sha']}
