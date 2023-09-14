#!/usr/bin/python3

"""
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
    db.close()
