import mysql.connector
from mysql.connector import Error

def delete_all_records():
    try:
        connection = mysql.connector.connect(
            host= '192.168.8.161',  # or your MariaDB host
            database= 'MCP',  # replace with your database name
            user= 'ned',  # replace with your database username
            password= 'ned'  # replace with your database password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            query = "DELETE FROM STATS_Machine"
            cursor.execute(query)
            connection.commit()
            print("All records deleted successfully from STATS_machine.")

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    delete_all_records()
