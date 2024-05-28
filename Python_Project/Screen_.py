from tkinter import *
from PIL import Image,ImageTk
import Time_
class Screen():

    def __init__(self) -> None:
        self.sc=Tk()
        img=Image.open("E:/92e11abff3c942545c156532e576cba4.jpg")
        im_g=ImageTk.PhotoImage(img)
        self.img=Label(image=im_g)
        self.img.pack()
        self.sc.title("Front Screen")
        self.sc.geometry("1000x700")
        self.label=Label(text="Hotel Reservation System By Group 10",font=("arial",30,"bold"),bg="silver")
        self.label.place(x=50,y=50,width=900,height=60)
        self.add_items()
        self.sc.mainloop()
        pass
    def add_items(self)->None:
        self.l1=Label(text=Time_.show(),font=("arial",15,"bold"),bg="gray")
        self.l1.place(x=100,y=510,width=300,height=30)
        def b1_com()->None:
            self.sc.destroy()
            import Login_
            Login_.Login__()
        self.b1=Button(text="Login",font=("arial",18,"bold"),command=b1_com)
        self.b1.place(x=50,y=550,width=200,height=40)
        def b2_com()->None:
            self.sc.destroy()
            import Sign_Up
            Sign_Up.Screen()
        self.b2=Button(text="Signup",font=("arial",18,"bold"),command=b2_com)
        self.b2.place(x=250,y=550,width=200,height=40)
        def b3_com()->None:
            self.sc.destroy()
            import Reset_pass
            Reset_pass.Reset_Pass()
        self.b3=Button(text="Change Password",font=("arial",15,"bold"),command=b3_com)
        self.b3.place(x=50,y=590,width=200,height=40)
        def ext()->None:
            self.sc.destroy()
            import Main
            Main.exi_t()
        self.b4=Button(text="Exit",font=("arial",18,"bold"),command=ext)
        self.b4.place(x=250,y=590,width=200,height=40)
        pass

import os
if os.path.exists("s.s"):
    os.remove("s.s")
    Screen()