#!/usr/bin/python3
"""Prints the "X-Request-Id" header's value from URL (argv[1]).

Args:
    url (str): Destination URL

Example:
    $ ./1-hbtn_header.py https://intranet.hbtn.io
    d623ce98-f11b-4357-865c-d2818cc4d1c5
    $
"""


import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.getheader("X-Request-Id")
        print(header)
