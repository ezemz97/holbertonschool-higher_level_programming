#!/usr/bin/python3
"""List 10 commits (recent to oldest) of a repository.

Uses GitHub API

Args:
    repo: repository name - argv[1]
    owner: owner name - argv[2]

Example:
    ./100-github_commits.py rails rails
"""


import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get('https://api.github.com/repos/{}/{}/commits'.format(
                     argv[2], argv[1]))

    for commit in r.json()[:10]:
        print("{}: {}".format(
              commit.get('sha'),
              commit.get('commit').get('author').get('name')))
    # Pretty print
    # for key, value in r.json().items():
    #   print("{} ({})".format(key, value)) """
