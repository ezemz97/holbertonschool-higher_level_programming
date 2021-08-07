#!/usr/bin/python3
"""Lists states from the database.

Retrieves the cities of the matching state from a database,
the resuls are displayed in ascending order by states.id.
Takes four arguments.

Example:
    $ ./5-filter_cities.py root root hbtn_0e_0_usa

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
    cur.execute("SELECT cities.name FROM cities JOIN states "
                "WHERE cities.state_id = states.id AND states.name = %s",
                (statename,))
    query_rows = cur.fetchall()
    cities = []
    for row in query_rows:
        cities.append(row[0])
    print(', '.join(cities))
    cur.close()
    conn.close()
