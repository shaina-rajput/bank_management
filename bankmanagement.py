import tkinter
from tkinter import messagebox
from tkinter import StringVar
from tkinter import IntVar
from tkinter.ttk import *
import mysql.connector
import smtplib
import datetime
convar=mysql.connector.connect(
   host='localhost',
   user='root',
   passwd='',
   database='bankmanagement'
    )
mycur=convar.cursor()
#window variables
window1=None
window2=None
window3=None
window4=None
window5=None

#window variables
namef=[]
acco=[]

#string variables
ch=None
search=None
nameset=None
usertxt1=None
tfname=None
tmname=None
tlname=None
tacc1=None
tacc=None
tfname2=None
tmname2=None
tlname2=None
datett=None
temail=None
taadhar=None
tphoneno=None
trv=None
tracc=None
trname=None
trbalance=None
trwithdrawl=None
trdeposit=None
trfina=None
tremail=None
trtime=None
#string variables
#windows start
def window2opener():
    window1.destroy()
    win2open()

def window3opener():
    window2.destroy()

def window4opener():
    window3.destroy()
    win4open()

def window2new():
    messagebox.showinfo("SPR bank","account is created")
    window4.destroy()
    win2open()

def window2new1():
    messagebox.showinfo("SPR bank","account is created")
    window3.destroy()
    win2open()
def window5opener():
    window2.destroy()
    cashbook()
def window2new2():
    if messagebox.askyesno('confirm please','Are you sure you want to exit'):
            window5.destroy()
            win2open()
    else:
        return True
#window end
#*****************************LOGIN PAGE**************************************************

def login():
    if(usrtxt.get()=='sprbank@2000' and passtxt.get()=='sprbank'):
        window2opener()
        
    else:
        messagebox.showinfo("SPR bank","username or password error")
def logout():
    window2.destroy()

window1=tkinter.Tk()
window1.geometry('500x500+400+50')

usrtxt=tkinter.StringVar(window1)
passtxt=tkinter.StringVar(window1)

window1.configure(background='light yellow')
window1.title('SPR bank',)
window1.iconbitmap(r'favicon (2).ico')
txt=tkinter.Label(window1,text='Welcome to SPR Bank',font=('Gabriola',40),fg='white',bg='blue')
txt.pack()

photo=tkinter.PhotoImage(file='treasury.png')
labelphoto=tkinter.Label(window1,image=photo,bg='light yellow')
labelphoto.place(x=15,y=150)

txt23=tkinter.Label(window1,text='Location=Ghaziabad    phoneno=3849074667   email=sprbanktrust@gmail.com',font=('Gabriola',15),fg='white',bg='blue')
txt23.place(x=5,y=450)


username=tkinter.Entry(window1,bd=4,textvariable=usrtxt)
username.place(x=310,y=190,height=25,width=100)

password=tkinter.Entry(window1,bd=4,show='*',textvariable=passtxt)
password.place(x=310,y=230,height=25,width=100)

usrlbl=tkinter.Label(window1,text='Username :',font=('Gabriola'),bg='light yellow',fg='black')
usrlbl.place(x=160,y=190,height=25,width=150)

passlbl=tkinter.Label(window1,text='Password :',font=('Gabriola'),bg='light yellow',fg='black')
passlbl.place(x=160,y=230,height=25,width=150)

photo2=tkinter.PhotoImage(file='user.png')
btnphoto=tkinter.Button(window1,image=photo2,bg='light yellow',command=login)
btnphoto.place(x=290,y=300)


#*********************************LOGIN ENDS********************************************

#**********************************DATABASE WORK**************************************
def databaseenter():
    global mycur
    global convar
    global tbalance
    global ch
    ch=datetime.datetime.now()
    query="insert into account values('"+tfname.get()+"','"+tmname.get()+"','"+tlname.get()+"','"+tacc1.get()+"','"+str(ch)+"','"+temail.get()+"','"+tphoneno.get()+"','"+taadhar.get()+"','"+str(tbalance.get())+"')"
    mycur.execute(query)
    convar.commit()
    
    window2new1()

