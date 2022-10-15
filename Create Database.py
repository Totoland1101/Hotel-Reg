import mysql.connector
mydb = mysql.connector.connect(
  host = "localhost",
  user="root",
  password="1234567890",
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE cs_project")


