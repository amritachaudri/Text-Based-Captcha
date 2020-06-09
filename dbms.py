from tkinter import*
from tkinter import messagebox
top1=Tk()

def veiw():
    if (len(e1.get())==0):
        messagebox.showinfo("VEIW",("Please enter Specialization"))
    elif((e1.get()=="Admin")or(e1.get()=="admin")or(e1.get()=="ADMIN")):
        import  insert
    elif((e1.get()=="student")or(e1.get()=="Student")or(e1.get()=="STUDENT")):
        import data2
    elif((e1.get()=="teacher")or(e1.get()=="Teacher")or(e1.get()=="TEACHER")):
        import data2
    else:
        messagebox.showinfo("VEIW",("Sorry no user found"))
l1=Label(top1,text="Specialization:")
l1.pack()
e1=Entry(top1,bd=4,bg="light blue",fg="black")
e1.pack()
b1=Button(top1,text="Veiw",command=veiw)
b1.pack()


