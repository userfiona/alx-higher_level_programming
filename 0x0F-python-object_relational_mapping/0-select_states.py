#!/usr/bin/python3
<<<<<<< HEAD
""" Script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':

    # make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # It gives us the ability to have multiple seperate working environments
    # through the same connection to the database.
    cur = db.cursor()
    cur.execute("SELECT * FROM states")

    rows = cur.fetchall()
    for i in rows:
        print(i)
    # Clean up process
    cur.close()
    db.close()
=======

"""
    A script that lists all states from the database hbtn_0e_0_usa
    Username, password, and database names are given as user args
"""

import sys
import MySQLdb

if __name__ == '__main__':
    # Check if all three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(user=username,
                             passwd=password,
                             db=database_name,
                             host='localhost',
                             port=3306)

        # Create a cursor
        cursor = db.cursor()

        # Execute the query to select all states and order by id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all rows and print them
        data = cursor.fetchall()

        for row in data:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    except Exception as e:
        print("Error:", e)
    finally:
        # Close the cursor and the database connection in a finally block
        cursor.close()
        db.close()
>>>>>>> 4af1a2f9cddcdbd0e8ccc7cb2f6b9ac828f01653
