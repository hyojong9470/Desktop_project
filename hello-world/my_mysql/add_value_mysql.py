import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='hyojong9470',
    passwd='1234',
    database='mysql'
)

mycursor=mydb.cursor()

mycursor.execute("INSERT INTO customers (name, address) VALUES ('JOH','HIGHway21')")
mydb.commit()

print(mycursor.rowcount, "record insterted.")
