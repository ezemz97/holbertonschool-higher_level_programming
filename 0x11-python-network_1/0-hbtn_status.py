#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status

Prints the type of the response,
the content, and the utf-8 decoded content.
"""


import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        decode = html.decode('utf-8')
        print("Body response:\n"
            "\t- type: {}\n"
            "\t- content: {}\n"
            "\t- utf8 content: {}"
            .format(type(html), html, decode))