def databaseenter1():
    global mycur
    global convar
    global ch
    ch=datetime.datetime.now()
    
    mycur.execute("insert into account values('"+tfname.get()+"','"+tmname.get()+"','"+tlname.get()+"','"+tacc1.get()+"','"+str(ch)+"','"+temail.get()+"','"+tphoneno.get()+"','"+taadhar.get()+"','"+str(tbalance.get())+"')")
    convar.commit()
    window2new()
#****************************DATABASE END*****************************************8

    
#********************************************main menu starts*******************************
def win2open():
    global window2
    window2=tkinter.Tk()
    window2.geometry('500x500+400+50')
    window2.title('SPR bank')
    window2.iconbitmap(r'favicon (2).ico')
    window2.configure(background='light yellow')

    mainmenu=tkinter.Label(window2,text='MAIN MENU',font=('Gabriola',40),bg='blue',fg='white')
    mainmenu.pack()

    main1=tkinter.Radiobutton(window2,text='Create new Account',value=1,font=('Gabriola',16),bg='light yellow',fg='black',activeforeground='blue',command=form)
    main1.place(x=90,y=165)
    main2=tkinter.Radiobutton(window2,text='Account details',value=2,font=('Gabriola',16),bg='light yellow',fg='black',activeforeground='blue',command=window5opener)
    main2.place(x=90,y=230)
 
    btnlogout=tkinter.Button(window2,text="LOGOUT",activebackground='red',command=logout)
    btnlogout.place(x=250,y=350,height=25,width=150)

    txt23=tkinter.Label(window2,text='Location=Ghaziabad    phoneno=3849074667   email=sprbanktrust@gmail.com',font=('Gabriola',15),fg='white',bg='blue')
    txt23.place(x=5,y=450)

#*********************************************main menu end****************************************

#**********************************************ACCOUNT CREATE WORK START*****************************************


def submit():
    btnsubmit=tkinter.Button(window3,text="SUBMIT",command=databaseenter)
    btnsubmit.place(x=500,y=650,height=25,width=150)
    
    
def submit1():
    
    btnsubmit=tkinter.Button(window4,text="SUBMIT",command=databaseenter1)
    btnsubmit.place(x=500,y=650,height=25,width=150)
    
    

def nominee1():

   
    global tbalance
    
    tbalance=IntVar(window4)
    nomname=tkinter.Label(window4,text='Name of nominee :',font=('Gabriola'),bg='light blue',fg='black')
    nomname.place(x=10,y=165)    
    fnameno=tkinter.Label(window4,text='Frist Name :',font=('Gabriola'),bg='light blue',fg='black')
    fnameno.place(x=10,y=195)    
    nomname1=tkinter.Entry(window4,bd=4)
    nomname1.place(x=100,y=205,height=20,width=100)
    mnameno=tkinter.Label(window4,text='Middle Name :',font=('Gabriola'),bg='light blue',fg='black')
    mnameno.place(x=230,y=195)    
    mmnameno=tkinter.Entry(window4,bd=4)
    mmnameno.place(x=330,y=205,height=20,width=100)
    lnameno=tkinter.Label(window4,text='Last Name :',font=('Gabriola'),bg='light blue',fg='black')
    lnameno.place(x=450,y=195)    
    llnameno=tkinter.Entry(window4,bd=4)
    llnameno.place(x=530,y=205,height=20,width=100)
    dobno=tkinter.Label(window4,text='Date of Birth :',font=('Gabriola'),bg='light blue',fg='black')
    dobno.place(x=10,y=245)    
    dno=tkinter.Label(window4,text='Date :',font=('Gabriola'),bg='light blue',fg='black')
    dno.place(x=95,y=245)
    combono=Combobox(window4)
    combono['values']=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
    combono.current()
    combono.place(x=140,y=255,height=20,width=50)
    mno=tkinter.Label(window4,text='Month :',font=('Gabriola'),bg='light blue',fg='black')
    mno.place(x=200,y=245)  
    combo1no=Combobox(window4)
    combo1no['values']=('January','Feberary','March','April','May','June','July','August','Semptember','October','November','December')
    combo1no.current()
    combo1no.place(x=260,y=255,height=20,width=75)   
    yno=tkinter.Label(window4,text='Year :',font=('Gabriola'),bg='light blue',fg='black')
    yno.place(x=350,y=245)    
    yyno=tkinter.Entry(window4,bd=4)
    yyno.place(x=400,y=255,height=20,width=75)
    bal=tkinter.Label(window4,text='opening balance :',font=('Gabriola'),bg='light blue',fg='black')
    bal.place(x=15,y=355)
    balno=tkinter.Entry(window4,bd=4,textvariable=tbalance)
    balno.place(x=120,y=365,height=20,width=100)

    submit1()
    

