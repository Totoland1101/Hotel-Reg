from tkinter import *
import tkinter as tk
import tkinter.messagebox
import mysql.connector
from tkinter import  ttk

#establishing connection
conn = mysql.connector.connect(
user='root', password='1234567890', host='localhost', database='test02')


root = Tk()

root.title("โรงแรมผีสิง เข้าพักมีนางรำ Login")

root.geometry("480x480")

def chkLogin():
    var1 = TxT.get()
    var2 = txt1.get()
    if (var1 == '') and (var2 == ''):
        # print(var1)
        booking()()
    else:
        tkinter.messagebox.showinfo(
            'โรงแรมผีสิง เข้าพักมีนางรำ Login', 'ไม่สามารถเข้าสู่ระบบได้')


def exitProgram():
    confirm = tkinter.messagebox.askquestion(
        "ยืนยัน", "Do you Want exit")
    if confirm == "yes":
        root.destroy()

frame1 = Frame(root, highlightbackground="blue", highlightthickness=2)
frame1.pack(padx=20, pady=20)

myLabel1 = Label(frame1 , text="โรงแรมผีสิง เข้าพักมีนางรำ", fg="black",height=3, width=52, font=("4711_AtNoon_Regular", 28)).pack()

myLabel2 = Label(frame1, text=" Username :", fg="black", font=("4711_AtNoon_Regular", 28),).pack()

TxT = StringVar()
T1 = Entry(frame1, textvariable=TxT, font=("4711_AtNoon_Regular", 16)).pack()
# การ Label สำหรับ Password
lbUN = Label(frame1, text="Password :", fg="black",
             font=("4711_AtNoon_Regular", 28), ).pack()

txt1 = StringVar()
T2 = Entry(frame1, show='*', textvariable=txt1, font=("4711_AtNoon_Regular", 16)).pack()

btn1 = Button(frame1, text="Login", fg="black", font=("4711_AtNoon_Regular", 20), bg="lightgrey",
              width="10", height="1", command=chkLogin).pack()

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


def booking():
    mainBooking = Tk()
    mainBooking.title("โรงแรมผีสิง เข้าพักมีนางรำ")
    mainBooking.geometry("500x500")

  # สร้าง menu
    myMenu = Menu()
    mainBooking.config(menu=myMenu)
    # เพิ่มเมนู หลัก
    myMenu.add_cascade(label="File")
    myMenu.add_cascade(label="Edit")
    myMenu.add_cascade(label="View")

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
                    bg="lightgrey", width="20", height="3", command=openWindow).grid(row=10, column=0, sticky='NSEW')
    
    mainloop()

