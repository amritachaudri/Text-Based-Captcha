import sqlite3
from tkinter import *
db=sqlite3.connect("ad1.db")
c=db.cursor()
def fun():
    c.execute("INSERT INTO d1 VALUES(?,?,?,?)",(e1.get(),e2.get(),e3.get(),e4.get()))
    d=c.execute("SELECT * FROM d1")
    print(d.fetchall())
top=Tk()
#c.execute('''CREATE TABLE d2 (name text, Mobileno text, age real , email text)''')
#c.execute("INSERT INTO d2 VALUES ( 'A','0987654321',19,'a@gmail.com')")
#c.execute("INSERT INTO d2 VALUES ( 'B','9999955555',20,'b@gmail.com')")
#c.execute("INSERT INTO d2 VALUES ( 'C','9999955555',21,'c@gmail.com')")
#c.execute("INSERT INTO d2 VALUES ( 'D','5555577777',21,'d@gmail.com')")
#c.execute("INSERT INTO d2 VALUES ( 'E','4444433333',22,'e@gmail.com')")
l1=Label(top,text="Enter your name")
e1=Entry(top,border=5)
l1.grid(row=0)
e1.grid(row=0,column=1)
l2=Label(top,text="Enter your Mobile")
e2=Entry(top,border=5)
l2.grid(row=1)
e2.grid(row=1,column=1)
l3=Label(top,text="Enter your age")
e3=Entry(top,border=5)
l3.grid(row=2)
e3.grid(row=2,column=1)
l4=Label(top,text="Enter your email")
e4=Entry(top,border=5)
l4.grid(row=3)
e4.grid(row=3,column=1)
b=Button(top,text="Click",command=fun)
b.grid(row=4,columnspan=2)
d=c.execute("SELECT * FROM d2")
print(d.fetchall())
db.commit()