def date1():


    global tbalance
    
    tbalance=IntVar(window4)
    bal=tkinter.Label(window4,text='Opening balance :',font=('Gabriola'),bg='light blue',fg='black')
    bal.place(x=15,y=355)
    balno=tkinter.Entry(window4,bd=4,textvariable=tbalance)
    balno.place(x=120,y=365,height=20,width=100)

    submit1()
    
def nominee():

    global tbalance
    
    tbalance=IntVar(window3)
    nomname=tkinter.Label(window3,text='Name of nominee :',font=('Gabriola'),bg='light blue',fg='black')
    nomname.place(x=10,y=465)    
    fnameno=tkinter.Label(window3,text='Frist Name :',font=('Gabriola'),bg='light blue',fg='black')
    fnameno.place(x=10,y=495)    
    nomname1=tkinter.Entry(window3,bd=4)
    nomname1.place(x=100,y=505,height=20,width=100)
    mnameno=tkinter.Label(window3,text='Middle Name :',font=('Gabriola'),bg='light blue',fg='black')
    mnameno.place(x=230,y=495)    
    mmnameno=tkinter.Entry(window3,bd=4)
    mmnameno.place(x=330,y=505,height=20,width=100)
    lnameno=tkinter.Label(window3,text='Last Name :',font=('Gabriola'),bg='light blue',fg='black')
    lnameno.place(x=450,y=495)    
    llnameno=tkinter.Entry(window3,bd=4)
    llnameno.place(x=530,y=505,height=20,width=100)
    dobno=tkinter.Label(window3,text='Date of Birth :',font=('Gabriola'),bg='light blue',fg='black')
    dobno.place(x=10,y=545)    
    dno=tkinter.Label(window3,text='Date :',font=('Gabriola'),bg='light blue',fg='black')
    dno.place(x=95,y=545)
    combono=Combobox(window3)
    combono['values']=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
    combono.current()
    combono.place(x=140,y=555,height=20,width=50)
    mno=tkinter.Label(window3,text='Month :',font=('Gabriola'),bg='light blue',fg='black')
    mno.place(x=200,y=545)  
    combo1no=Combobox(window3)
    combo1no['values']=('January','Feberary','March','April','May','June','July','August','Semptember','October','November','December')
    combo1no.current()
    combo1no.place(x=260,y=555,height=20,width=75)   
    yno=tkinter.Label(window3,text='Year :',font=('Gabriola'),bg='light blue',fg='black')
    yno.place(x=350,y=545)    
    yyno=tkinter.Entry(window3,bd=4)
    yyno.place(x=400,y=555,height=20,width=75)
    bal=tkinter.Label(window3,text='Opening balance :',font=('Gabriola'),bg='light blue',fg='black')
    bal.place(x=15,y=600)
    balno=tkinter.Entry(window3,bd=4,textvariable=tbalance)
    balno.place(x=120,y=610,height=20,width=100)
    
    submit()


def date():
    
    global tbalance
    
    tbalance=IntVar(window3)
    bal=tkinter.Label(window3,text='Opening balance :',font=('Gabriola'),bg='light blue',fg='black')
    bal.place(x=15,y=465)
    balno=tkinter.Entry(window3,bd=4,textvariable=tbalance)
    balno.place(x=120,y=475,height=20,width=150)
    
    submit()



