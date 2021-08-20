#!/bin/bash
# Write out response code
# https://everything.curl.dev/usingcurl/verbose/writeout
curl -s -w '%{http_code}' $1 -o /dev/null
