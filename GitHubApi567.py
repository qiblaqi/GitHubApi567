import requests
import json


def read_from_git_api(user_id):
    """
    this function get the github user_id and query all the user repo
    :param user_id: the user github id
    :return: [repo name]
    """
    ans = []
    r = requests.get(f'https://api.github.com/users/{user_id}/repos')
    if r.status_code!=200 and r.status_code!=403:
        raise Exception("invalid user id")   #raise ValueError if the user_id does not exsist
    if r.status_code == 403:
        raise Exception("too much request, please wait for a hour")
    response = json.loads(r.text)

    for repo in response:
        repo_name = repo["name"]
        r2 = requests.get(f'https://api.github.com/repos/{user_id}/{repo_name}/commits')
        response2 = json.loads(r2.text)
        ans.append(f'Repo: {repo["name"]} Number of commits: {len(response2)}')
    return ans