def singleacc():

    mode=tkinter.Label(window4,text='Nomination Required :',font=('Gabriola'),bg='light blue',fg='black')
    mode.place(x=10,y=380)
    yes=tkinter.Radiobutton(window3,text='YES ',value=1,font=('Gabriola'),bg='light blue',fg='black',command=nominee)
    yes.place(x=60,y=425)
    no=tkinter.Radiobutton(window3,text='NO ',value=2,font=('Gabriola'),bg='light blue',fg='black',command=date)
    no.place(x=250,y=425)


def win4open():

    global window4
    window4=tkinter.Tk()
    window4.geometry('700x700+320+5')
    window4.title('SPR bank Form')
    window4.iconbitmap(r'favicon (2).ico')
    window4.configure(background='light blue')
    
    mode=tkinter.Label(window4,text='Mode of operation :',font=('Gabriola'),bg='light blue',fg='black')
    mode.place(x=10,y=10)    
    self=tkinter.Checkbutton(window4,text='Self ',onvalue=1,font=('Gabriola'),bg='light blue',fg='black')
    self.place(x=60,y=50)
    eith=tkinter.Checkbutton(window4,text='Either or survivor ',onvalue=2,font=('Gabriola'),bg='light blue',fg='black')
    eith.place(x=250,y=50)
    mode=tkinter.Label(window4,text='Nomination Required :',font=('Gabriola'),bg='light blue',fg='black')
    mode.place(x=10,y=90)
    yes=tkinter.Radiobutton(window4,text='YES ',value=1,font=('Gabriola'),bg='light blue',fg='black',command=nominee1)
    yes.place(x=60,y=130)
    no=tkinter.Radiobutton(window4,text='NO ',value=2,font=('Gabriola'),bg='light blue',fg='black',command=date1)
    no.place(x=250,y=130)
   




def jointacc():

    nomname=tkinter.Label(window3,text='Name of second candidate :',font=('Gabriola'),bg='light blue',fg='black')
    nomname.place(x=10,y=315)  
    fname=tkinter.Label(window3,text='Frist Name :',font=('Gabriola'),bg='light blue',fg='black')
    fname.place(x=10,y=345)    
    ffname=tkinter.Entry(window3,bd=4)
    ffname.place(x=100,y=355,height=20,width=100)
    mname=tkinter.Label(window3,text='Middle Name :',font=('Gabriola'),bg='light blue',fg='black')
    mname.place(x=230,y=345)    
    mmname=tkinter.Entry(window3,bd=4)
    mmname.place(x=330,y=355,height=20,width=100)
    lname=tkinter.Label(window3,text='Last Name :',font=('Gabriola'),bg='light blue',fg='black')
    lname.place(x=450,y=345)    
    llname=tkinter.Entry(window3,bd=4)
    llname.place(x=530,y=355,height=20,width=100)
    dob=tkinter.Label(window3,text='Date of Birth :',font=('Gabriola'),bg='light blue',fg='black')
    dob.place(x=10,y=380)    
    d=tkinter.Label(window3,text='Date :',font=('Gabriola'),bg='light blue',fg='black')
    d.place(x=95,y=380)
    combo=Combobox(window3)
    combo['values']=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
    combo.current()
    combo.place(x=140,y=390,height=20,width=50)
    m=tkinter.Label(window3,text='Month :',font=('Gabriola'),bg='light blue',fg='black')
    m.place(x=200,y=380)  
    combo1=Combobox(window3)
    combo1['values']=('January','Feberary','March','April','May','June','July','August','Semptember','October','November','December')
    combo1.current()
    combo1.place(x=260,y=390,height=20,width=75)   
    y=tkinter.Label(window3,text='Year :',font=('Gabriola'),bg='light blue',fg='black')
    y.place(x=350,y=380)    
    yy=tkinter.Entry(window3,bd=4)
    yy.place(x=400,y=390,height=20,width=75)
    ad=tkinter.Label(window3,text='Address :',font=('Gabriola'),bg='light blue',fg='black')
    ad.place(x=10,y=420)    
    add=tkinter.Entry(window3,bd=4)
    add.place(x=75,y=420,height=25,width=620)
    email=tkinter.Label(window3,text='Email :',font=('Gabriola'),bg='light blue',fg='black')
    email.place(x=10,y=460)    
    email1=tkinter.Entry(window3,bd=4)
    email1.place(x=70,y=470,height=25,width=500)
    phn=tkinter.Label(window3,text='Phone no :',font=('Gabriola'),bg='light blue',fg='black')
    phn.place(x=10,y=510)    
    phnno=tkinter.Entry(window3,bd=4)
    phnno.place(x=85,y=520,height=20,width=160)
    phn2=tkinter.Label(window3,text='reference no :',font=('Gabriola'),bg='light blue',fg='black')
    phn2.place(x=280,y=510)    
    phnno2=tkinter.Entry(window3,bd=4)
    phnno2.place(x=380,y=520,height=20,width=160)
    adh=tkinter.Label(window3,text='Aadhar card no :',font=('Gabriola'),bg='light blue',fg='black')
    adh.place(x=10,y=550)    
    aadh=tkinter.Entry(window3,bd=4)
    aadh.place(x=130,y=560,height=20,width=160)
    btnnext=tkinter.Button(window3,text="NEXT",activebackground='green',command=window4opener)
    btnnext.place(x=350,y=650,height=25,width=150)



    
