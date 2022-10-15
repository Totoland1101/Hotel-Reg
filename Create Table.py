import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234567890",
    database="cs_project"
)
mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE REG (name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("CREATE TABLE REG (RID int  AUTO_INCREMENT,Name varchar(255) ,Phone varchar(255),Nationality varchar(255),Address varchar(255),TyRoom varchar(255), Tyroom1 varchar(255), Uint varchar(255), CheckIn varchar(255), CheckOut varchar(255), Adult varchar(255), Children varchar(255), RoomNum varchar(255), ReservationNum varchar(255), PriceST varchar(255), PriceST1 varchar(255), PriceST2 varchar(255), ADDON varchar(255), PRIMARY KEY (RID));")
mycursor.execute("CREATE TABLE Customer (ID int NOT NULL AUTO_INCREMENT,Name varchar(255) ,Phone varchar(255),Nationality varchar(255),Address varchar(255),TyRoom varchar(255), Tyroom1 varchar(255), Uint varchar(255), CheckIn varchar(255), CheckOut varchar(255), Adult varchar(255), Children varchar(255), RoomNum varchar(255), ReservationNum varchar(255), PriceST varchar(255), PriceST1 varchar(255), PriceST2 varchar(255), ADDON varchar(255), PRIMARY KEY (ID));")


# mycursor.execute("CREATE TABLE REG (RID int  AUTO_INCREMENT,NAME varchar(255) ,CONTACT varchar(255),EMAIL varchar(255),GENDER varchar(255),CITY varchar(255),STATE varchar(255), PRIMARY KEY (RID));")
