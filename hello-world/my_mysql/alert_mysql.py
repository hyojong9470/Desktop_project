import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='hyojong9470',
    passwd='1234',
    database='mysql'
)

mycursor=mydb.cursor()
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
