from welcome_msg import welcome_msg
import MySQLdb
from MySQLdb import Error

def create_connection():
    connection = None
    try:
        connection = MySQLdb.connect(
            host="localhost",
            user="root",
            password="root",
            db="stock_system"
        )
        print(welcome_msg)
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection()