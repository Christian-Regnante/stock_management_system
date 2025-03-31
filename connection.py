from welcome_msg import welcome_msg
import MySQLdb
from MySQLdb import Error

def create_connection():
    connection = None
    try:
        # Connect to MySQL server without specifying a database
        connection = MySQLdb.connect(
            host="a4ca0c0864c1.7258c438.alu-cod.online", #you can change this to your host address
            user="christian", # you can change this to your username
            port=36472, # you can change this to your port number
            password="root", # you can change this to your password
        )
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS stock_system")
    except Error as e:
        print(f"The error '{e}' occurred while creating the database")

def connect_to_database():
    connection = None
    try:
        # Connect to the specific database after ensuring it exists
        connection = MySQLdb.connect(
            host="a4ca0c0864c1.7258c438.alu-cod.online", #you can change this to your host address
            user="christian", # you can change this to your username
            port=36472, # you can change this to your port number
            password="root", # you can change this to your password
            db="stock_system" # you can change this to your database name
        )
        print(welcome_msg)
    except Error as e:
        print(f"The error '{e}' occurred while connecting to the database")
    return connection

# Step 1: Connect to MySQL server
connection = create_connection()

# Step 2: Create the database if it doesn't exist
if connection:
    create_database(connection)
    connection.close()

# Step 3: Connect to the newly created database
connection = connect_to_database()