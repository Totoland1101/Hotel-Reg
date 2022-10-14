from tkinter import *
from  tkinter import  ttk
import tkinter as tk
import tkinter.messagebox
# importing connection
import  mysql.connector
#establishing connection
conn = mysql.connector.connect(
   user='root', password='1234567890', host='localhost', database='test02')

def register():
    #getting form data
    name=txt.get()
    phnum=txt2.get()
    nationality=txt3.get()
    Address=txt4.get()
    typeroom1=typeroom.get()
    Typeroom1=Typeroom.get()
    checkroom=txt5.get()
    checkin=txt6.get()
    checkout=txt7.get()
    checktype=txt8.get()
    checktypech=txt9.get()
    roomnum=txt10.get()
    reservation=txt11.get()
    price0=price.get()
    price1=priceroom.get()
    price2=priceroom1.get()
    More=txt12.get()

    #applying empty validation
    if name=='' or phnum==''or nationality=='' or Address==''or typeroom1==''or Typeroom1=='' or checkroom=='' or checkin==''or checkout=='' or checktype==''or checktypech==''or roomnum==''or reservation==''or price0==''or price1==''or price2==''or More=='' :
        message.set("fill the empty field!!!")
    else:
       # Creating a cursor object using the cursor() method
       cursor = conn.cursor()
       # Preparing SQL query to INSERT a record into the database.
       insert_stmt = (
           "INSERT INTO REG(Name, Phone, Nationality, Address, TyRoom, Tyroom1 , Uint , CheckIn , CheckOut , Adult ,Children , RoomNum ,ReservationNum ,PriceST , PriceST1 ,PriceST2 ,ADDON )"
           "VALUES (%s, %s,%s,%s,%s, %s,%s, %s, %s, %s, %s, %s , %s, %s, %s, %s, %s ,%s )"
       )
       if typeroom1==1:
        data = (name, phnum, nationality, Address, "Standard", Typeroom1 , checkroom , checkin , checkout , Adult ,checktype ,checktypech , roomnum ,reservation ,price0 , price1 ,price2 ,More)
       
       else:
        data = (name, phnum, nationality, Address, "Duluxe", Typeroom1 , checkroom , checkin , checkout , Adult ,checktype ,checktypech , roomnum ,reservation ,price0 , price1 ,price2 ,More)
       
       if price1==1:
        data = (name, phnum, nationality, Address, typeroom1, Typeroom1 , checkroom , checkin , checkout , Adult ,checktype ,checktypech , roomnum ,reservation ,price0 , "ยังไม่ขำระ" ,price2 ,More)
  
       else:
        data = (name, phnum, nationality, Address, typeroom1, Typeroom1 , checkroom , checkin , checkout , Adult ,checktype ,checktypech , roomnum ,reservation ,price0 , "ชำระแล้ว"  ,price2 ,More)    
        

       if price2==1:
        data = (name, phnum, nationality, Address, typeroom1, Typeroom1 , checkroom , checkin , checkout , Adult ,checktype ,checktypech , roomnum ,reservation ,price0 , price1 ,"ยังไม่ขำระ"  ,More)
       
       else:
        data = (name, phnum, nationality, Address, typeroom1, Typeroom1 , checkroom , checkin , checkout , Adult ,checktype ,checktypech , roomnum ,reservation ,price0 , price1 , "ชำระแล้ว"  ,More)   
        
       try:
           #executing the sql command
           cursor.execute(insert_stmt,data)
           #commit changes in database
           conn.commit()
       except:
           conn.rollback()
       message.set("Stored successfully")

def Login():
    global root
    root = Tk()
    root.title("โรงแรมผีสิง เข้าพักมีนางรำ Login")
    root.geometry("480x480")

    TxT = StringVar()
    txt1 = StringVar()
    var1 = TxT.get()
    var2 = txt1.get()

    if (var1 == '') and (var2 == ''):
        # print(var1)
        mainbooking()
    else:
        tkinter.messagebox.showinfo(
            'โรงแรมผีสิง เข้าพักมีนางรำ Login', 'ไม่สามารถเข้าสู่ระบบได้')

    frame1 = Frame(root, highlightbackground="blue", highlightthickness=2)
    frame1.pack(padx=20, pady=20)

    myLabel1 = Label(frame1 , text="โรงแรมผีสิง เข้าพักมีนางรำ", fg="black",height=3, width=52, font=("4711_AtNoon_Regular", 28)).pack()

    myLabel2 = Label(frame1, text=" Username :", fg="black", font=("4711_AtNoon_Regular", 28),).pack()

    T1 = Entry(frame1, textvariable=TxT, font=("4711_AtNoon_Regular", 16)).pack()
    # การ Label สำหรับ Password
    lbUN = Label(frame1, text="Password :", fg="black",
             font=("4711_AtNoon_Regular", 28), ).pack()

   
    T2 = Entry(frame1, show='*', textvariable=txt1, font=("4711_AtNoon_Regular", 16)).pack()

    btn1 = Button(frame1, text="Login", fg="black", font=("4711_AtNoon_Regular", 20), bg="lightgrey",
              width="10", height="1",).pack()
    root.mainloop()
