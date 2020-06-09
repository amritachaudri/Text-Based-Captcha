from tkinter import *
from tkinter import messagebox
t=Tk()    
def sub():
    if (len(e2.get())==0):
        messagebox.showinfo("Submit",("Please enter first name"))
    elif(len(e3.get())==0):
        messagebox.showinfo("Submit",("Please enter last name"))
    elif(len(e4.get())==0):
        messagebox.showinfo("Submit",("Please enter ID"))
    elif(len(e5.get())==0):
        messagebox.showinfo("Submit",("Please enter Specialization"))
    elif(len(e6.get())==0):
        messagebox.showinfo("Submit",("Please enter Mobile No"))
    elif(len(e7.get())==0):
        messagebox.showinfo("Submit",("Please enter Email id"))
    elif(len(e8.get())==0):
        messagebox.showinfo("Submit",("Please enter Password"))
    elif(len(e6.get())!=0):
        mob()
    elif(len(e8.get())!=0):
        check()
    else:
        messagebox.showinfo("Submit",("User Created Sucessfull"))
def mob():
    m=s1.get()
    if(len(m)!=10):
        messagebox.showinfo("mobile",("The mobile no is invalid"))
    elif(len(m)==10):
        messagebox.showinfo("Submit",("User Created Sucessfull"))
       
def check():
    s=s2.get()
    l=0
    u=0
    d=0
    if(6<len(s)<=10):
        for i in s:
            if i.isupper():
                u=1
            if i.islower():
                l=1
            if i.isdigit():
                d=1
        if(u==1 and l==1 and d==1):
            messagebox.showinfo("password",("password fulfills the condination"))
        else:
            messagebox.showinfo("password",("The password should contain an upper case ,lower case and a digit"))
    else:
            messagebox.showinfo("password",("The password should contain an upper case ,lower case and a digit"))
   
def log():
    import login
s1=StringVar()
s2=StringVar()
l1=Label(t,text="WELCOME TO THE PROJECT OF TEXT BASED CAPTCHA USING PYTHON")
l1.grid(row=0,columnspan=2)
l2=Label(t,text="Name:")
l2.grid(row=1)
e2=Entry(t,bd=4,bg="light blue",fg="black")
e2.grid(row=1,column=1)
l3=Label(t,text="Lat Name:")
l3.grid(row=2)
e3=Entry(t,bd=4,bg="light blue",fg="black")
e3.grid(row=2,column=1)
l4=Label(t,text="ID:")
l4.grid(row=3)
e4=Entry(t,bd=4,bg="light blue",fg="black")
e4.grid(row=3,column=1)
l5=Label(t,text="Specialization:")
l5.grid(row=4)
e5=Entry(t,bd=4,bg="light blue",fg="black")
e5.grid(row=4,column=1)
l6=Label(t,text="Mobile No.:")
l6.grid(row=5)
e6=Entry(t,bd=4,bg="light blue",fg="black",textvariable=s1)
e6.grid(row=5,column=1)
l7=Label(t,text="Email Id:")
l7.grid(row=6)
e7=Entry(t,bd=4,bg="light blue",fg="black")
e7.grid(row=6,column=1)
l8=Label(t,text="Enter Password")
l8.grid(row=7)
e8=Entry(t,bd=4,bg="light blue",fg="black",textvariable=s2)
e8.grid(row=7,column=1)
l9=Label(t,text="Gender:")
l9.grid(row=8)
r=IntVar()
r1=Radiobutton(t,text="  Male",variable=r,value=0)
r1.grid(row=8,column=1)
r2=Radiobutton(t,text="Female",variable=r,value=1)
r2.grid(row=9,column=1)
r3=Radiobutton(t,text="Others",variable=r,value=2)
r3.grid(row=10,column=1)
b1=Button(t,text="Submit",command=sub)
b1.grid(row=11,columnspan=2)
b2=Button(t,text="Login Page",command=log)
b2.grid(row=12,columnspan=3)

