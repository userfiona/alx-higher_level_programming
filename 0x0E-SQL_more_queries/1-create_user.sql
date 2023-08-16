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

    # Create user user_0d_1 if not exists
    create_user_0d_1 = "CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';"
    cursor.execute(create_user_0d_1)
    print("Created user user_0d_1")

    # Grant all privileges to user_0d_1
    grant_privileges_0d_1 = "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';"
    cursor.execute(grant_privileges_0d_1)
    print("Granted all privileges to user_0d_1")

    # Create database hbtn_0d_2 if not exists
    create_database_hbtn_0d_2 = "CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;"
    cursor.execute(create_database_hbtn_0d_2)
    print("Created database hbtn_0d_2")

    # Create user user_0d_2 if not exists
    create_user_0d_2 = "CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';"
    cursor.execute(create_user_0d_2)
    print("Created user user_0d_2")

    # Grant SELECT privilege to user_0d_2 on hbtn_0d_2
    grant_privileges_0d_2 = "GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';"
    cursor.execute(grant_privileges_0d_2)
    print("Granted SELECT privilege to user_0d_2 on hbtn_0d_2")

    # Flush privileges
    cursor.execute("FLUSH PRIVILEGES;")
    print("Flushed privileges")

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
