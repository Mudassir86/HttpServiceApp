import requests


class VersionService:
    def versionz(self):
        api_url = "https://api.github.com/repos"
        owner = "Mudassir86"
        repo = "HttpService"
        base_url = api_url + "/" + owner + "/" + repo

        api_request = requests.get(base_url)
        api_request.raise_for_status
        response_api_json = api_request.json()

        branch = 'master'
        commit_api_url = base_url + '/commits' + '/' + branch
        commit_request = requests.get(commit_api_url)
        commit_request.raise_for_status
        response_commit_json = commit_request.json()

        return {'name': response_api_json['name'], 'last_commit_hash': response_commit_json['sha']}
