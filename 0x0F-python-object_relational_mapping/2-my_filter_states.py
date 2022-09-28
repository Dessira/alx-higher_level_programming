#!/usr/bin/python3
"""Script that lists all states with a name starting with N
    Script should take 3 arguments: 
    mysql username: arg[1]
    mysql password: arg[2]
    database name: arg[3]
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(sys.argv[4]))
    holder = c.fetchall()
    for x in holder:
        print(x)
    c.close()
    db.close()
