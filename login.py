from tkinter import*
from tkinter import messagebox
top=Tk()
def nex():
        if (len(e1.get())==0):
                messagebox.showinfo("NEXT",("Please enter ID"))
        elif(len(e2.get())==0):
                messagebox.showinfo("NEXT",("Please enter password"))
        else:
                import dbms
l1=Label(top,text="ID.:")
l1.grid(row=0)
e1=Entry(top,bd=4,bg="light blue",fg="black")
e1.grid(row=0,column=1)
l2=Label(top,text="Password:")
l2.grid(row=1)
e2=Entry(top,bd=4,bg="light blue",fg="black")
e2.grid(row=1,column=1)
b1=Button(top,text="Next",command=nex)
b1.grid(row=2,columnspan=2)

