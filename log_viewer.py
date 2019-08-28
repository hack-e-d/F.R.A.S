import mysql.connector
import datetime
import time

def View_attendance():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="attendance"
    )

    print(mydb)

    mycursor = mydb.cursor()

    name=''
    current_time=''
    d1=''

    sql = "select * from attendance_log"
    val = (name, current_time, d1)
    mycursor.execute(sql)

    records = mycursor.fetchall()
    print("Total number of rows in Laptop is: ", mycursor.rowcount)
    print("\nPrinting each laptop record")
    for row in records:
        print("Name = ", row[0], )
        print("Date = ", row[1])
        print("Time  = ", row[2],"\n")
    
