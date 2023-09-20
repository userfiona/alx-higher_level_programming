#!/usr/bin/python3

"""
A script that lists all cities from the database hbtn_0e_4_usa
Username, password, and database names are given as user args
"""

import sys
import MySQLdb

if __name__ == '__main__':
    # Check if all three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3],
                             host='localhost',
                             port=3306)

        # Create a cursor
        cursor = db.cursor()

        # Execute the SQL query to select all cities with their corresponding state names
        sql = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
        """

        cursor.execute(sql)

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
