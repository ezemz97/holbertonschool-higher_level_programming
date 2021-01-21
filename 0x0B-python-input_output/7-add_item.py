#!/usr/bin/python3
"""Comment"""
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


try:
    jsonfile = load_from_json_file('add_item.json')
except:
    jsonfile = []

for i in range(1, len(argv)):
    jsonfile.append(argv[i])

save_to_json_file(jsonfile, 'add_item.json')
