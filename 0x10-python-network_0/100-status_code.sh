#!/bin/bash
# Write out response code
curl -s -w '%{response_code}' "$1" -o /dev/null
