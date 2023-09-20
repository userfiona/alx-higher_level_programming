#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Create a cursor for database operations
    cur = db.cursor()

    # Execute a SQL query to select states with names starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    # Fetch all rows that match the query
    rows = cur.fetchall()

    # Iterate through the results and print them
    for row in rows:
        print(row)

    # Clean up process by closing cursor and database connection
    cur.close()
    db.close()
