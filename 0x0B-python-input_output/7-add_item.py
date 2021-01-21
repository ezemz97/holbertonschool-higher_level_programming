#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""
import sys
import json


load_json = __import__('8-load_from_json_file').load_from_json_file
save_json = __import__('7-save_to_json_file').save_to_json_file


try:
    my_list = load_json("add_item.json")
except FileNotFoundError:
    my_list = []

for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])

save_json(my_list, filename)
