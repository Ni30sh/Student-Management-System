from tkinter import *
from tkinter import Toplevel, messagebox
import random
import time
from tkinter.ttk import Treeview
from tkinter import ttk
import mysql.connector

# #################################################ADDMISSION ##################################
def student_admission():
    def submit_details():
        global conn, cur
        account_val = ID.get()
        name_val = NAME.get()
        aadhar_val = AADHAR.get()
        dob_val = DOB.get()
        address_val = ADDRESS.get()
        contact_val = MOBILE.get()
        email_val = EMAIL.get()
        gender_val = GENDER.get()
        date = time.strftime("%d-%m-%Y")
        strn = "USE studentpanel"
        cur.execute(strn)
        strn = "SELECT * FROM INFORMATION  WHERE ID = %s"
        cur.execute(strn, (account_val,))
        existing_data = cur.fetchall()
        if existing_data:
            messagebox.showinfo("Notification", "ID Already Exist")
        else:
            cur = conn.cursor()
            cur.execute("INSERT INTO INFORMATION VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (account_val, name_val, aadhar_val, dob_val, address_val, contact_val, email_val, gender_val,
                         date))
            conn.commit()
            strin = "SELECT * FROM INFORMATION"
            cur.execute(strin)
            xt = cur.fetchall()
            student_details.delete(*student_details.get_children())
            for i in xt:
                student_details.insert("", END, values=i)  # [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]])
            message_box = messagebox.askyesnocancel("Notification", "ADDED SUCCESSFULLY... WANT TO CLEAR THE FORM")
            if message_box == True:
                ID.set("")
                NAME.set("")
                AADHAR.set("")
                DOB.set("")
                ADDRESS.set("")
                MOBILE.set("")
                EMAIL.set("")
                GENDER.set("")

    admission_window = Toplevel()
    admission_window.grab_set()
    admission_window.geometry("420x410+800+130")  # W X H
    admission_window.title("Admission Shell")
    admission_window.resizable(False, False)
    admission_window.config(bg="white")
    suggest_label = Label(admission_window, text="Fill the Details of Student", bg="white",
                          font=("Time in romana", 14, "bold"))
    suggest_label.place(x=20, y=10)
    id_label = Label(admission_window, text="ID :", bg="white", font=("Microsoft YaHei UI Light", 11, "bold"))
    id_label.place(x=20, y=64)
    name_label = Label(admission_window, text="NAME :", bg="white", font=("Microsoft YaHei UI Light", 11, "bold"))
    name_label.place(x=20, y=100)
    aadhar_label = Label(admission_window, text="AADHAR :", bg="white", font=("Microsoft YaHei UI Light", 11, "bold"))
    aadhar_label.place(x=20, y=130)
    mobile_label = Label(admission_window, text="MOBILE :", bg="white", font=("Microsoft YaHei UI Light", 11, "bold"))
    mobile_label.place(x=20, y=160)
    address_label = Label(admission_window, text="ADDRESS :", bg="white",
                          font=("Microsoft YaHei UI Light", 11, "bold"))
    address_label.place(x=20, y=190)
    dob_label = Label(admission_window, text="D.O.B :", bg="white", font=("Microsoft YaHei UI Light", 11, "bold"))
    dob_label.place(x=20, y=220)
    email_label = Label(admission_window, text="EMAIL :", bg="white", font=("Microsoft YaHei UI Light", 11, "bold"))
    email_label.place(x=20, y=250)
    gender_label = Label(admission_window, text="GENDER :", bg="white", font=("Microsoft YaHei UI Light", 11, "bold"))
    gender_label.place(x=20, y=280)
    # _______________________________________________________________________________________________________________
    ID = StringVar()
    NAME = StringVar()
    AADHAR = StringVar()
    ADDRESS = StringVar()
    MOBILE = StringVar()
    EMAIL = StringVar()
    DOB = StringVar()
    GENDER = StringVar()
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    id_entry = Entry(admission_window, textvariable=ID, width=25, bg="white", bd=0,
                     font=("Microsoft YaHei UI Light", 13, "bold"))
    id_entry.place(x=150, y=64)
    Frame(admission_window, width=260, height=2, bg="black").place(x=150, y=86)
    name_entry = Entry(admission_window, textvariable=NAME, width=25, bg="white", bd=0,
                       font=("Microsoft YaHei UI Light", 13, "bold"))
    name_entry.place(x=150, y=95)
    Frame(admission_window, width=260, height=2, bg="black").place(x=150, y=119)
    aadhar_entry = Entry(admission_window, textvariable=AADHAR, width=25, bg="white", bd=0,
                         font=("Microsoft YaHei UI Light", 13, "bold"))
    aadhar_entry.place(x=150, y=125)
    Frame(admission_window, width=260, height=2, bg="black").place(x=150, y=149)
    mobile_entry = Entry(admission_window, textvariable=MOBILE, width=25, bg="white", bd=0,
                         font=("Microsoft YaHei UI Light", 13, "bold"))
    mobile_entry.place(x=150, y=155)
    Frame(admission_window, width=260, height=2, bg="black").place(x=150, y=179)
    address_entry = Entry(admission_window, textvariable=ADDRESS, width=25, bg="white", bd=0,
                          font=("Microsoft YaHei UI Light", 13, "bold"))
    address_entry.place(x=150, y=185)
    Frame(admission_window, width=260, height=2, bg="black").place(x=150, y=209)
    dob_entry = Entry(admission_window, textvariable=DOB, width=25, bg="white", bd=0,
                      font=("Microsoft YaHei UI Light", 13, "bold"))
    dob_entry.place(x=150, y=215)
    Frame(admission_window, width=260, height=2, bg="black").place(x=150, y=239)
    email_entry = Entry(admission_window, textvariable=EMAIL, width=25, fg="black", bg="white", bd=0,
                        font=("Microsoft YaHei UI Light", 13, "bold"))
    email_entry.place(x=150, y=245)
    Frame(admission_window, width=260, height=2, bg="black").place(x=150, y=269)
    gender_entry = Entry(admission_window, textvariable=GENDER, width=25, fg="black", bg="white", bd=0,
                         font=("Microsoft YaHei UI Light", 13, "bold"))
    gender_entry.place(x=150, y=280)
    Frame(admission_window, width=260, height=2, bg="black").place(x=150, y=304)
    # ################################################################################################
    submit_btn = Button(admission_window, text="SUBMIT", font=("time in romana", 12, "bold"), activeforeground="black",
                        activebackground="white", bg="blue", command=submit_details, fg="white")
    submit_btn.place(x=120, y=350, width=200)
    admission_window.mainloop()