def form():
    window3opener()
    global tfname
    global tmname
    global tlname
    global tacc1
    global temail
    global tphoneno
    global taadhar
    global window3
    window3=tkinter.Tk()
    window3.geometry('700x700+320+5')
    window3.title('SPR bank Form')
    window3.iconbitmap(r'favicon (2).ico')
    window3.configure(background='light blue')
    tfname=StringVar(window3)
    tmname=StringVar(window3)
    tlname=StringVar(window3)    
    tacc1=StringVar(window3)
    temail=StringVar(window3)
    tphoneno=StringVar(window3)
    taadhar=StringVar(window3)
    
    fname=tkinter.Label(window3,text='Frist Name :',font=('Gabriola'),bg='light blue',fg='black')
    fname.place(x=10,y=10)    
    ffname=tkinter.Entry(window3,bd=4,textvariable=tfname)
    ffname.place(x=100,y=20,height=20,width=100)
    mname=tkinter.Label(window3,text='Middle Name :',font=('Gabriola'),bg='light blue',fg='black')
    mname.place(x=230,y=10)    
    mmname=tkinter.Entry(window3,bd=4,textvariable=tmname)
    mmname.place(x=330,y=20,height=20,width=100)
    lname=tkinter.Label(window3,text='Last Name :',font=('Gabriola'),bg='light blue',fg='black')
    lname.place(x=450,y=10)    
    llname=tkinter.Entry(window3,bd=4,textvariable=tlname)
    llname.place(x=530,y=20,height=20,width=100)
    dob=tkinter.Label(window3,text='Date of Birth :',font=('Gabriola'),bg='light blue',fg='black')
    dob.place(x=10,y=45)    
    d=tkinter.Label(window3,text='Date :',font=('Gabriola'),bg='light blue',fg='black')
    d.place(x=95,y=45)
    combo=Combobox(window3)
    combo['values']=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
    combo.current()
    combo.place(x=140,y=55,height=20,width=50)
    m=tkinter.Label(window3,text='Month :',font=('Gabriola'),bg='light blue',fg='black')
    m.place(x=200,y=45)  
    combo1=Combobox(window3)
    combo1['values']=('January','Feberary','March','April','May','June','July','August','Semptember','October','November','December')
    combo1.current()
    combo1.place(x=260,y=55,height=20,width=75)   
    y=tkinter.Label(window3,text='Year :',font=('Gabriola'),bg='light blue',fg='black')
    y.place(x=350,y=45)    
    yy=tkinter.Entry(window3,bd=4)
    yy.place(x=400,y=55,height=20,width=75)
    ad=tkinter.Label(window3,text='Address :',font=('Gabriola'),bg='light blue',fg='black')
    ad.place(x=10,y=80)    
    add=tkinter.Entry(window3,bd=4)
    add.place(x=75,y=90,height=25,width=620)
    email=tkinter.Label(window3,text='Email :',font=('Gabriola'),bg='light blue',fg='black')
    email.place(x=10,y=130)    
    email1=tkinter.Entry(window3,bd=4,textvariable=temail)
    email1.place(x=70,y=135,height=25,width=500)
    phn=tkinter.Label(window3,text='Phone no :',font=('Gabriola'),bg='light blue',fg='black')
    phn.place(x=10,y=175)    
    phnno=tkinter.Entry(window3,bd=4,textvariable=tphoneno)
    phnno.place(x=85,y=185,height=20,width=160)
    phn2=tkinter.Label(window3,text='reference no :',font=('Gabriola'),bg='light blue',fg='black')
    phn2.place(x=280,y=175)    
    phnno2=tkinter.Entry(window3,bd=4)
    phnno2.place(x=380,y=185,height=20,width=160)

    adh=tkinter.Label(window3,text='Aadhar card no :',font=('Gabriola'),bg='light blue',fg='black')
    adh.place(x=10,y=215)    
    aadh=tkinter.Entry(window3,bd=4,textvariable=taadhar)
    aadh.place(x=130,y=225,height=20,width=160)

    acc=tkinter.Label(window3,text='Account no. allocated :',font=('Gabriola'),bg='light blue',fg='black')
    acc.place(x=300,y=215)    
    acco=tkinter.Entry(window3,bd=4,textvariable=tacc1)
    acco.place(x=450,y=225,height=20,width=160)
    
    acctype=tkinter.Label(window3,text='Account Type :',font=('Gabriola'),bg='light blue',fg='black')
    acctype.place(x=10,y=250)
    combo3=Combobox(window3)
    combo3['values']=('Saving Account','Current Account','Fix Deposit','Recurring Deposit')
    combo3.current()
    combo3.place(x=120,y=260,height=20,width=160)   
    adhS=tkinter.Checkbutton(window3,text='Single Account : ',font=('Gabriola'),bg='light blue',fg='black',onvalue=1,command=singleacc)
    adhS.place(x=60,y=280)
    adhJ=tkinter.Checkbutton(window3,text='Joint Account : ',font=('Gabriola'),bg='light blue',fg='black',onvalue=2,command=jointacc)
    adhJ.place(x=250,y=280)
    
