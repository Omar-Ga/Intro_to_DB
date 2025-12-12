#!/usr/bin/python3
"""
A script that creates the database alx_book_store in a MySQL server.
"""
import mysql.connector
from mysql.connector import errorcode

try:
    # Connect to the MySQL server.
    # NOTE: Please replace 'your_username' and 'your_password' with your actual MySQL credentials.
    cnx = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password"
    )
    cursor = cnx.cursor()

    # Try to create the database.
    try:
        cursor.execute("CREATE DATABASE alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        # If the database already exists, the script should not fail.
        # We check for the specific error code for "database exists".
        if err.errno != errorcode.ER_DB_CREATE_EXISTS:
            print(f"Failed to create database: {err}")
            exit(1)

except mysql.connector.Error as err:
    # Handle errors during connection.
    print(f"Error connecting to MySQL: {err}")
    exit(1)

finally:
    # Ensure that the connection is closed.
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'cnx' in locals() and cnx.is_connected():
        cnx.close()
