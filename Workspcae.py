from tkinter import *
# import tkinter as tk
import tkinter.messagebox
# import  mysql.connector
from  tkinter import  ttk

#establishing connection
# conn = mysql.connector.connect(
#    user='root', password='', host='localhost', database='cs_project')


root = Tk()

root.title("โรงแรมผีสิง เข้าพักมีนางรำ Login")

root.geometry("480x480")

def chkLogin():
    var1 = txt.get()
    var2 = txt1.get()
    if (var1 == 'admin') and (var2 == '123'):
        # print(var1)
        openWindow()
    else:
        tkinter.messagebox.showinfo(
            'ระบบร้านสะดวกซื้อ', 'ไม่สามารถเข้าสู่ระบบได้')


def exitProgram():
    confirm = tkinter.messagebox.askquestion(
        "ยืนยัน", "คุณต้องการปิดโปรแกรมหรือไม่")
    if confirm == "yes":
        root.destroy()

frame1 = Frame(root, highlightbackground="blue", highlightthickness=2)
frame1.pack(padx=20, pady=20)

myLabel1 = Label(frame1 , text="โรงแรมผีสิง เข้าพักมีนางรำ", fg="black",height=3, width=52, font=("4711_AtNoon_Regular", 28)).pack()

myLabel2 = Label(frame1, text=" Username :", fg="black", font=("4711_AtNoon_Regular", 28),).pack()

txt = StringVar()
T1 = Entry(frame1, textvariable=txt, font=("4711_AtNoon_Regular", 16)).pack()
# การ Label สำหรับ Password
lbUN = Label(frame1, text="Password :", fg="black",
             font=("4711_AtNoon_Regular", 28), ).pack()

txt1 = StringVar()
T2 = Entry(frame1, show='*', textvariable=txt1, font=("4711_AtNoon_Regular", 16)).pack()

btn1 = Button(frame1, text="Login", fg="black", font=("4711_AtNoon_Regular", 20), bg="lightgrey",
              width="10", height="1", command=chkLogin).pack()


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

    lbTitle = Label(mainWindow, text="บันทึกรายการ", fg="black",height=2, width=15, font=("4711_AtNoon_Regular", 24),bg="lightBlue").grid(row=0, column=0, sticky='NSEW', columnspan=1)

    lbcon_name = Label(mainWindow, text="ชื่อลูกค้า :", fg="black", font=("4711_AtNoon_Regular", 24), bg="lightgrey").grid(row=1, column=0, sticky='NSEW')
    # ----------------
    txt1 = StringVar()
    txtlbcon_name = Entry(mainWindow, textvariable=txt1,font=("4711_AtNoon_Regular", 24)).grid(row=1, column=1, sticky='NSEW')

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


    typeroom=IntVar()
    priceroom=IntVar()
    priceroom1=IntVar()


    Label(mainWindow, text="ประเภทห้อง : ",  fg="black", font=("4711_AtNoon_Regular", 24), bg="lightgrey").grid(row=3, column=0, sticky='NSEW')
    # gender radiobutton
    Radiobutton(mainWindow,text="Standard",variable=typeroom,value=1).place(x=250,y=149)
    Radiobutton(mainWindow, text="Duluxe", variable=typeroom, value=2).place(x=350, y=149)
    Radiobutton(mainWindow, text="Suite", variable=typeroom, value=3).place(x=450, y=149)

    Label(mainWindow, text="ชนิดห้องพัก" , fg="black", font=("4711_AtNoon_Regular", 24),bg="lightgrey" ).grid(row=3, column=2, sticky='NSEW')
    dropdown = ttk.Combobox(mainWindow, width=15, font=("4711_AtNoon_Regular", 15) )
    dropdown['values'] = (' Single Bed',' Twin',' Ocean view',' Mountain View')
    dropdown.current()
    dropdown.place(x=750,y=147)

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

    lbchack_type= Label(mainWindow, text="จำนวนผู้เข้าพัก ผู้ใหญ่:", fg="black", font=("4711_AtNoon_Regular", 24),bg="lightgrey").grid(row=6, column=0, sticky='NSEW')
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
    dropdown1 = ttk.Combobox(mainWindow, width=15, font=("4711_AtNoon_Regular", 15) )
    dropdown1['values'] = (' 1500',' 3000',' 4500',' 7500')
    dropdown1.current()
    dropdown1.place(x=245,y=343)

    Label(mainWindow, text="การชำระเงิน : ",  fg="black", font=("4711_AtNoon_Regular", 24), bg="lightgrey").grid(row=9, column=0, sticky='NSEW')
    # gender radiobutton
    Radiobutton(mainWindow,text="ชำระแล้ว",variable=priceroom,value=1).place(x=245,y=380)
    Radiobutton(mainWindow, text="ยังไม่ชำระ", variable=priceroom, value=2).place(x=350, y=380)

    Label(mainWindow, text="เงินมัดจำ : ",  fg="black", font=("4711_AtNoon_Regular", 24), bg="lightgrey").grid(row=10, column=0, sticky='NSEW')
    # gender radiobutton
    Radiobutton(mainWindow,text="ชำระแล้ว",variable=priceroom1,value=1).place(x=247,y=413)
    Radiobutton(mainWindow, text="ยังไม่ชำระ", variable=priceroom1, value=2).place(x=350, y=413)

    lbmore= Label(mainWindow, text="หมายเหตุ:", fg="black", font=("4711_AtNoon_Regular", 24),bg="lightgrey").grid(row=11, column=0, sticky='NSEW')
# -------------------------
    txt12 = StringVar()
    txtmore = Entry(mainWindow, textvariable=txt12, font=("4711_AtNoon_Regular", 24)).grid(row=11, column=1, sticky='NSEW')
# ปุ่มกด
    btnADD = Button(mainWindow, text="Save", fg="black", font=("Verdana", 12),
                    bg="lightgrey", width="20", height="3", command=chkLogin).grid(row=12, column=0, sticky='NSEW')
    btnDEL = Button(mainWindow, text="Add Room", fg="black", font=("Verdana", 12),
                    bg="lightgrey", width="20", height="3", command=openWindow).grid(row=12, column=1, sticky='NSEW')
    btnEDIT = Button(mainWindow, text="Edit", fg="black", font=("Verdana", 12),
                     bg="lightgrey", width="20", height="3", command=exitProgram).grid(row=12, column=2, sticky='NSEW')
    btnCLOSE = Button(mainWindow, text="Close", fg="black", font=("Verdana", 12),
                      bg="lightgrey", width="20", height="3", command=exitProgram).grid(row=12, column=3, sticky='NSEW')
    





















root.mainloop()