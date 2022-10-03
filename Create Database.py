import mysql.connector
mydb = mysql.connector.connect(
      host = "localhost",
    user="root@localhost",
    password="",
   
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE cs_project")
