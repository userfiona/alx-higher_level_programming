#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Establish a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    
    # Create a cursor for database operations
    cur = db.cursor()
    
    # Execute a SQL query to select all rows from the "states" table where the name matches the argument
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC", (argv[4],))
    
    # Fetch all rows that match the query
    rows = cur.fetchall()
    
    # Iterate through the results and print them
    for row in rows:
        print(row)
    
    # Close cursor and database connection
    cur.close()
    db.close()
