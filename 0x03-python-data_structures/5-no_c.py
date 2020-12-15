#!/usr/bin/env python3
def no_c(my_string):
    new_string = ""
    for x in my_string:
        if x is not "c" and x is not "C":
            new_string += x
    return new_string
