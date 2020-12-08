#!/usr/bin/python3
for symbol in range(97, 123):
    if symbol == 101 or symbol == 113:
        continue
    else:
        print("{}".format(chr(symbol)), end="")
