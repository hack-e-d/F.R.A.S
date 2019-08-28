import mysql.connector
import datetime
import time

def Mark_attendance(name):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="attendance"
    )

    print(mydb)

    mycursor = mydb.cursor()

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)

    today = datetime.date.today()
    d1 = today.strftime("%Y-%m-%d")
    print(d1)

    sql = "INSERT INTO attendance_log (Name,  Time) VALUES (%s, %s)"
    sql = "INSERT INTO attendance_log (Name, Date, Time) VALUES (%s, %s, %s)"
    val = (name, current_time, d1)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    
