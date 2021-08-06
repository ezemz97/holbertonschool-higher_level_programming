#!/usr/bin/python3
"""Lists states starting with 'N' from the database.

Retrieves the states starting with 'N' from the database,
the resuls are displayed in ascending order by states.id.
Takes three arguments.

NOT SAFE FROM SQL INJECTIONS

Example:
    $ ./1-filter_states.py root root hbtn_0e_0_usa

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
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
