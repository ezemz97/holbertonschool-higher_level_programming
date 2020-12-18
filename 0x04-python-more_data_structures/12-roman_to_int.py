#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    romans = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    new = []
    total = 0
    for w in roman_string:
        new.append(romans[w])
    y = 0
    lenmenosuno = len(new) - 1
    for x in range(len(new)):
        if (y < lenmenosuno):
            y = x + 1
            if new[x] >= new[y]:
                total += new[x]
            else:
                total -= new[x]
    total += new[lenmenosuno]
    return total
