#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if (my_list):
        newlist = my_list.copy()
        newlist = [replace if value == search else value for value in newlist]
        return newlist
    return None
