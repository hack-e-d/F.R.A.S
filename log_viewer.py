import mysql.connector
import datetime
import time
from tkinter import *

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
    lst=[]
    for row in records:
        lst.append([row[0],row[1],row[2]])
    root = Tk()
    t = Text(root)
    i=int(0)
    for x in lst:
        t.insert(END, "\nEntery : "+str(i) , str(i) , "\n\tName = "+ x[0], "\n\tDate = "+ x[1], "\n\tTime = "+ x[2] ,"\n")
        i=i+1
    t.pack()
    root.mainloop()





