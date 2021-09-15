#!/usr/bin/python3
"""Sends a POST request with an email as data and retrieves the response.

Args:
    (1) url: Destination url
    (2) email: email value
"""


from urllib import request, parse
import sys

if __name__ == "__main__":
    email = parse.urlencode({"email": sys.argv[2]}).encode('utf-8')
    with request.urlopen(sys.argv[1], email) as response:
        print(response.read().decode('utf-8'))
