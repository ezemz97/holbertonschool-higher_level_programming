#!/bin/bash
# Write out response code

curl -sIw '%{response_code}' $1 -o /dev/null
