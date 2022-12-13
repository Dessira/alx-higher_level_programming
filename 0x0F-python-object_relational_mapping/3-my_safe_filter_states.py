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
    db_con = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3],
                             charset="utf8")
    curr = db_con.cursor()
    curr.execute("SELECT * FROM states WHERE name = %s;",
                 (sys.argv[4],))
    states = curr.fetchall()
    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
    curr.close()
    db_con.close()
