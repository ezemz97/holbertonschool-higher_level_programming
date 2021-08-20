#!/bin/bash
# Write out response code

curl -s -I -w '%{response_code}' '$1' -o /dev/null
