from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox

class Screen():

    def __init__(self) -> None:
        self.sc=Tk()
        img=Image.open("E:/Python_image1.jpg")
        im_g=ImageTk.PhotoImage(img)
        self.img=Label(image=im_g)
        self.img.pack()
        self.sc.title("Signup")
        self.sc.geometry("800x700")
        self.__add_item__()
        self.add_input_item()
        self.sc.mainloop()
    def __add_item__(self)->None:
        self.name=Label(text="Name",font=("arial",15,"bold"))
        self.name.place(x=200,y=100,width=200,height=30)
        self.email=Label(text="Email",font=("arial",15,"bold"))
        self.email.place(x=200,y=150,width=200,height=30)
        self.num=Label(text="Phone Number",font=("arial",15,"bold"))
        self.num.place(x=200,y=200,width=200,height=30)
        self.uname=Label(text="User Name",font=("arial",15,"bold"))
        self.uname.place(x=200,y=250,width=200,height=30)
        self.ps=Label(text="Password",font=("arial",15,"bold"))
        self.ps.place(x=200,y=300,width=200,height=30)
        self.cnps=Label(text="Confirm Password",font=("arial",15,"bold"))
        self.cnps.place(x=200,y=350,width=200,height=30)
        x=["Male","Female","Others"]
        self.getgen=StringVar()
        self.gender=OptionMenu(self.sc,self.getgen,*x)
        self.getgen.set("Select Gender")
        self.gender.place(x=420,y=400,width=200,height=30)
    
    def add_input_item(self)->None:
        var1,var2,var3,var4,var5,var6=StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
        self.i1=Entry(textvariable=var1,font=("arial",15,"bold"))
        self.i1.place(x=420,y=100,width=200,height=30)
        self.i2=Entry(textvariable=var2,font=("arial",15,"bold"))
        self.i2.place(x=420,y=150,width=200,height=30)
        self.i3=Entry(textvariable=var3,font=("arial",15,"bold"))
        self.i3.place(x=420,y=200,width=200,height=30)
        self.i4=Entry(textvariable=var4,font=("arial",15,"bold"))
        self.i4.place(x=420,y=250,width=200,height=30)
        self.i5=Entry(textvariable=var5,font=("arial",15,"bold"))
        self.i5.place(x=420,y=300,width=200,height=30)
        self.i6=Entry(textvariable=var6,font=("arial",15,"bold"))
        self.i6.place(x=420,y=350,width=200,height=30)

        def Work()->None:
            x1=var1.get()
            x2=var2.get()
            x3=var3.get()
            x4=var4.get()
            x5=var5.get()
            x6=var6.get()

            gen=self.getgen.get()

            if(x1!=None and x2!=None and x3!=None and x4!=None and x5!=None and x6!=None and gen!=None and gen!="Select Gender"):
                if(len(x1)>=4 and len(x2)>=4 and len(x3)==10 and len(x4)>=4 and len(x5)>=4 and x5==x6):
                    import mysql.connector

                    con=mysql.connector.connect(
                        host="localhost",
                        password="2020",
                        port="2020",
                        username="root"
                    )

                    with con.cursor() as c:
                        c.execute("use login")
                        c.execute("select username from personaldetail where username=%s",[x4])
                        x=c.fetchall()
                        if(len(x)==0):
                            c.execute("insert into personaldetail(name,email,mobile,username,password,gender)values(%s,%s,%s,%s,%s,%s);",[x1,x2,x3,x4,x5,gen])
                            tkinter.messagebox.showinfo(title="Info",message="Account Creation SuccessFull")
                        else:
                            tkinter.messagebox.showerror(title="!!",message="Username Exists")

                    con.commit()
                else:
                    tkinter.messagebox.showerror(title="!!",message="Please Enter Valid Data")
            else:tkinter.messagebox.showerror(title="!!",message="Please Enter Valid Data")

        self.b1=Button(text="SignUp",font=("arial",18,"bold"),bg="orange",command=Work)
        self.b1.place(x=250,y=500,width=300,height=40)
        def ext()->None:
            self.sc.destroy()
            import Screen_
            Screen_.Screen()
        self.b2=Button(text="Return",font=("arial",18,"bold"),bg="orange",command=ext)
        self.b2.place(x=250,y=540,width=300,height=40)

