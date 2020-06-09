from tkinter import *
from tkinter import messagebox
root=Tk()
def veiw1():
    if(e1.get()=="HOPE"):
        import user
    else:
        messagebox.showinfo("VEIW",("Sorry,Wrong input"))
canvas = Canvas(root,width = 500, height = 200, bg = 'blue')
canvas.pack()
img = PhotoImage(file = 'c3.png')
canvas.create_image(50, 10, image = img, anchor = NW)
l1=Label(root,text="Enter The Text in image:")
l1.pack()
e1=Entry(root,bd=4,bg="light blue",fg="black")
e1.pack()
b1=Button(root,text="NEXT",command=veiw1)
b1.pack()
root.mainloop()