# ########################################### LABEL OF FEE SUBMITTING #################################################
def fee_submit():
    def submit_fee():
        global conn, cur
        aadhar_number = entry_aadhar.get()
        fee_amount = entry_fee.get()
        strn = "USE studentpanel"
        cur.execute(strn)
        cur = conn.cursor()
        cur.execute("SELECT * FROM submit WHERE aadhar = %s", (aadhar_number,))
        existing_data = cur.fetchall()
        # Check if Aadhar number exists in the database
        cur.execute("SELECT * FROM INFORMATION WHERE aadhar = %s", (aadhar_number,))
        result = cur.fetchone()
        if existing_data:
            messagebox.showinfo("Notification", "Fee Already Submit", parent=fee_window)
        elif result:
            # Aadhar number exists, submit to the 'SUBMIT' table
            cur.execute("INSERT INTO SUBMIT (aadhar, fee) VALUES (%s, %s)", (aadhar_number, fee_amount))
            conn.commit()
            messagebox.showinfo("Notification", "Successfully submitted!", parent=fee_window)
        else:
            # Aadhar number does not exist
            messagebox.showerror("ERROR", "No Student of this Aadhar.", parent=fee_window)
            # cur.close()

    fee_window = Toplevel()
    fee_window.grab_set()
    fee_window.geometry('300x300+700+199')
    fee_window.title("Fee Window")
    # ########################################################## Entry and Command ####################################
    entry_aadhar = StringVar()
    entry_fee = StringVar()
    suggest_label = Label(fee_window, text="Enter Aadhar and Amount", font=("Microsoft YaHei UI Light", 12, "bold"))
    suggest_label.place(x=5, y=10, height=25, width=220)
    aadhar_label = Label(fee_window, text="Aadhar :", font=("Microsoft YaHei UI Light", 11, "bold"))
    aadhar_label.place(x=10, y=60, height=25, width=90)
    aadhar_entry = Entry(fee_window, textvariable=entry_aadhar, bd=0, font=("Microsoft YaHei UI Light", 11, "bold"))
    aadhar_entry.place(x=20, y=85, height=25, width=260)
    Frame(fee_window, width=260, height=2, bg="black").place(x=20, y=108)
    amount_label = Label(fee_window, text="Amount :", font=("Microsoft YaHei UI Light", 11, "bold"))
    amount_label.place(x=10, y=120, height=25, width=90)
    amount_entry = Entry(fee_window, textvariable=entry_fee, bd=0, font=("Microsoft YaHei UI Light", 11, "bold"))
    amount_entry.place(x=20, y=145, height=25, width=260)
    Frame(fee_window, width=260, height=2, bg="black").place(x=20, y=168)
    submit_fee_button = Button(fee_window, text="Submit", bg="blue", fg="white", font=("chiller", 11, "bold"),
                               activebackground="white", activeforeground="black", command=submit_fee)
    submit_fee_button.place(x=100, y=210, height=35, width=100)
    fee_window.mainloop()


