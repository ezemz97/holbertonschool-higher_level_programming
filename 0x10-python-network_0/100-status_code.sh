#!/bin/bash
# https://everything.curl.dev/usingcurl/verbose/writeout
# Write out response code

curl -s -w '%{http_code}' $1 -o /dev/null
