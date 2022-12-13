#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa
    Script should take 3 arguments:
    mysql username: arg[1]
    mysql password: arg[2]
    databasename: arg[3]
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

    cur.execute("SELECT * FROM states ORDER BY id")
    states = cur.fetchall()

    for state in states:
        print(state)
