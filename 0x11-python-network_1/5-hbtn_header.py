#!/usr/bin/python3
"""Sends get request (headers) to URL (argv)

Print the "X-Request-Id" header's value.

Args:
    url: Destination URL
"""


import requests

if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status').headers
    print(response.get("X-Request-Id"))
