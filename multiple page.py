import numpy as np
import pandas as pd
from tkinter import *
import tkinter.messagebox as tmsg
from PIL import Image,ImageTk
mai=Tk()
def new_window():
    if user.get()!="saeednitjsr@gmail.com":
        tmsg.showinfo(title="message",message="you have entered wrong user id !")
        user.set("")
        password.set("")
    elif user.get()=="saeednitjsr@gmail.com" and password.get()!="saeed12345":
        tmsg.showinfo(title="message", message="you have entered wrong password !")
        password.set("")
    else:
        mai.withdraw()
        root = Toplevel(mai)
        def saeed():
            if name.get()=="" or registration_no.get()=="" or age.get()=="" or gender.get()=="" or branch.get()=="" or phone.get()=="" or e_mail.get()=="":
                 tmsg.showinfo(title="warning",message="Please enter all information")
            else:
                 s.loc[len(s.index) ] = [name.get(),registration_no.get(), age.get(), gender.get(),branch.get(),phone.get(),e_mail.get()]
                 s.to_excel('ss.xlsx', "a",index=False)
                 tmsg.showinfo("message",message="your data uploaded successfully!")
                 name.set("")
                 registration_no.set("")
                 age.set("")
                 gender.set("")
                 branch.set("")
                 e_mail.set("")
                 phone.set("")
                 password.set("")
        def quit():
            ans=tmsg.askquestion(title="warning",message="Are you want to log out ?")
            if ans=="yes":
                root.destroy()
                mai.deiconify()
                password.set("")
        s = pd.read_excel('ss.xlsx', "a")
        root.geometry("500x400")
        name=StringVar()
        registration_no=StringVar()
        age=StringVar()
        gender=StringVar()
        branch=StringVar()
        phone=StringVar()
        e_mail=StringVar()
        Label(root,text="Name :").grid(row=0,column=0,pady=10)
        n=Entry(root,textvariable=name).grid(row=0,column=1,pady=10,ipadx=20)
        Label(root,text="Registration_No :").grid(row=1,column=0,pady=10)
        r=Entry(root,textvariable=registration_no).grid(row=1,column=1,pady=10,ipadx=20)
        Label(root,text="Age :").grid(row=2,column=0,pady=10)
        a=Entry(root,textvariable=age).grid(row=2,column=1,pady=10,ipadx=20)
        Label(root,text="GENDER :").grid(row=3,column=0,pady=10)
        g=Entry(root,textvariable=gender).grid(row=3,column=1,pady=10,ipadx=20)
        Label(root,text="Branch :").grid(row=4,column=0,pady=10)
        ba=Entry(root,textvariable=branch).grid(row=4,column=1,pady=10,ipadx=20)
        Label(root,text="Phone Number :").grid(row=5,column=0,pady=10)
        p=Entry(root,textvariable=phone).grid(row=5,column=1,pady=10,ipadx=20)
        Label(root,text="E-mail :").grid(row=6,column=0,pady=10)
        e=Entry(root,textvariable=e_mail).grid(row=6,column=1,pady=10,ipadx=20)
        b=Button(root,text="Submit",command=saeed)
        b.grid(row=7,column=1,columnspan=10)
        b1 = Button(root, text="logout",command=quit)
        b1.grid(row=7, column=2, columnspan=10)
        mainloop()
def show():
    if shoe.get()==1:
        e = Entry(widget, textvariable=password, borderwidth=5).grid(row=3, column=1, pady=20, ipadx=20)
    elif shoe.get()==0:
        e = Entry(widget, textvariable=password, borderwidth=5,show="*").grid(row=3, column=1, pady=20, ipadx=20)
user=StringVar()
password=StringVar()
shoe=IntVar()
user.set("saeednitjsr@gmail.com")
password.set("")
widget=Canvas(mai,width=705,height=400)
widget.grid()
image=Image.open("C:\\Users\\SAEED UDDIN\\Downloads\\gims.png")
resized_image= image.resize((300,80), Image.ANTIALIAS)
photo=ImageTk.PhotoImage(resized_image)
Label(widget,image=photo).grid(row=0,column=2)
Label(widget,text="PERSONAL DETAILS",font="bold").grid(row=1,column=1,pady=20)
mai.geometry("705x400")
Label(widget, text="user ID :").grid(row=2, column=0)
Entry(widget, textvariable=user,borderwidth=5).grid(row=2, column=1,ipadx=20)
Label(widget, text="Password :").grid(row=3, column=0)
e=Entry(widget, textvariable=password,borderwidth=5,show="*").grid(row=3, column=1,pady=20,ipadx=20)
Checkbutton(widget,text="show password",offvalue=0,onvalue=1,variable=shoe,command=show).grid(row=3,column=1,columnspan=50)
b=Button(widget,text="Login",command=new_window,bg="blue",fg="white",borderwidth=7).grid(row=4,column=1)
Label(widget,text="powered by saeed",bg="white").grid(row=10,columns=2,pady=90)
widget.create_line(0,88,1000,88,fill="black",width=5)
print(password.get())
mainloop()


