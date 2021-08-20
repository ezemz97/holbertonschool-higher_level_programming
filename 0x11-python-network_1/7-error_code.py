#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter.

Displays the body of the response.

Args:
    url: Destination URL
    email: Email value
"""


import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    if r.raise_for_status():
        print("Error code: {}".format(r.status_code))
    else:
        print("{}".format(r.text))
