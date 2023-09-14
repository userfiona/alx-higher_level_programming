#!/usr/bin/python3

"""
List all cities of a given state from a database
"""

import sys
import MySQLdb

if __name__ == '__main__':
    # Check if all four arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get the arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Establish a connection to the database
        db = MySQLdb.connect(user=username, passwd=password,
                             db=database_name, port=3306)

        # Create a cursor
        cur = db.cursor()

        # Execute the query to select cities of the given state and order by cities.id
        query = "SELECT cities.id, cities.name FROM cities " \
                "JOIN states ON cities.state_id = states.id " \
                "WHERE states.name = %s ORDER BY cities.id ASC"
        cur.execute(query, (state_name,))

        # Fetch all rows and print them
        cities = cur.fetchall()

        for city in cities:
            print(city)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    except Exception as e:
        print("Error:", e)
    finally:
        # Clean up process
        cur.close()
        db.close()
