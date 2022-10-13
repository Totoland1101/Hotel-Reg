import mysql.connector
mydb = mysql.connector.connect(
      host = "localhost",
    user="root",
    password="1234567890",
    database="test03"
)
mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE REG (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("CREATE TABLE REG (RID int NOT NULL AUTO_INCREMENT,NAME varchar(255) NOT NULL,CONTACT varchar(255),EMAIL varchar(255),GENDER varchar(255),CITY varchar(255),STATE varchar(255), PRIMARY KEY (RID));")


# CREATE TABLE REG (RID int NOT NULL AUTO_INCREMENT,NAME varchar(255) NOT NULL,CONTACT varchar(255),EMAIL varchar(255),GENDER varchar(255),CITY varchar(255),STATE varchar(255), PRIMARY KEY (RID));

#อันนี้เป็น ref ของการ CREATE TABLE ถ้าไม่ถนัดใช้ code ไปสร้างในหน้า php ได้ค่า 
# พวกรายละเอียด table อยู่ใน workspace 140 