import mysql.connector

class db_connect():
    def get_connection(self):
        db_config = {
            'host': 'localhost',
            'user': 'yourusername', 
            'password': 'yourpassword', 
            'database': 'dbms_project'
        }
        try:
            # Connect to MySQL
            connection = mysql.connector.connect(**db_config)
            return connection

        except mysql.connector.Error as err:
            print("Error:", err)
            return f"Database error: {err}"
    def close_connection(self,connection):
        try:
            cursor = connection.cursor()
            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print("Error:", err)
            return f"Database error: {err}"
