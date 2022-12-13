#!/usr/bin/python3
"""Script that lists all states with a name starting with N
    Script should take 3 arguments: 
    mysql username: arg[1]
    mysql password: arg[2]
    database name: arg[3]
"""
import MySQLdb
import sys

if __name__ == '__main__':
    import sys
    import MySQLdb

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         user=user,
                         passwd=password,
                         db=db_name)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    states = cur.fetchall()

    for state in states:
        print(state)