##########################################################  search_student    ##########################################
def search_student():
    aadhar_no = StringVar()

    def show_student_details():
        global conn, cur
        aadhar_number = aadhar_no.get()
        strn = "USE studentpanel"
        cur.execute(strn)
        # check if Aadhar is existing in Database
        strn = "SELECT * FROM INFORMATION WHERE AADHAR = %s"
        cur.execute(strn, (aadhar_number,))
        results = cur.fetchall()
        if results:
            student_details.delete(*student_details.get_children())
            for result in results:
                student_details.insert("", END, values=result)
        else:
            messagebox.showinfo("Notification", "No Aadhar Number Exist.", parent=search_window)

    search_window = Toplevel()
    search_window.grab_set()
    search_window.geometry('400x300+700+130')
    search_window.title("Principal Portal")
    suggest_label = Label(search_window, text="Enter The Aadhar Number To Get Student Profile",
                          font=("Time in romana", 11, "bold"))
    suggest_label.place(x=10, y=20, height=20, width=370)
    aadhar_label = Label(search_window, text="Enter Aadhar Number:", font=("Time in romana", 10, "bold"))
    aadhar_label.place(x=47, y=77, height=25, width=180)
    aadhar_entry = Entry(search_window, textvariable=aadhar_no, font=("Time in romana", 15, "bold"), bd=0)
    aadhar_entry.place(x=50, y=120, height=25, width=260)
    Frame(search_window, width=260, height=2, bg="black").place(x=50, y=144)
    show_details_button = Button(search_window, text="Show Details", font=("Time in romana", 10),
                                 command=show_student_details, bg="blue", fg="white")
    show_details_button.place(x=135, y=180, width=150, height=35)
    search_window.mainloop()


