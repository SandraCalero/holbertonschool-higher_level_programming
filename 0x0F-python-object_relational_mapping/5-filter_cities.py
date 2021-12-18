#!/usr/bin/python3
"""This script is takeing in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()

    cur.execute("SELECT cities.name FROM cities INNER JOIN states on\
        states.id = cities.state_id WHERE BINARY states.name = %s\
        ORDER BY cities.id", [argv[4]])
    query_rows = cur.fetchall()
    idx = 0
    for row in query_rows:
        if idx == 0:
            print(row[0], end='')
            idx += 1
        else:
            print(', {}'.format(row[0]), end='')
    print()
    cur.close()
    conn.close()
