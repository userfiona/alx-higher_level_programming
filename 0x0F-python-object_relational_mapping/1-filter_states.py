#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Make a connection to the database
    with MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    ) as db:
        # Create a cursor for database operations
        cur = db.cursor()

        # Execute a SQL query to select states with names starting with 'N'
        query = """
            SELECT *
            FROM states
            WHERE name LIKE BINARY 'N%'
            ORDER BY id ASC
        """
        cur.execute(query)

        # Fetch all rows that match the query
        rows = cur.fetchall()

        # Iterate through the results and print them
        for row in rows:
            print(row)
