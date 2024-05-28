from tkinter import *
from tkinter import messagebox
from jnius import *
from PIL import ImageTk,Image
class Reset_Pass():

    def __init__(self)->None:
        self.sc=Tk()
        img=Image.open("E:/OIP.jpg")
        im_g=ImageTk.PhotoImage(img)
        self.l1=Label(image=im_g)
        self.l1.pack()
        self.sc.geometry("500x400")
        self.sc.title("Reset Pass")
        self.add_Item()
        self.sc.mainloop()
    def add_Item(self)->None:
        self.l1=Label(text="Enter Curr Pass",font=("arial",15,"bold"),bg="orange",fg="black")
        self.l1.place(x=35,y=50,width=200,height=40)
        var1=StringVar()
        var2=StringVar()
        self.i1=Entry(textvariable=var1,font=("arial",15,"bold"),bg="orange",fg="black")
        self.i1.place(x=275,y=50,width=200,height=40)
        self.l2=Label(text="Enter New Password",font=("arial",15,"bold"),bg="orange",fg="black")
        self.l2.place(x=35,y=150,width=200,height=40)
        self.i2=Entry(textvariable=var2,font=("arial",15,"bold"),bg="orange",fg="black")
        self.i2.place(x=275,y=150,width=200,height=40)

        def validate():
            import os
            x=""
            if os.path.exists("password.txt"):
                f1=open("password.txt")
                x=f1.read()
                f1.close()

            y=""
            if os.path.exists("username.txt"):
                f1=open("username.txt")
                y=f1.read()

                f1.close()

            
            if(x==var1.get() and var2.get()!=None and len(var2.get())>=4):
               import mysql.connector
               con=mysql.connector.connect(
                  host="localhost",
                  port="2020",
                  password="2020",
                  username="root"
               )
               try:
                   with con.cursor() as cs:
                       cs.execute("use login")
                       cs.execute("update personaldetail set password=%s where username=%s",(var2.get(),y))
                   con.commit()
                   messagebox.showinfo("Form","PassWord Updated SuccessFully")
               except Exception as e:
                   messagebox.showerror("Alert",e)
               finally:
                   con.close()
            else:
                messagebox.showwarning("Form","Invalid!!")
        def ext():
            self.sc.destroy()
            import Login_
            Login_.Login__()
    

        self.b1=Button(text="Change Pass",font=("arial",15,"bold"),bg="pink",fg="black",command=validate)
        self.b1.place(x=35,y=250,width=430,height=40)
        self.b2=Button(text="Go Back",font=("arial",15,"bold"),bg="pink",fg="black",command=ext)
        self.b2.place(x=35,y=290,width=430,height=40)