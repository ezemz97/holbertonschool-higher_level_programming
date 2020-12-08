#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastdigit = number % 10
else:
    lastdigit = number % -10

if lastdigit > 5:
    text = "and is greater than 5"
elif lastdigit < 6 and lastdigit != 0:
    text = "and is less than 6 and not 0"
elif lastdigit == 0:
    text = "and is 0"

print("Last digit of {} is {} {}".format(number, lastdigit, text))
