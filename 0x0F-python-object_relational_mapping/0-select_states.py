#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa.

Takes three arguments and retrieves all states from the database.
Resuls are displayed in ascending order by states.id.

Example:
    $ ./0-select_states.py root root hbtn_0e_0_usa

Args:
    user (str): mysql username
    pass (str): mysql password
    database (str): mysql database name
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
