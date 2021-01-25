#!/usr/bin/python3
""" 18-main """
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file(list_rectangles_input)

    lyst = []
    lyst2 = []
    with open("Rectangle.json", "r") as file:
        lyst = Rectangle.from_json_string(file.read())
    for element in range(len(lyst)):
        lyst[element] = Rectangle.create(**lyst[element])
    for rect in lyst:
        print("[{}] {}".format(id(rect), rect))