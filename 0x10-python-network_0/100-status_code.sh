#!/bin/bash
# Write out response code

curl -s -w '%{http_code}' $1 -o /dev/null
