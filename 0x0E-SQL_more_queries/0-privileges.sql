import mysql.connector

# MySQL server configuration
config = {
    'user': 'root',  # Change to your MySQL username
    'password': 'your_password',  # Change to your MySQL password
    'host': 'localhost',
}

# Connect to MySQL server
try:
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Create user user_0d_1
    create_user_0d_1 = "CREATE USER 'user_0d_1'@'localhost';"
    cursor.execute(create_user_0d_1)
    print("Created user user_0d_1")

    # Grant privileges to user_0d_1
    grant_privileges_0d_1 = "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';"
    cursor.execute(grant_privileges_0d_1)
    print("Granted privileges to user_0d_1")

    # Try to list privileges for user_0d_1
    try:
        query_show_grants_0d_1 = "SHOW GRANTS FOR 'user_0d_1'@'localhost';"
        cursor.execute(query_show_grants_0d_1)
        grants_0d_1 = cursor.fetchall()

        print("Grants for user_0d_1@localhost:")
        for grant in grants_0d_1:
            print(grant[0])

    except mysql.connector.Error as e:
        print("Error listing privileges for user_0d_1:", e)

    # Try to list privileges for user_0d_2
    try:
        query_show_grants_0d_2 = "SHOW GRANTS FOR 'user_0d_2'@'localhost';"
        cursor.execute(query_show_grants_0d_2)
        grants_0d_2 = cursor.fetchall()

        print("\nGrants for user_0d_2@localhost:")
        for grant in grants_0d_2:
            print(grant[0])

    except mysql.connector.Error as e:
        print("Error listing privileges for user_0d_2:", e)

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
