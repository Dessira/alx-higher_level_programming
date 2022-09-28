#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa
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
    c.execute("SELECT cities.id, cities.name, states.name FROM states INNER JOIN cities ON states.id = cities.state_id ORDER BY cities.id ASC")
    holder = c.fetchall()
    for x in holder:
        print(x)
    c.close()
    db.close()
