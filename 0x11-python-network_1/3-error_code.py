#!/usr/bin/python3
"""Sends a request and retrieves the status code.

Args:
    (1) url: Destination url
"""


from urllib import request, error
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
