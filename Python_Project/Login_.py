from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox
class Login__():
    def __init__(self) -> None:
        self.sc=Tk()
        self.sc.title("Login_Page")
        img=Image.open("E:/Login_Python.png")
        im_g=ImageTk.PhotoImage(img)
        self.img=Label(image=im_g)
        self.img.pack()
        self.sc.geometry("700x800")
        self.add_Item()
        self.sc.mainloop()
        pass

    def add_Item(self)->None:
        self.l1=Label(text="Username",font=("arial",15,"bold"),bg="orange")
        self.l1.place(x=150,y=600,width=200,height=40)
        self.l2=Label(text="Password",font=("arial",15,"bold"),bg="orange")
        self.l2.place(x=150,y=660,width=200,height=40)
        var1,var2=StringVar(),StringVar()
        self.i1=Entry(textvariable=var1,font=("arial",15,"bold"),bg="orange")
        self.i1.place(x=370,y=600,width=200,height=40)
        self.i2=Entry(textvariable=var2,font=("arial",15,"bold"),bg="orange")
        self.i2.place(x=370,y=660,width=200,height=40)

        def work()->None:
            x1=var1.get()
            x2=var2.get()
            if(x1==None or x2==None):
                tkinter.messagebox.showerror(title="!!",message="Enter Valid Input")
            else:
                 import mysql.connector
                 con=mysql.connector.connect(
                   host="localhost",
                    port="2020",
                     username="root",
                     password="2020"
                    )
                 with con.cursor() as c:
                  c.execute("use login")
                  c.execute("select password from personaldetail where username=%s",[x1])
                  x=c.fetchall()
                  if(len(x)==0):tkinter.messagebox.showerror(title="!!",message="UserName Does Not Exists")
                  else:
                      temp=""
                      for i in x[0]:
                          temp+=i
                      if(temp==x2):
                          f=open("username.txt","w")
                          f.write(x1)
                          f=open("password.txt","w")
                          f.write(x2)
                          f.close()
                          with con.cursor() as c:
                              c.execute("select name from personaldetail where username=%s",[x1])
                              x=c.fetchall()
                          f=open("name.txt","w")
                          temp=""
                          for i in x[0]:
                              temp+=i
                          f.write(temp)
                          f.close()
                          self.sc.destroy()
                          import jnius
                          x=jnius.autoclass("Hotel")
                          x.show()
                          fo=open("r.s","w")
                          fo.close()
                          fo=open("r.s")
                          while fo.read()!="True":pass
                          fo.close()
                          pass
                      else:tkinter.messagebox.showerror(title="!!",message="Password Mismatchs")
                          
            pass

        self.b1=Button(text="Login",font=("arial",18,"bold"),bg="orange",command=work)
        self.b1.place(x=150,y=720,width=210,height=40)

        def back()->None:
            self.sc.destroy()
            import Screen_
            Screen_.Screen()
            pass

        self.b2=Button(text="Go Back",font=("arial",18,"bold"),bg="orange",command=back)
        self.b2.place(x=360,y=720,width=210,height=40)
        pass
