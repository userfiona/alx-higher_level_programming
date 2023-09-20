#!/usr/bin/python3

"""
<<<<<<< HEAD
    A script that lists all cities from the database hbtn_0e_0_usa
    Username, password and database names are given as user args
"""


import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cursor = db.cursor()

    sql = """SELECT c.id, c.name, s.name
          FROM states s, cities c
          WHERE c.state_id = s.id
          ORDER BY c.id ASC"""

    cursor.execute(sql)

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
=======
List all cities from a database
"""

import sys
import MySQLdb

if __name__ == '__main__':
    # Check if all three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Establish a connection to the database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    # Create a cursor
    cur = db.cursor()

    # Execute the query to select cities and their corresponding state names
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id ASC")

    # Fetch all rows and print them
    cities = cur.fetchall()

    for city in cities:
        print(city)

    # Close the cursor and the database connection
    cur.close()
>>>>>>> 4af1a2f9cddcdbd0e8ccc7cb2f6b9ac828f01653
    db.close()