#**************************************************ACCOUNT CREATE WORK ENDS*****************************************************************

#***************************************************ACCOUNT DETAILS WORK START**************************************************
def update(rows):
    global trv
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('','end',values=i)

        
def clear():
    query='SELECT fristname,lastname,accountno,email,accountcreated,closingbalance from account'
    mycur.execute(query)
    rows=mycur.fetchall()
    update(rows)

def getrow(event):
    global tracc
    global trname
    global trbalance
    global tremail
    global trtime
    rowid=trv.identify_row(event.y)
    item=trv.item(trv.focus())
    tracc.set(item['values'][2])
    trname.set(item['values'][0])
    trbalance.set(item['values'][5])
    tremail.set(item['values'][3])
    trtime.set(item['values'][4])
    

def delete():
    global tracc
    if messagebox.askyesno('confirm delete?','Are you sure you want to delete this account'):
           query='DELETE FROM account WHERE accountno="'+tracc.get()+'"'
           mycur.execute(query)
           convar.commit()
           clear()
    else:
        return True

def updatenew():
    global trwithdrawl
    global trdeposit
    global trfinal
    global tracc
    global trbalance
    global tremail
    global ch
    if messagebox.askyesno('confirm please','Are you sure you want to update this account'):
        try:
          if(trwithdrawl.get()!=0):
            totalsub =trbalance.get()-trwithdrawl.get()
            if(totalsub<0):
                messagebox.showinfo("SPR bank","insufficient balance!")
                clear()
            else:
                query='UPDATE account SET closingbalance="'+str(totalsub)+'" WHERE accountno="'+tracc.get()+'"'
                mycur.execute(query)
                trbalance.set(totalsub)
                trfinal.set(totalsub)
                s=smtplib.SMTP('smtp.gmail.com',587)
                s.starttls()
                s.login('shainaofficial3100@gmail.com','shaina@2000')
                message='Rs. '+str(trwithdrawl.get())+' Amount is withdrawl from SPR BANK. Balance amount in your account is Rs. '+str(trfinal.get())
                s.sendmail('shainaofficial3100@gmail.com','"'+tremail.get()+'"',message)
                s.quit()
                messagebox.showinfo("SPR bank","email sent")
                ch=datetime.datetime.now()
                query2='UPDATE account SET accountcreated="'+str(ch)+'" WHERE accountno="'+tracc.get()+'"'
                mycur.execute(query2)
                convar.commit()
                clear()
          else:
            totalsum =trbalance.get()+trdeposit.get()
            query1='UPDATE account SET closingbalance="'+str(totalsum)+'" WHERE accountno="'+tracc.get()+'"'
            mycur.execute(query1)
            convar.commit()
            trbalance.set(totalsum)
            trfinal.set(totalsum)
            s=smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login('shainaofficial3100@gmail.com','shaina@2000')
            message='Rs. '+str(trdeposit.get())+' Amount is deposit to SPR BANK. Balance amount in your account is Rs. '+str(trfinal.get())
            s.sendmail('shainaofficial3100@gmail.com','"'+tremail.get()+'"',message)
            s.quit()
            messagebox.showinfo("SPR bank","email is sent")
            ch=datetime.datetime.now()
            query4='UPDATE account SET accountcreated="'+str(ch)+'" WHERE accountno="'+tracc.get()+'"'
            mycur.execute(query4)
            convar.commit()
            clear()
        except:
            messagebox.showinfo("SPR bank","something is went wrong! please check the details")           

    else:
        return True
    

    
