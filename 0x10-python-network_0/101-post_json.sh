#!/bin/bash
# Sends a post request from a json file
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
