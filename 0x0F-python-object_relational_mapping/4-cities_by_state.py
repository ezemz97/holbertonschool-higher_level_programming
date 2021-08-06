#!/usr/bin/python3
"""Lists cities from the database.

Retrieves all the cities from the database with their state,
the resuls are displayed in ascending order by cities.id.
Takes three arguments.

Example:
    $ ./4-cities_by_state.py root root hbtn_0e_4_usa
    ('cities.id', 'cities.name', 'states.name')

Args:
    user (str): mysql username
    pass (str): mysql password
    database (str): mysql database name
    cityname (str): state name to search
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
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities LEFT JOIN states ON cities.state_id = states.id\
                ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
