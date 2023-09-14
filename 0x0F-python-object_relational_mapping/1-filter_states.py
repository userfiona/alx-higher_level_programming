#!/usr/bin/python3

"""
Script that lists all states with a name starting with N (upper N)
from the database
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Check if all three arguments are provided
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    try:
        # Establish a connection to the database
        db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3])

        # Create a cursor
        cur = db.cursor()

        # Execute the query to select states starting with 'N' and order by id
        cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

        # Fetch all rows and print them
        rows = cur.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    except Exception as e:
        print("Error:", e)
    finally:
        # Clean up process
        cur.close()
        db.close()