def search1(): 
       query='SELECT fristname,lastname,accountno,email,accountcreated,closingbalance from account WHERE fristname LIKE "'+search.get()+'" or lastname LIKE "'+search.get()+'"'
       mycur.execute(query)
       rows=mycur.fetchall()
       update(rows)
def cashbook():
    global mycur
    global usertext1
    global window5
    global trv
    global search
    global tracc
    global trname
    global trbalance

    global trwithdrawl
    global trdeposit
    global trfinal
    global tremail
    global trtime
    
    window5=tkinter.Tk()
    window5.geometry('1250x900+50+5')
    window5.configure(background='light blue')
    window5.title('SPR bank')
    window5.iconbitmap(r'favicon (2).ico')
    
    search=StringVar(window5)
    tracc=StringVar(window5)
    trname=StringVar(window5)
    trbalance=IntVar(window5)
    trwithdrawl=IntVar(window5)
    trdeposit=IntVar(window5)
    trfinal=IntVar(window5)
    tremail=StringVar(window5)
    trtime=StringVar(window5)
    
    wrapper1=tkinter.LabelFrame(window5,text='cashbook',bg='light blue')
    wrapper2=tkinter.LabelFrame(window5,text='update',bg='light blue')
    
    wrapper1.pack(fill='both',expand='yes',padx='20',pady='0')
    wrapper2.pack(fill='both',expand='yes',padx='20',pady='10')

    trv=Treeview(wrapper1,columns=(1,2,3,4,5,6),show='headings',height='15')
    trv.pack()
    trv.heading(1,text='firstname')
    trv.heading(2,text='lastname')
    trv.heading(3,text='accountno')
    trv.heading(4,text='email')
    trv.heading(5,text='lasttime update')
    trv.heading(6,text='Closing Balance')

    lbl1=tkinter.Label(wrapper2,text='Search :',font=('Gabriola'),bg='light blue',fg='black')
    lbl1.grid(row=1,column=0,padx='5',pady='3')
    ent1=tkinter.Entry(wrapper2,bd=4,textvariable=search)
    ent1.grid(row=1,column=1,padx='5',pady='3')

    btnsr=tkinter.Button(wrapper2,text="SEARCH",activebackground='green',command=search1)
    btnsr.grid(row=1,column=2)
    btncl=tkinter.Button(wrapper2,text="CLEAR",activebackground='green',command=clear)

    trv.bind('<Double 1>',getrow)
    
    btncl.grid(row=1,column=4)
    lbl2=tkinter.Label(wrapper2,text='Accountno:',font=('Gabriola'),bg='light blue',fg='black')
    lbl2.grid(row=4,column=0,padx='5',pady='3')
    ent2=tkinter.Entry(wrapper2,bd=4,textvariable=tracc)
    ent2.grid(row=4,column=1,padx='20',pady='5')

    lbl3=tkinter.Label(wrapper2,text='Name :',font=('Gabriola'),bg='light blue',fg='black')
    lbl3.grid(row=5,column=0)
    ent3=tkinter.Entry(wrapper2,bd=4,textvariable=trname)
    ent3.grid(row=5,column=1,padx='20',pady='5')

    lbl5=tkinter.Label(wrapper2,text='email :',font=('Gabriola'),bg='light blue',fg='black')
    lbl5.grid(row=6,column=0)
    ent5=tkinter.Entry(wrapper2,bd=4,textvariable=tremail)
    ent5.grid(row=6,column=1,padx='20',pady='5')

    
    lbl5=tkinter.Label(wrapper2,text='lasttime update :',font=('Gabriola'),bg='light blue',fg='black')
    lbl5.grid(row=7,column=0)
    ent5=tkinter.Entry(wrapper2,bd=4,textvariable=trtime)
    ent5.grid(row=7,column=1,padx='20',pady='5')
    
    
    lbl4=tkinter.Label(wrapper2,text='balance :',font=('Gabriola'),bg='light blue',fg='black')
    lbl4.grid(row=8,column=0)
    ent4=tkinter.Entry(wrapper2,bd=4,textvariable=trbalance)
    ent4.grid(row=8,column=1,padx='20',pady='5')
    lbl5=tkinter.Label(wrapper2,text='Withdrawl :',font=('Gabriola'),bg='light blue',fg='black')
    lbl5.grid(row=6,column=4)
    ent5=tkinter.Entry(wrapper2,bd=4,textvariable=trwithdrawl)
    ent5.grid(row=6,column=5,padx='20',pady='5')
   
    lbl5=tkinter.Label(wrapper2,text='Deposit :',font=('Gabriola'),bg='light blue',fg='black')
    lbl5.grid(row=7,column=4,padx='5',pady='3')
    ent5=tkinter.Entry(wrapper2,bd=4,textvariable=trdeposit)
    ent5.grid(row=7,column=5,padx='5',pady='3')

    lbl6=tkinter.Label(wrapper2,text='final balance :',font=('Gabriola'),bg='light blue',fg='black')
    lbl6.grid(row=8,column=4,padx='5',pady='3')
    ent6=tkinter.Entry(wrapper2,bd=4,textvariable=trfinal)
    ent6.grid(row=8,column=5,padx='5',pady='3')

    btnup=tkinter.Button(wrapper2,text="DELETE",activebackground='red',command=delete)
    btnup.grid(row=9,column=1)


    btnup=tkinter.Button(wrapper2,text="UPDATE",activebackground='green',command=updatenew)
    btnup.place(x=570,y=150,height=25,width=150)

    btnex=tkinter.Button(wrapper2,text="EXIT",activebackground='red',command=window2new2)
    btnex.place(x=750,y=150,height=25,width=150)

    query='SELECT fristname,lastname,accountno,email,accountcreated,closingbalance from account'
    mycur.execute(query)
    rows=mycur.fetchall()
    update(rows)
    
#*************************************************************ACCOUNT DETAILS WORK END*****************************************    




