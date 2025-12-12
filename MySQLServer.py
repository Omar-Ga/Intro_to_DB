#!/usr/bin/python3
"""
A script that creates the database alx_book_store in a MySQL server.
"""
import mysql.connector
from mysql.connector import errorcode

db_connection = None
db_cursor = None

try:
    # Establish connection to MySQL
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    db_cursor = db_connection.cursor()

    # Execute CREATE DATABASE IF NOT EXISTS statement
    db_cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    # If database already exists, script should not fail
    if err.errno == errorcode.ER_DB_CREATE_EXISTS:
        # Silently pass if database exists, as per requirements
        pass
    else:
        # Handle other potential errors
        print(f"An error occurred: {err}")

finally:
    # Close cursor and connection
    if db_cursor:
        db_cursor.close()
    if db_connection and db_connection.is_connected():
        db_connection.close()
