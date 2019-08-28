import FaceERP_Mark4 as fr
import log_viewer as lv
import tkinter as tk
from functools import partial

def on_closing():
    if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
        top.destroy()

    
def hi(option):
    option=int(option.get())
    if(option==1):
        fr.Detect_face()
    elif(option==2):
        lv.View_attendance()
top = tk.Tk() 
top.wm_title("FRAS")
top.geometry("400x300")  
option=tk.StringVar()
tk.Label(top, text = "Enter  \n1 - Mark attandance\n2 - View attendance").place(x = 30,y = 50)  
tk.Entry(top,textvariable=option).place(x = 95, y = 130)  
hi=partial(hi,option)
on_closeing=partial(on_closing)
tk.Button(top, text = "Submit",activebackground = "pink", activeforeground = "blue",command=hi).place(x = 50, y = 170)
tk.Button(top, text = "Close",activebackground = "pink", activeforeground = "blue",command=on_closing).place(x = 130, y = 170) 
top.mainloop()  
print(option)