Login()

def mainbooking():
    global mainBooking
    mainBooking = Tk()
    mainBooking.title("โรงแรมผีสิง เข้าพักมีนางรำ")
    mainBooking.geometry("500x500")
  # สร้าง menu
    myMenu = Menu()
    # mainBooking.config(menu=myMenu)
    # เพิ่มเมนู หลัก
    # myMenu.add_cascade(label="File")
    # myMenu.add_cascade(label="Edit")
    # myMenu.add_cascade(label="View")

    Standard=IntVar()
    Duluxe=IntVar()
    Suite=IntVar()

    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar() 
    var7 = IntVar() 
    var8 = IntVar()
    var9 = IntVar()
    var10 = IntVar()
    var11 = IntVar()
    var12 = IntVar()
    
    

    lbcon_name = Label(mainBooking, text="Room Type :", fg="black", font=("4711_AtNoon_Regular", 24), bg="lightgrey").grid(row=0, column=0, sticky='NSEW')
    
    
    Checkbutton(mainBooking, text="1", variable=var1).grid(row=0, column=1, sticky= 'W' )
    Checkbutton(mainBooking, text="2", variable=var2).grid(row=0, column=2, sticky= 'W' )   
    Checkbutton(mainBooking, text="3", variable=var3).grid(row=0, column=3, sticky= 'W' )
    Checkbutton(mainBooking, text="4", variable=var4).grid(row=0, column=4, sticky= 'W' ) 
    Checkbutton(mainBooking, text="5", variable=var5).grid(row=1, column=1, sticky= 'W' )
    Checkbutton(mainBooking, text="6", variable=var6).grid(row=1, column=2, sticky= 'W' ) 
    Checkbutton(mainBooking, text="7", variable=var7).grid(row=1, column=3, sticky= 'W' )
    Checkbutton(mainBooking, text="8", variable=var8).grid(row=1, column=4, sticky= 'W' ) 
    Checkbutton(mainBooking, text="9", variable=var9).grid(row=2, column=1, sticky= 'W' )
    Checkbutton(mainBooking, text="10", variable=var10).grid(row=2, column=2, sticky= 'W' )
    Checkbutton(mainBooking, text="11", variable=var11).grid(row=2, column=3, sticky= 'W' )
    Checkbutton(mainBooking, text="12", variable=var12).grid(row=2, column=4, sticky= 'W' )


    Label(mainBooking, text="Standard",   font=("4711_AtNoon_Regular", 24), bg="lightgrey").grid(row=3, column=0, sticky='NSEW')
    # gender radiobutton
    Radiobutton(mainBooking,text="Standard",variable=Standard,value=1).place(x=125,y=110)
    Radiobutton(mainBooking, text="Duluxe", variable=Standard, value=2).place(x=215, y=110)
   
    Label(mainBooking, text="Duluxe",font=("4711_AtNoon_Regular", 24), bg="lightgrey").grid(row=6, column=0, sticky='NSEW')
    # gender radiobutton
    Radiobutton(mainBooking,text="Single Bed",variable=Duluxe,value=1).place(x=125,y=155)
    Radiobutton(mainBooking, text="Twin", variable=Duluxe, value=2).place(x=215, y=155)

    Label(mainBooking, text="Suite",   font=("4711_AtNoon_Regular", 24), bg="lightgrey").grid(row=9, column=0, sticky='NSEW')
    # gender radiobutton
    Radiobutton(mainBooking,text="Ocean View",variable=Suite,value=1).place(x=125,y=202)
    Radiobutton(mainBooking, text="Mountain view", variable=Suite, value=2).place(x=215, y=202)

   
    


    btnADD = Button(mainBooking, text="NEXT", fg="black", font=("4711_AtNoon_Regular", 12),
                    bg="lightgrey", width="20", height="3", ).grid(row=10, column=0, sticky='NSEW')
    
    mainBooking.mainloop()
mainBooking()



