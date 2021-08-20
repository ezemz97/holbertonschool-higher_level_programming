#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response.

Prints the error code (if)

Args:
    url: Destination URL
"""


import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Error code: {}".format(r.status_code))
    else:
        print("{}".format(r.text))
