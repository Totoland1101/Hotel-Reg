from tkinter import *
from  tkinter import  ttk
# importing connection
import  mysql.connector
#establishing connection
conn = mysql.connector.connect(
   user='root', password='1234567890', host='localhost', database='test03')
"""
here in my case there is no password so password='' is blank
root is username
localhost is server or host name 
you can also use 127.0.0.1 in place of local host
pythondata is the name of Database
"""
#defining register function
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
           "VALUES (%s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s  )"
       )
       if typeroom1==1:
        data = (name, phnum, nationality, Address, "Standard", Typeroom1 , checkroom , checkin , checkout ,checktype ,checktypech , roomnum ,reservation ,price0 , price1 ,price2 ,More)
       
       else:
        data = (name, phnum, nationality, Address, "Duluxe", Typeroom1 , checkroom , checkin , checkout , checktype ,checktypech , roomnum ,reservation ,price0 , price1 ,price2 ,More)
       
       if price1==1:
        data = (name, phnum, nationality, Address, typeroom1, Typeroom1 , checkroom , checkin , checkout , checktype ,checktypech , roomnum ,reservation ,price0 , "ชำระแล้ว" ,price2 ,More)
  
       else:
        data = (name, phnum, nationality, Address, typeroom1, Typeroom1 , checkroom , checkin , checkout , checktype ,checktypech , roomnum ,reservation ,price0 , "ยังไม่ขำระ"  ,price2 ,More)    
        

       if price2==1:
        data = (name, phnum, nationality, Address, typeroom1, Typeroom1 , checkroom , checkin , checkout , checktype ,checktypech , roomnum ,reservation ,price0 , price1 ,"ชำระแล้ว"  ,More)
       
       else:
        data = (name, phnum, nationality, Address, typeroom1, Typeroom1 , checkroom , checkin , checkout , checktype ,checktypech , roomnum ,reservation ,price0 , price1 , "ยังไม่ขำระ"  ,More)   
        
       try:
           #executing the sql command
           cursor.execute(insert_stmt,data)
           #commit changes in database
           conn.commit()
       except:
           conn.rollback()
       message.set("Stored successfully")

#defining Registrationform function
def openWindow():
    mainWindow = Tk()
    mainWindow.title("โรงแรมผีสิง เข้าพักมีนางรำ")
    mainWindow.geometry("1080x800")

    # # สร้าง menu
    # myMenu = Menu()
    # mainWindow.config(menu=myMenu)
    # # เพิ่มเมนู หลัก
    # myMenu.add_cascade(label="File")
    # myMenu.add_cascade(label="Edit")
    # myMenu.add_cascade(label="View")


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
    global message
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

    Label(mainWindow, text="",textvariable=message).place(x=245,y=726)

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
    mainWindow.mainloop()

openWindow()