#!/usr/bin/python3
<<<<<<< HEAD
"""Lists states"""
=======

"""
Script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument, safe from MySQL
injections
"""
>>>>>>> 4af1a2f9cddcdbd0e8ccc7cb2f6b9ac828f01653

import MySQLdb
from sys import argv

if __name__ == "__main__":
<<<<<<< HEAD
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id ASC",
                (argv[4], ))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
=======
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
>>>>>>> 4af1a2f9cddcdbd0e8ccc7cb2f6b9ac828f01653