def openWindow():
    mainWindow = Tk()
    mainWindow.title("โรงแรมผีสิง เข้าพักมีนางรำ")
    mainWindow.geometry("1080x800")

    # สร้าง menu
    myMenu = Menu()
    mainWindow.config(menu=myMenu)
    # เพิ่มเมนู หลัก
    myMenu.add_cascade(label="File")
    myMenu.add_cascade(label="Edit")
    myMenu.add_cascade(label="View")


    global txt
    global txt2
    global txt3
    global txt4
    global txt5
    global txt6
    global txt7
    global txt8
    global txt9
    global txt10
    global txt11
    global txt12
    global  message;
    
    global typeroom
    global Typeroom
    global price
    global priceroom
    global priceroom1  


    typeroom=IntVar()
    Typeroom=StringVar()
    price= StringVar()
    priceroom=IntVar()
    priceroom1=IntVar()
    message=StringVar()
    
  


    lbTitle = Label(mainWindow, text="บันทึกรายการ", fg="black",height=2, width=15, font=("4711_AtNoon_Regular", 24),bg="lightBlue").grid(row=0, column=0, sticky='NSEW', columnspan=1)

    lbcon_name = Label(mainWindow, text="ชื่อลูกค้า :", fg="black", font=("4711_AtNoon_Regular", 24), bg="lightgrey").grid(row=1, column=0, sticky='NSEW')
    # ----------------
    txt = StringVar()
    txtlbcon_name = Entry(mainWindow, textvariable=txt,font=("4711_AtNoon_Regular", 24)).grid(row=1, column=1, sticky='NSEW')

    lbnum = Label(mainWindow, text="เบอร์โทรศัพท์ :", fg="black", font=("4711_AtNoon_Regular", 24), bg="lightgrey").grid(row=1, column=2, sticky='NSEW')
    # -----------------
    txt2 = StringVar()
    txtnum = Entry(mainWindow, textvariable=txt2, font=("4711_AtNoon_Regular", 24)).grid(row=1, column=3, sticky='NSEW')

    lbNAT = Label(mainWindow, text="สัญชาติ :", fg="black", font=("4711_AtNoon_Regular", 24),bg="lightgrey").grid(row=2, column=0, sticky='NSEW')
    # ----------------------
    txt3 = StringVar()
    txtNAT = Entry(mainWindow, textvariable=txt3, font=("4711_AtNoon_Regular", 24)).grid(row=2, column=1, sticky='NSEW')

    lbADD= Label(mainWindow, text="ที่อยู่ :", fg="black", font=("4711_AtNoon_Regular", 24),bg="lightgrey").grid(row=2, column=2, sticky='NSEW')
    # -------------------------
    txt4 = StringVar()
    txtadd = Entry(mainWindow, textvariable=txt4, font=("4711_AtNoon_Regular", 24)).grid(row=2, column=3, sticky='NSEW')


    Label(mainWindow, text="ประเภทห้อง : ",  fg="black", font=("4711_AtNoon_Regular", 24), bg="lightgrey").grid(row=3, column=0, sticky='NSEW')
    # gender radiobutton
    Radiobutton(mainWindow,text="Standard",variable=typeroom,value=1).place(x=193,y=193)
    Radiobutton(mainWindow, text="Duluxe", variable=typeroom, value=2).place(x=283, y=193)
    Radiobutton(mainWindow, text="Suite", variable=typeroom, value=3).place(x=363, y=193)

    Label(mainWindow, text="ชนิดห้องพัก" , fg="black", font=("4711_AtNoon_Regular", 24),bg="lightgrey" ).grid(row=3, column=2, sticky='NSEW')
    dropdown = ttk.Combobox(mainWindow, width=15, font=("4711_AtNoon_Regular", 15) ,textvariable=Typeroom )
    dropdown['values'] = (' Single Bed',' Twin',' Ocean view',' Mountain View')
    dropdown.current()
    dropdown.place(x=605,y=190)

    lbchack_room= Label(mainWindow, text="จำนวนห้อง:", fg="black", font=("4711_AtNoon_Regular", 24),bg="lightgrey").grid(row=4, column=0, sticky='NSEW')  
    # -------------------------
    txt5 = StringVar()
    txtcheck_room = Entry(mainWindow, textvariable=txt5, font=("4711_AtNoon_Regular", 24)).grid(row=4, column=1, sticky='NSEW')

    lbchack_in= Label(mainWindow, text="เข้าพักตั้งแต่วันที่ :", fg="black", font=("4711_AtNoon_Regular", 24),bg="lightgrey").grid(row=4, column=2, sticky='NSEW')
    # -------------------------
    txt6 = StringVar()
    txtcheck_in = Entry(mainWindow, textvariable=txt6, font=("4711_AtNoon_Regular", 24)).grid(row=4, column=3, sticky='NSEW')

    lbchack_out= Label(mainWindow, text="ถึงวันที่ :", fg="black", font=("4711_AtNoon_Regular", 24),bg="lightgrey").grid(row=5, column=0, sticky='NSEW')
    # -------------------------
    txt7 = StringVar()
    txtcheck_out = Entry(mainWindow, textvariable=txt7, font=("4711_AtNoon_Regular", 24)).grid(row=5, column=1, sticky='NSEW')

    lbcheck_type= Label(mainWindow, text="จำนวนผู้เข้าพัก ผู้ใหญ่:", fg="black", font=("4711_AtNoon_Regular", 24),bg="lightgrey").grid(row=6, column=0, sticky='NSEW')
    # -------------------------
    txt8 = StringVar()
    txtcheck_type = Entry(mainWindow, textvariable=txt8, font=("4711_AtNoon_Regular", 24)).grid(row=6, column=1, sticky='NSEW')

    lbchack_ch= Label(mainWindow, text="เด็ก:", fg="black", font=("4711_AtNoon_Regular", 24),bg="lightgrey").grid(row=6, column=2, sticky='NSEW')
    # -------------------------
    txt9 = StringVar()
    txtcheck_ch = Entry(mainWindow, textvariable=txt9, font=("4711_AtNoon_Regular", 24)).grid(row=6, column=3, sticky='NSEW')

    lbchack_room_num= Label(mainWindow, text="หมายเลขห้อง:", fg="black", font=("4711_AtNoon_Regular", 24),bg="lightgrey").grid(row=7, column=0, sticky='NSEW')
    # -------------------------
    txt10 = StringVar()
    txtcheck_room_num = Entry(mainWindow, textvariable=txt10, font=("4711_AtNoon_Regular", 24)).grid(row=7, column=1, sticky='NSEW')

    lbchack_re= Label(mainWindow, text="รหัสผู้จอง:", fg="black", font=("4711_AtNoon_Regular", 24),bg="lightgrey").grid(row=7, column=2, sticky='NSEW')
    # -------------------------
    txt11 = StringVar()
    txtcheck_re = Entry(mainWindow, textvariable=txt11, font=("4711_AtNoon_Regular", 24)).grid(row=7, column=3, sticky='NSEW')

    Label(mainWindow, text="ราคาห้องพัก" , fg="black", font=("4711_AtNoon_Regular", 24),bg="lightgrey" ).grid(row=8, column=0, sticky='NSEW')
    dropdown1 = ttk.Combobox(mainWindow, width=15, font=("4711_AtNoon_Regular", 15) ,textvariable=price )
    dropdown1['values'] = (' 1500',' 3000',' 4500',' 7500')
    dropdown1.current()
    dropdown1.place(x=245,y=426)

    Label(mainWindow, text="การชำระเงิน : ",  fg="black", font=("4711_AtNoon_Regular", 24), bg="lightgrey").grid(row=9, column=0, sticky='NSEW')
    # gender radiobutton
    Radiobutton(mainWindow,text="ชำระแล้ว",variable=priceroom,value=1).place(x=185,y=475)
    Radiobutton(mainWindow, text="ยังไม่ชำระ", variable=priceroom, value=2).place(x=283, y=475)

    Label(mainWindow, text="เงินมัดจำ : ",  fg="black", font=("4711_AtNoon_Regular", 24), bg="lightgrey").grid(row=10, column=0, sticky='NSEW')
    # gender radiobutton
    Radiobutton(mainWindow,text="ชำระแล้ว",variable=priceroom1,value=1).place(x=185,y=522)
    Radiobutton(mainWindow, text="ยังไม่ชำระ", variable=priceroom1, value=2).place(x=283, y=522)

    lbmore= Label(mainWindow, text="หมายเหตุ:", fg="black", font=("4711_AtNoon_Regular", 24),bg="lightgrey").grid(row=11, column=0, sticky='NSEW')
# -------------------------
    txt12 = StringVar()
    txtmore = Entry(mainWindow, textvariable=txt12, font=("4711_AtNoon_Regular", 24)).grid(row=11, column=1, sticky='NSEW')
# ปุ่มกด
    btnADD = Button(mainWindow, text="Save", fg="black", font=("4711_AtNoon_Regular", 18),
                    bg="lightgrey", width="20", height="3", command=register).grid(row=12, column=0, sticky='NSEW')
    btnDEL = Button(mainWindow, text="Add Room", fg="black", font=("4711_AtNoon_Regular", 18),
                    bg="lightgrey", width="20", height="3", command=openWindow).grid(row=12, column=1, sticky='NSEW')
    btnEDIT = Button(mainWindow, text="Edit", fg="black", font=("4711_AtNoon_Regular", 18),
                     bg="lightgrey", width="20", height="3", command=exitProgram).grid(row=12, column=2, sticky='NSEW')
    btnCLOSE = Button(mainWindow, text="Close", fg="black", font=("4711_AtNoon_Regular", 18),
                      bg="lightgrey", width="20", height="3", command=exitProgram).grid(row=12, column=3, sticky='NSEW')
    

root.mainloop()