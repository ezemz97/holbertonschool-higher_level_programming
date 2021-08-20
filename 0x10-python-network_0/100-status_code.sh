#!/bin/bash
# https://everything.curl.dev/usingcurl/verbose/writeout
# Write out response code

curl -sIw '%{response_code}' 0.0.0.0:5000 -o /dev/null
