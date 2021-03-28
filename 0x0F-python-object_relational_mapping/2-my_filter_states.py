#!/usr/bin/python3
"""Fetch all states from database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    search = argv[4]

    db = MySQLdb.connect("localhost", username, password, db_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = '{}'".format(search))
    results = cursor.fetchall()
    for row in results:
        print(row)
    db.close()

