#!/usr/bin/python3
"""Sends a POST request to  with a letter as a parameter.

Displays the body of the response.

Args:
    q: letter value
"""


import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        value = ""
    else:
        value = argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': value})
    try:
        json = r.json()
        if not json:
            print("No result")
        else:
            print("[{}] {}".format(json.get("id"), json.get("name")))
    except ValueError:
        print("Not a valid JSON")
