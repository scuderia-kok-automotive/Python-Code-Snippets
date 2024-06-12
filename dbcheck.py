import mysql.connector

# Replace these values with your MySQL server credentials
host = 'localhost'
user = 'bigg'
password = 'The47ronin#'

# Connect to the MySQL server
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Execute the query to list all databases
    cursor.execute("SHOW DATABASES")

    # Fetch all the rows
    databases = cursor.fetchall()

    # Print the list of databases
    print("List of MySQL databases:")
    for db in databases:
        print(db[0])

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed")
