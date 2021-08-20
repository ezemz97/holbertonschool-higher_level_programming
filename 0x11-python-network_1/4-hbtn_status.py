#!/usr/bin/python3
"""Sends get request to https://intranet.hbtn.io/status.

Prints the body response (text)
"""


import requests

if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status').text
    print("Body response:\n"
          "\t- type: {}\n"
          "\t- content: {}"
          .format(type(response), response))
