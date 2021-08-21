#!/usr/bin/python3
"""Uses the GitHub API to display user id.

Takes GitHub credentials (username and password (token))

Args:
    username: github user
    password: github password (token)
Example:
    ./10-my_github.py ezedksl ghp_CdLQXOM1j94BfG3l4S5hsvBZfECGGc0IHuV2
"""


import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(r.json().get("id"))
