#!/usr/bin/python3
"""Lists states from the database.

Retrieves the matching states by user input from the database,
the resuls are displayed in ascending order by states.id.
Takes four arguments.

Example:
    $ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa

Args:
    user (str): mysql username
    pass (str): mysql password
    database (str): mysql database name
    statename (str): state name to search
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    statename = argv[4]
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name\
                LIKE %s ORDER BY id ASC", (statename,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
