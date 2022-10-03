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