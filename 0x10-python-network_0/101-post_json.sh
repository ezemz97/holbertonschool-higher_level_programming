#!/bin/bash
# Sends a post request from a json file
curl -s -H 'Content-Type: application/json' -X POST "$1" -d @"$2"
