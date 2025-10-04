import mysql.connector

dataBase = mysql.connector.connect(
    host="127.0.0.1",
    user="Zaina",
    password="Password123",
    auth_plugin="mysql_native_password"
)

cursorObject = dataBase.cursor()

# Create database only if it doesn't exist
cursorObject.execute("CREATE DATABASE IF NOT EXISTS elderco")

print("All Done!")

