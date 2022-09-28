#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa
    Script should take 3 arguments:
    mysql username: arg[1]
    mysql password: arg[2]
    databasename: arg[3]
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(passwd=sys.argv[2], host="localhost", db=sys.argv[3], user=sys.argv[1])
    c = db.cursor()
    c.execute("SELECT id, name FROM states ORDER by id ASC")
    holder = c.fetchall()
    for x in holder:
        print(x)
    db.close
    c.close