# ########################################################## PRINCIPAL ACCESS ##########################################
def principal_access():
    def login():
        entered_id = id_entry.get()
        entered_password = password_entry.get()
        if entered_id == "admin" and entered_password == "password":  # Check if the entered ID and password match the assigned values
            open_principal_portal()
        else:
            messagebox.showerror("Error", "Invalid ID or Password")

    def open_principal_portal():
        aadhar_no = StringVar()

        def show_aadhar_details():
            global conn, cur
            aadhar_number = aadhar_no.get()
            strn = "USE studentpanel"
            cur.execute(strn)
            strn = "SELECT * FROM INFORMATION WHERE AADHAR = %s"
            cur.execute(strn, (aadhar_number,))
            results = cur.fetchall()
            if results:
                student_details.delete(*student_details.get_children())
                for result in results:
                    student_details.insert("", END, values=result)
            else:
                messagebox.showinfo("Notification", "No Admission", parent=principal_window)

        def show_fee_details():
            global conn, cur
            aadhar_number1 = aadhar_no.get()
            strn = "USE studentpanel"
            cur.execute(strn)
            strn = "SELECT * FROM SUBMIT WHERE AADHAR = %s"
            cur.execute(strn, (aadhar_number1,))
            results = cur.fetchall()
            if results:
                fee_details = results[0]
                # for result in results:
                #     fee_details += f"Aadhar : {result[0]}\nFee: {result[1]}\n\n"
                messagebox.showinfo("Fee Details", f"Aadhar: {aadhar_number1}\n\nFee : {fee_details[1]}",
                                    parent=principal_window)
            else:
                messagebox.showinfo("Fee Details ", "No Fee Details found for the given Aadhar number",
                                    parent=principal_window)

        principal_window = Toplevel()
        principal_window.geometry('350x300+700+130')
        principal_window.title("Principal Portal")
        suggest_label1 = Label(principal_window, text="Aadhar No. To Get Student Profile", font=('chiller', 11, 'bold'))
        suggest_label1.place(x=6, y=20, height=25, width=310)
        aadhar_label = Label(principal_window, text="Enter Aadhar Number:", font=('chiller', 10, 'bold'))
        aadhar_label.place(x=12, y=77, height=25, width=180)
        aadhar_entry = Entry(principal_window, textvariable=aadhar_no, bd=0, font=('chiller', 13, 'bold'))
        aadhar_entry.place(x=20, y=110, height=25, width=260)
        Frame(principal_window, width=260, height=2, bg="black").place(x=20, y=135)
        show_details_button = Button(principal_window, text="Details", activeforeground="black",
                                     activebackground="white",
                                     command=show_aadhar_details, font=('chiller', 10, 'bold'), fg="white", bg="blue")
        show_details_button.place(x=50, y=180, width=100)
        show_details_button = Button(principal_window, text="Fee Details", command=show_fee_details,
                                     activeforeground="black", activebackground="white", font=('chiller', 10, 'bold'),
                                     fg="white", bg="blue")
        show_details_button.place(x=210, y=180, width=100)
        principal_window.mainloop()

    # Create the login window
    login_window = Tk()
    login_window.grab_set()
    login_window.geometry('300x249+800+200')  # w x h
    login_window.title("Principal login Window")
    suggest_label = Label(login_window, text="Login with ID or Password", font=('chiller', 13, 'bold'))
    suggest_label.place(x=10, y=10, height=25, width=210)
    id_label = Label(login_window, text="Principal ID :", font=('chiller', 10, 'bold'))
    id_label.place(x=14, y=55, height=25, width=80)
    id_entry = Entry(login_window, bd=0, font=("Time in romana", 13, "bold"))
    id_entry.place(x=10, y=80, height=25, width=240)
    Frame(login_window, width=240, height=2, bg="black").place(x=10, y=103)
    password_label = Label(login_window, text="Password:", font=('chiller', 10, 'bold'))
    password_label.place(x=10, y=120, height=25, width=77)
    password_entry = Entry(login_window, font=(13,), show="*", bd=0)
    password_entry.place(x=10, y=150, height=25, width=240)
    Frame(login_window, width=240, height=2, bg="black").place(x=10, y=173)
    login_button = Button(login_window, text="Login", bg="Dark blue", fg="white",
                          font=("Microsoft YaHei UI Light", 10, "bold"), command=login)
    login_button.place(x=100, y=200, width=100)
    login_window.mainloop()


def exit_studt():
    var = messagebox.askyesno("Notification", "Do you want to exit?")
    if var == True:
        qwe.destroy()


