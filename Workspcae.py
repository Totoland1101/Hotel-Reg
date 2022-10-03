from tkinter import *
import tkinter.messagebox
import  mysql.connector
#establishing connection
# conn = mysql.connector.connect(
#    user='root', password='', host='localhost', database='cs_project')


root = Tk()

root.title("โรงแรมผีสิง เข้าพักมีนางรำ Login")

root.geometry("480x480")

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

def openWindow():
    # หน้าจอที่ 2
    mainWindow = Tk()
    mainWindow.title("โรงแรมผีสิง เข้าพักมีนางรำ")
    mainWindow.geometry("500x400")

    # สร้าง menu
    myMenu = Menu()
    mainWindow.config(menu=myMenu)
    # เพิ่มเมนู หลัก
    myMenu.add_cascade(label="File")
    myMenu.add_cascade(label="Edit")
    myMenu.add_cascade(label="View")

    lbTitle = Label(mainWindow, text="ข้อมูลสินค้า", fg="black",
                    height=3, width=32, font=("Courier", 20),
                    bg="lightBlue").grid(row=0, column=0, sticky='NSEW', columnspan=2)
    lbProID = Label(mainWindow, text="รหัสสินค้า :", fg="green", font=("Courier", 20),
                    bg="lightgrey").grid(row=1, column=0, sticky='NSEW')
    lbProName = Label(mainWindow, text="ชื่อสินค้า :", fg="green", font=("Courier", 20),
                      bg="lightgrey").grid(row=2, column=0, sticky='NSEW')
    lbProPrice = Label(mainWindow, text="ราคาสินค้า :", fg="green", font=("Courier", 20),
                       bg="lightgrey").grid(row=3, column=0, sticky='NSEW')
    lbProQTY = Label(mainWindow, text="จำนวนสินค้า :", fg="green", font=("Courier", 20),
                     bg="lightgrey").grid(row=4, column=0, sticky='NSEW')

def chkLogin():
    var1 = txt.get()
    var2 = txt1.get()
    if (var1 == 'admin') and (var2 == '123'):
        # print(var1)
        openWindow()
    else:
        tkinter.messagebox.showinfo(
            'ระบบร้านสะดวกซื้อ', 'ไม่สามารถเข้าสู่ระบบได้')


# def exitProgram():
#     confirm = tkinter.messagebox.askquestion(
#         "ยืนยัน", "คุณต้องการปิดโปรแกรมหรือไม่")
#     if confirm == "yes":
#         root.destroy()


btn1 = Button(frame1, text="Login", fg="black", font=("4711_AtNoon_Regular", 20), bg="lightgrey",
              width="10", height="1", command=chkLogin).pack(anchor=CENTER)











root.mainloop()