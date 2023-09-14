#!/usr/bin/python3

"""
Lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all four arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    try:
        # Establish a connection to the database
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)

        # Create a cursor
        cur = db.cursor()

        # Use a prepared statement to safely insert the state name
        state_name = sys.argv[4]
        query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
        cur.execute(query, (state_name,))

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