#  ######################################## connection of database ####################################################
def database_window():
    def btn_connect_server():
        global cur, conn
        host = host_var.get()
        user = user_var.get()
        password = password_var.get()
        try:
            conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password)
            cur = conn.cursor()  # Create a cursor object
        except:
            messagebox.showerror("notification", "DATA IS INCORRECT, PLEASE TRY AGAIN.")
            return
        try:
            conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password)
            cur = conn.cursor()
            strin = "CREATE DATABASE IF NOT EXISTS StudentPanel"
            cur.execute(strin)
            strin = 'USE StudentPanel'
            cur.execute(strin)
            strin = """CREATE TABLE INFORMATION (
                 ID  INT AUTO_INCREMENT PRIMARY KEY,
                     NAME VARCHAR(255),
                              AADHAR BIGINT,
                           DOB VARCHAR(255),
              ADDRESS VARCHAR(255),
               `CONTACT` VARCHAR(255),
                          EMAIL VARCHAR(255),
                          GENDER VARCHAR(255),
                           `DATE` VARCHAR(255)) """
            cur.execute(strin)
            strin = """CREATE TABLE IF NOT EXISTS submit (
                                   AADHAR BIGINT,
                                   FEE VARCHAR(255))"""
            cur.execute(strin)
            conn.close()
            messagebox.showinfo("Notification", "Database created. Now in database")
        except:
            strin = "USE StudentPanel"
            cur.execute(strin)
            messagebox.showinfo("Notification", "NOW YOU ARE CONNECTED TO THE DATABASE", parent=data)
        data.destroy()
        try:
            conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password)
            cur = conn.cursor()
            label.config(text="C", font=('chiller', 13, 'italic bold'), bg="green")
        except mysql.connector.connect:
            label.config(text="D", font=('chiller', 13, 'italic bold'), bg="red")
    def toggle_password():
        if show_password.get():
            entry_password.config(show="")
        else:
            entry_password.config(show="*")
    data = Toplevel()
    data.grab_set()  # close last label then first label
    data.geometry('390x290+900+300')  # w x h
    data.title("DataBase Window")
    data.resizable(False, False)
    data.config(bg="white")
    # ___________________________________________________________________________________connectdb label
    host1 = Label(data, text="Hostname : ", bg="white", font=("times", 14, "bold"), anchor="s")
    host1.place(x=5, y=60, height=34, width=140)
    user = Label(data, text="Username : ", bg="white", font=("times", 14, "bold"), anchor="s")
    user.place(x=5, y=95, height=34, width=140)
    password = Label(data, text="Password : ", bg="white", font=("times", 14, "bold"), anchor="s")
    password.place(x=5, y=132, height=34, width=140)
    password = Label(data, text="CONNECT TO DATABASE ", bg="white", font=("times", 15, "bold"), anchor="s")
    password.place(x=10, y=10, height=34, width=250)
    # ______________________________________________________________________________________entry-label of connection
    host_var = StringVar()
    user_var = StringVar()
    password_var = StringVar()
    entry_host = Entry(data, relief=GROOVE, borderwidth=3, textvariable=host_var, font=("Time in romana", 14,), bd=0,
                       bg="white")
    entry_host.place(x=150, y=64, height=34, width=200)
    Frame(data, width=200, height=2, bg="black").place(x=150, y=90)
    entry_user = Entry(data, relief=GROOVE, borderwidth=3, bd=0, textvariable=user_var, font=("Time in romana", 14),
                       bg="white")
    entry_user.place(x=150, y=99, height=34, width=200)
    Frame(data, width=200, height=2, bg="black").place(x=150, y=125)
    entry_password = Entry(data, relief=GROOVE, borderwidth=3, bd=0, textvariable=password_var,
                           font=("Time in romana", 14), bg="white", show="*")
    entry_password.place(x=150, y=138, height=34, width=200)
    Frame(data, width=200, height=2, bg="black").place(x=150, y=164)

    connect_btn = Button(data, text="   CONNECT   ", font=("Time in romana", 13, "bold"), borderwidth=3, bg="blue",
                         width=15, activebackground='white', activeforeground='black', bd=3, fg="white",
                         command=btn_connect_server)
    connect_btn.place(x=125, y=230)
    show_password = BooleanVar()
    show_password.set(False)
    show_password_checkbox = Checkbutton(data, text="Show Password", variable=show_password,
                                         font=("Time in romana",10 , "bold"), command=toggle_password)
    show_password_checkbox.place(x=230,y=177)
    data.mainloop()


# _____________________________________________________________________________________  CALLING TITLE BAR
colors = ["red", "green", "white", "blue", "yellow", "pink", "red2", "sky blue"]


def titlebar_color():
    fg = random.choice(colors)
    title.config(fg=fg)
    title.after(250, titlebar_color)


def titlebar():
    global count, text
    if count >= len(x):
        count = 0
        text = ""
        title.config(text=text)
    else:
        text = text + x[count]
        title.config(text=text)
        count += 1
    title.after(200, titlebar)


# ___________________________________________________________________________________________________timer panel
def timer():
    time_module = time.strftime("%r")
    date_module = time.strftime("%d-%m-%Y")
    clock.config(text=date_module + "\n" + time_module)
    clock.after(300, timer)


# ____________________________________________________________________________________________________first panel
qwe = Tk()
qwe.title("Student Management System")
qwe.geometry("1078x630+250+40")  # w x h
qwe.resizable(False, False)
qwe.configure(bg="black")

dataentryframe = Frame(qwe, bg="gold2")
dataentryframe.place(x=0, y=130, height=500, width=240)
self = Label(dataentryframe, text="CODE BY NI30", bg="gold2")
self.place(x=120, y=481)

