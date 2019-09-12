import mysql.connector
import datetime
import time
from tkinter import *

def Clear_attendance():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="attendance"
    )

    print(mydb)

    mycursor = mydb.cursor()

    
    sql = "truncate table attendance_log"
    mycursor.execute(sql)
    print("The enteries of the previous day are cleared")
Clear_attendance()