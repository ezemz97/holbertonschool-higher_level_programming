#!/usr/bin/python3
"""Test suite for the "Base" module

"""
import unittest
from models.base import Base


class TestBaseModule(unittest.TestCase):
    def test_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(42)
        self.assertEqual(b2.id, 42)
        b3 = Base(None)
        self.assertEqual(b3.id, 2)
        b3.id = b3.id + 4
        self.assertEqual(b3.id, 6)
        b3.id = None
        self.assertEqual(b3.id, None)
        b4 = Base("you can assume id is an integer and\
        you don’t need to test the type of it")
        self.assertTrue(type(b4.id) is str)
        self.assertIsInstance(b1, Base)
        self.assertIsInstance(b2, Base)
        self.assertIsInstance(b3, Base)
        self.assertIsInstance(b4, Base)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string(""), "[]")
        with self.assertRaises(TypeError):
            Base.to_json_string()
        dictionary = {"width": 1, "height": 1, "x": 1, "y": 1, "id": 1}
        jsonSTR = Base.to_json_string(dictionary)
        self.assertTrue(type(jsonSTR) is str)

    def test_from_json_string(self):
        """ test from_json_string method """
        self.assertEqual(Base.from_json_string([]), [])
        self.assertEqual(Base.from_json_string(None), [])

    def test_save_to_file(self):
        with self.assertRaises(TypeError):
            Base.save_to_file()
        with self.assertRaises(TypeError):
            Base.save_to_file([], 1)
        Base.save_to_file([])
        with open("Base.json", "r") as f:
            self.assertEqual("[]", f.read())