im = PhotoImage(file=r"""std.png""")
frame = Label(qwe, image=im, bg="black")
frame.place(x=30, y=20, height=95, width=113)

dataentryframe1 = Frame(qwe, bg="white")
dataentryframe1.place(x=234, y=130, height=500, width=843)
# _________________________________________________    show     ________________________
style_1 = ttk.Style()
style_1.configure("Treeview.Heading", font=("Time in romana", 13, "bold"), foreground="blue")
style_1.configure("Treeview", font=("Time in romana", 13, "bold"), foreground="black", background="white")
scroll_x = Scrollbar(dataentryframe1, orient=HORIZONTAL)
scroll_y = Scrollbar(dataentryframe1, orient=VERTICAL)
student_details = Treeview(dataentryframe1,
                           columns=("id", "Name", "Aadhar", "DOB", "ADDRESS", "Contact", "Email", "Gender", "DATE"),
                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=student_details.xview)
scroll_y.config(command=student_details.yview)
student_details.heading("id", text="ID")
student_details.heading("Name", text="NAME")
student_details.heading("Aadhar", text="AADHAR")
student_details.heading("ADDRESS", text="ADDRESS")
student_details.heading("Contact", text="CONTACT")
student_details.heading("Email", text="EMAIL")
student_details.heading("DOB", text="DOB")
student_details.heading("Gender", text="GENDER")
student_details.heading("DATE", text="DATE")
student_details["show"] = "headings"
student_details.column("id", width=50)
student_details.column("Name", width=150)
student_details.column("Aadhar", width=150)
student_details.column("ADDRESS", width=200)
student_details.column("Contact", width=150)
student_details.column("Email", width=200)
student_details.column("DOB", width=150)
student_details.column("Gender", width=100)
student_details.column("DATE", width=100)
student_details.pack(fill=BOTH, expand=1)
# #################################################  BUTTONS  #########################################################

student_btn = Button(dataentryframe, text="ADMISSION", font=("time to romana", 15, "bold"), borderwidth=4,
                     bg="white", width=13, activebackground='blue', activeforeground='white',
                     command=student_admission)
student_btn.place(x=35, y=75)
fee_btn = Button(dataentryframe, text="FEE", font=("time to romana", 15, "bold"), borderwidth=4,
                 bg="white", width=13, activebackground='blue', activeforeground='white', command=fee_submit)
fee_btn.place(x=35, y=155)
detail_btn = Button(dataentryframe, text="DETAILS", font=("time to romana", 15, "bold"), borderwidth=4,
                    bg="white", width=13, activebackground='blue', activeforeground='white', command=search_student)
detail_btn.place(x=35, y=235)
principal_btn = Button(dataentryframe, text="PRINCIPAL", font=("time to romana", 15, "bold"), borderwidth=4,
                       bg="white", width=13, activebackground='blue', activeforeground='white',
                       command=principal_access)
principal_btn.place(x=35, y=315)
exit_btn = Button(dataentryframe, text="EXIT", font=("time to romana", 15, "bold"), borderwidth=4,
                  bg="white", width=13, activebackground='blue', activeforeground='white', command=exit_studt)
exit_btn.place(x=35, y=400)
# ________________________________________________________________________________________________ title
x = " WELCOME TO N.K.Y SCHOOL MANAGEMENT SYSTEM "
count = 0
text = ''
title = Label(qwe, text=x, font=('chiller', 20, ' bold'), fg="white", bg="black")
title.place(x=180, y=40, width=730)
titlebar()
titlebar_color()
# _________________________________________________________________________________   clock
clock = Label(qwe, font=('Microsoft YaHei', 10, 'bold'), fg="white", bg="gold2")
clock.place(x=0, y=130)
timer()
# _________________________________________________________________________________________________ connect to database

database_butt0n = Button(qwe, text="DATA BASE", font=('chiller', 11, 'italic bold'), relief=GROOVE,
                         borderwidth=3, bg="white", fg="black", activebackground='blue', activeforeground='white',
                         command=database_window)
database_butt0n.place(x=922, y=90, height=36, width=113)
label = Label(qwe, text="D", font=('chiller', 13, 'italic bold'), bg="red", fg="white")
label.place(x=1037, y=90, height=36, width=40)
qwe.mainloop()
