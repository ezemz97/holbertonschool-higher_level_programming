#!/usr/bin/python3
"""Retrieves the "X-Request-Id" header's value from specified URL.

Args:
    url: Destination URL
"""


import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1]).headers
    print(response.get("X-Request-Id"))
