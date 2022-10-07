import mysql.connector
mydb = mysql.connector.connect(
      host = "localhost",
    user="root",
    password="1234567890",
    database="Test01"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE REG ( RID int AUTO_INCREMENT,NAME varchar(255) ,EMAIL varchar(255),GENDER varchar(255),CITY varchar(255),STATE varchar(255),PRIMARY KEY (RID)")


# CREATE TABLE REG (
#     RID int NOT NULL AUTO_INCREMENT,
#     NAME varchar(255) NOT NULL,
#     CONTACT varchar(255),
#     EMAIL varchar(255),
#     GENDER varchar(255),
#     CITY varchar(255),
#     STATE varchar(255),
#     PRIMARY KEY (RID)
# );