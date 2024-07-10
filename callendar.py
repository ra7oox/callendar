#Ra7oox
import calendar
from tkinter import *
from tkinter  import messagebox


root=Tk()
root.geometry("400x400")
root.title("callendar")
label1=Label(root,text="enter the year")
label1.place(x=140,y=50)
input1=Entry(root)
input1.place(x=120,y=80)
label2=Label(root,text="enter the month")
label2.place(x=140,y=120)
input2=Entry(root)
input2.place(x=120,y=160)

def show():
    messagebox.showinfo("callendar",calendar.month(int(input1.get()),int(input2.get())))
    
button=Button(root,text="click",command=show)
button.place(x=150,y=200)



root.mainloop()