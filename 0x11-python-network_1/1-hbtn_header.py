#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status

Prints the "X-Request-Id" header's value from URL

Args:
    url (str): Destination URL
"""


import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.getheader("X-Request-Id")
        print(header)
