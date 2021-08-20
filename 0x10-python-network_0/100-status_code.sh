#!/bin/bash
# https://everything.curl.dev/usingcurl/verbose/writeout
# Write out response code

curl -sIw '%{response_code}' $1 -o /dev/null
