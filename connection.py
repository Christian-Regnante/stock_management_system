from welcome_msg import welcome_msg
import MySQLdb
from MySQLdb import Error

def create_connection():
    connection = None
    try:
        connection = MySQLdb.connect(
            host="localhost", #you can change this to your host address
            user="root", # you can change this to your username
            password="root", # you can change this to your password
            db="stock_system" # you can change this to your database name
        )
        print(welcome_msg)
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection()