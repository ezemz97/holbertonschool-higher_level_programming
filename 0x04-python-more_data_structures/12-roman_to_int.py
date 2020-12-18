#!/usr/bin/python3

roman_string = "LXXXVII"
romans = {"M":1000, "D":500, "C":100, "L":50, "X": 10, "V":5, "I":1}
new = []
total = 0
for w in roman_string:
    new.append(romans[w])
print (new)
prev = 0
z = -1
for x in range(len(new)):
    if new[x] >= prev:
        total += prev
    else:
        total -= prev
    prev = new[z+1]
    

print (total)