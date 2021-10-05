from tkinter import *
from PIL import ImageTk,Image
import mysql.connector as c
import tkinter.messagebox as msg
from datetime import datetime
import random
import sys

mydb = c.connect(host="localhost", user="root", passwd="$amgod510", database="hospital_sys")
cursor = mydb.cursor()

# signup_user function for storing data into sql table
def signup_user():
    global screen1
    name = nameval.get()
    age = ageval.get()
    city = cityval.get()
    address = addval.get()
    username = username_val.get()
    password = pass_val.get()
    gender = genderval.get()

    query = "insert into login(name,age,city,address,username,password,gender)values('{}',{},'{}','{}','{}','{}','{}')".format(name,age,city,address,username,password,gender)

    cursor.execute(query)
    mydb.commit()


# fill form for signup
def signup():
    global screen1

    screen1 = Toplevel(screen)
    screen1.title("Sign Up")
    screen1.geometry("500x600")

    global nameval
    global ageval
    global genderval
    global cityval
    global addval
    global username_val
    global pass_val

    nameval = StringVar()
    ageval = IntVar()
    cityval = StringVar()
    addval = StringVar()
    username_val = StringVar()
    pass_val = StringVar()
    genderval = StringVar()

    ageval.set("")    

    Label(screen1,text="Sign Up",font=("arial bold",20),pady=30).pack(padx=100)

    f1 = Frame(screen1)
    Label(f1,text="Name:",padx=30,font=("arial bold",10)).pack(side="left")
    Name_entry = Entry(f1,textvariable=nameval).pack(side="left")
    f1.pack(pady=5)
    f2 = Frame(screen1)
    Label(f2,text="Age:",padx=35,font=("arial bold",10)).pack(side="left")
    Age_entry = Entry(f2,textvariable=ageval).pack(side="left")
    f2.pack(pady=5)
    
    f3 = Frame(screen1)
    Label(f3,text="City:",padx=35,font=("arial bold",10)).pack(side="left")
    City_entry = Entry(f3,textvariable=cityval).pack(side="left")
    f3.pack(pady=5)
    f4 = Frame(screen1)
    Label(f4,text="Address:",padx=22,font=("arial bold",10)).pack(side="left")
    Add_entry = Entry(f4,textvariable=addval).pack(side="left")
    f4.pack(pady=5)
    f5 = Frame(screen1)
    Label(f5,text="User_Name:",padx=11,font=("arial bold",10)).pack(side="left")
    UserName_entry = Entry(f5,textvariable=username_val).pack(side="left")
    f5.pack(pady=5)
    f6 = Frame(screen1)
    Label(f6,text="Password:",padx=16,font=("arial bold",10)).pack(side="left")
    PassVal_entry = Entry(f6,show="*",textvariable=pass_val).pack(side="left")
    f6.pack(pady=5)
    f7 = Frame(screen1)
    Label(f7,text="Gender",padx=25,font=("arial bold",10)).pack(side="left")
    gender_entry = Entry(f7,textvariable=genderval).pack(side="left")
    f7.pack(pady=5)

    

    f8 = Frame(screen1,bd=2)
    Button(f8,text="Sign Up",command=signup_user).pack(side='left',pady=5,padx=3)
    Button(f8,text="Clear",command=quit).pack(side='left',pady=5)
    f8.pack()

    
#create new password
def create_new_password():
    username = user_val.get()
    password = new_pass.get()

    query = "update login set password='{}' where username='{}'".format(password,username)
    cursor.execute(query)
    mydb.commit()
    print("done")

def Submit():
    id_value = id_var.get()
    name = doctor_name.get()
    specialization = specialist.get()
    contact_ = contact.get()

    query = "insert into doctor_data values({},'{}','{}','{}')".format(id_value,name,specialization,contact_)
    cursor.execute(query)
    mydb.commit()

def doctor_search():
    doc_name = search.get()

    query = "select * from doctor_data where name='{}'".format(doc_name)
    cursor.execute(query)
    data = cursor.fetchone()

    msg.showinfo("Doctors",f"Doctor name is {data[1]}\nspecialisation in {data[2]}\ncontact no. is:{data[3]}")

def Delete():
    id_value = id_var.get()

    query = "delete from doctor_data where id={}".format(id_value)
    cursor.execute(query)
    mydb.commit()

def Update():
    id_value = id_var.get()
    name = doctor_name.get()
    specialization = specialist.get()
    contact_ = contact.get()

    query = "update doctor_data set name='{}' where id={}".format(name,id_value)
    cursor.execute(query)
    mydb.commit()
    query = "update doctor_data set specialization='{}' where id={}".format(specialization,id_value)
    cursor.execute(query)
    mydb.commit()
    query = "update doctor_data set contact='{}' where id={}".format(contact_,id_value)
    cursor.execute(query)
    mydb.commit()

    
    


def view():
    global screen4

    screen4 = Toplevel(screen3)

    screen4.geometry("700x300")
    screen4.maxsize(700,300)

    frame = Frame(screen4,bd=2)

    Label(frame,text="id").pack(side="left",padx=20)
    Label(frame,text="Name").pack(side="left",padx=15)
    Label(frame,text="Specialization").pack(side="left",padx=15)
    Label(frame,text="Contact").pack(side="left",padx=15)

    frame.pack(side="top")

    query = "select * from doctor_data"
    cursor.execute(query)
    data = cursor.fetchall()

    for datas in data:
        Label(screen4,text=f"{datas[0]}       {datas[1]}          {datas[2]}            {datas[3]}").pack()
            

    
def doctors():
    global screen3

    screen3 = Toplevel(screen2)
    screen3.geometry("700x300")
    screen3.maxsize(700,300)

    global doctor_name
    global specialist
    global contact
    global search
    global id_var

    doctor_name = StringVar()
    specialist = StringVar()
    contact = StringVar()
    search = StringVar()
    id_var = IntVar()

    frame = Frame(screen3,bd=2,bg="white")
    Button(frame,text="back",bg="pale goldenrod",command=login_user).pack(anchor="nw")
    frame.pack(side="top",fill="both",pady=5)

    frame0 = Frame(screen3,bd=2)
    Label(frame0,text="id").pack(side="left",padx=32)
    id_entry = Entry(frame0,textvariable=id_var).pack(side="left")
    search_entry = Entry(frame0,textvariable=search).pack(side="left",padx=5)
    Button(frame0,text="Search",command=doctor_search,bg="forest green").pack(side="left",padx=2)
    frame0.pack(pady = 5,fill="x")

    frame1 = Frame(screen3,bd=2)
    Label(frame1,text="Doctor Name").pack(side="left")
    d_name_entry = Entry(frame1,textvariable=doctor_name).pack(side="left")
    frame1.pack(pady = 5,fill="x")

    frame2 = Frame(screen3,bd=2)
    Label(frame2,text="Specialization").pack(side="left")
    d_name_entry = Entry(frame2,textvariable=specialist).pack(side="left")
    frame2.pack(pady = 5,fill="x")

    frame3 = Frame(screen3,bd=2)
    Label(frame3,text="Contact").pack(side="left",padx=15)
    d_name_entry = Entry(frame3,textvariable=contact).pack(side="left")
    frame3.pack(pady=5,fill="x")

    frame4 = Frame(screen3,bd=2)

    Button(frame4,text="Submit",padx=10,pady=5,bg="medium purple",command=Submit).pack(side="left",padx=30)
    Button(frame4,text="Delete",padx=10,pady=5,bg="deepskyblue2",command=Delete).pack(side="left",padx=30)
    Button(frame4,text="Update",padx=10,pady=5,bg="slategray2",command=Update).pack(side="left",padx=30)
    Button(frame4,text="View",padx=10,pady=5,bg="seagreen2",command=view).pack(side="left",padx=30)

    frame4.pack(side="bottom",fill="x")


def Pat_Submit():
    id_value = id_var.get()
    name = patient_name.get()
    problem_ = problem.get()
    contact_ = contact.get()

    query = "insert into patient_data values({},'{}','{}','{}')".format(id_value,name,problem_,contact_)
    cursor.execute(query)
    mydb.commit()

def patient_search():
    pat_name = search.get()

    query = "select * from patient_data where name='{}'".format(pat_name)
    cursor.execute(query)
    data = cursor.fetchone()

    msg.showinfo("patients",f"Patient name is {data[1]}\ncontact no:{data[3]}")

def Pat_Delete():
    id_value = id_var.get()

    query = "delete from patient_data where id={}".format(id_value)
    cursor.execute(query)
    mydb.commit()

def Pat_Update():
    id_value = id_var.get()
    name = doctor_name.get()
    specialization = specialist.get()
    contact_ = contact.get()

    query = "update patient_data set name='{}' where id={}".format(name,id_value)
    cursor.execute(query)
    mydb.commit()
    query = "update patient_data set problem='{}' where id={}".format(problem_,id_value)
    cursor.execute(query)
    mydb.commit()
    query = "update patient_data set contact='{}' where id={}".format(contact_,id_value)
    cursor.execute(query)
    mydb.commit()

    
    


def Pat_view():
    global screen6

    screen6 = Toplevel(screen5)

    screen6.geometry("700x300")
    screen6.maxsize(700,300)

    frame = Frame(screen6,bd=2)

    Label(frame,text="id").pack(side="left",padx=40)
    Label(frame,text="Patient_Name").pack(side="left",padx=40)
    Label(frame,text="Problem").pack(side="left",padx=40)
    Label(frame,text="Contact").pack(side="left",padx=40)

    frame.pack(side="top")

    query = "select * from patient_data"
    cursor.execute(query)
    data = cursor.fetchall()

    for datas in data:
        frame1 = Frame(screen6,bd=2)
        Label(frame1,text=f"{datas[0]}").pack(side="left",padx=40)
        Label(frame1,text=f"{datas[1]}").pack(side="left",padx=40)
        Label(frame1,text=f"{datas[2]}").pack(side="left",padx=40)
        Label(frame1,text=f"{datas[3]}").pack(side="left")
        frame1.pack()
            

def Patients():

    global screen5

    screen5 = Toplevel(screen2)
    screen5.geometry("700x300")
    screen5.maxsize(700,300)

    global patient_name
    global problem
    global contact
    global search
    global id_var

    patient_name = StringVar()
    problem = StringVar()
    contact = StringVar()
    search = StringVar()
    id_var = IntVar()

    frame = Frame(screen5,bd=2,bg="white")
    Button(frame,text="back",bg="pale goldenrod",command=login_user).pack(anchor="nw")
    frame.pack(side="top",fill="both",pady=5)

    frame0 = Frame(screen5,bd=2)
    Label(frame0,text="id").pack(side="left",padx=32)
    id_entry = Entry(frame0,textvariable=id_var).pack(side="left")
    search_entry = Entry(frame0,textvariable=search).pack(side="left",padx=5)
    Button(frame0,text="Search",command=patient_search,bg="forest green").pack(side="left",padx=2)
    frame0.pack(pady = 5,fill="x")

    frame1 = Frame(screen5,bd=2)
    Label(frame1,text="Patient Name").pack(side="left")
    d_name_entry = Entry(frame1,textvariable=patient_name).pack(side="left")
    frame1.pack(pady = 5,fill="x")

    frame2 = Frame(screen5,bd=2)
    Label(frame2,text="Problem").pack(side="left",padx=13)
    d_name_entry = Entry(frame2,textvariable=problem).pack(side="left")
    frame2.pack(pady = 5,fill="x")

    frame3 = Frame(screen5,bd=2)
    Label(frame3,text="Contact").pack(side="left",padx=15)
    d_name_entry = Entry(frame3,textvariable=contact).pack(side="left")
    frame3.pack(pady=5,fill="x")

    frame4 = Frame(screen5,bd=2)

    Button(frame4,text="Submit",padx=10,pady=5,bg="medium purple",command=Pat_Submit).pack(side="left",padx=30)
    Button(frame4,text="Delete",padx=10,pady=5,bg="deepskyblue2",command=Pat_Delete).pack(side="left",padx=30)
    Button(frame4,text="Update",padx=10,pady=5,bg="slategray2",command=Pat_Update).pack(side="left",padx=30)
    Button(frame4,text="View",padx=10,pady=5,bg="seagreen2",command=Pat_view).pack(side="left",padx=30)

    frame4.pack(side="bottom",fill="x")

def isleapyear(year):
    if (int(year) % 4) == 0:
        if (int(year) % 100) == 0:
            if (int(year) % 400) == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
def Appoinment():

    id = random.randrange(sys.maxsize)
    now = datetime.today()

    date = datetime.now()
    now1 = date.strftime("%d")
    now1 = int(now1)

    year = int(now.year)
    month = int(now.month)

    even_month = [1,3,5,7,8,10,12]
    odd_month = [4,6,9,11]

    if month in even_month:
        day = random.randrange(now1,32)
    elif month in odd_month:
        day = random.randrange(now1,31)
    else:
        if isleapyear(year):
            day = random.randrange(now1,30)
        else:
            day = random.randrange(now1,29)

    appoinment_day = f"{day}/{month}/{year}"
    msg.showinfo("Appoinment",f"Your Appoinment is on {appoinment_day}\nand your id is {id}\nThank you for booking appoinment")

    query = "insert into appoinment values({},'{}')".format(id,appoinment_day)
    cursor.execute(query)
    mydb.commit()
#log_in user function
# for checking that password is valid or not
# if valid open Admin screen otherwise show error

def patients_view():
    global screen8

    screen8 = Toplevel(screen2)
    screen8.configure(background="white")
    screen8.geometry("700x300")
    screen8.maxsize(700,300)

    frame = Frame(screen8,bd=2,bg="light salmon")

    Label(frame,text="id",bg="light salmon").pack(side="left",padx=20)
    Label(frame,text="Patient_Name",bg="light salmon").pack(side="left",padx=30)
    Label(frame,text="Problem",bg="light salmon").pack(side="left",padx=40)
    Label(frame,text="Contact",bg="light salmon").pack(side="left",padx=30)

    frame.pack(side="top")

    query = "select * from patient_data"
    cursor.execute(query)
    data = cursor.fetchall()

    for datas in data:
        frame1 = Frame(screen8,bd=2,bg="light salmon")
        Label(frame1,text=f"{datas[0]}",bg="light salmon").pack(side="left",padx=20)
        Label(frame1,text=f"{datas[1]}",bg="light salmon").pack(side="left",padx=30)
        Label(frame1,text=f"{datas[2]}",bg="light salmon").pack(side="left",padx=40)
        Label(frame1,text=f"{datas[3]}",bg="light salmon").pack(side="left",padx=30)
        frame1.pack()

def doctors_view():
    global screen7

    screen7 = Toplevel(screen2)
    screen7.configure(background="white")
    screen7.geometry("700x300")
    screen7.maxsize(700,300)

    frame = Frame(screen7,bd=2,bg="pale goldenrod")

    Label(frame,text="id",bg="pale goldenrod").pack(side="left",padx=20)
    Label(frame,text="Name",bg="pale goldenrod").pack(side="left",padx=15)
    Label(frame,text="Specialization",bg="pale goldenrod").pack(side="left",padx=15)
    Label(frame,text="Contact",bg="pale goldenrod").pack(side="left",padx=15)

    frame.pack(side="top")

    query = "select * from doctor_data"
    cursor.execute(query)
    data = cursor.fetchall()

    for datas in data:
        Label(screen7,text=f"{datas[0]}       {datas[1]}          {datas[2]}            {datas[3]}",bg="pale goldenrod").pack()
    
def login_user():

    user_name = userval.get()
    pass_word = passval.get()

    query = "select password from login where username='{}'".format(user_name)
    cursor.execute(query)
    data = cursor.fetchone()

    if (pass_word in data):
        global screen2

        screen2 = Toplevel(screen)
        screen2.configure(background="white")
        screen2.geometry("700x300")
        screen2.maxsize(700,300)
        screen2.title("Admin")

        frame1 = Frame(screen2,bd=2,bg="medium slate blue")
        Label(frame1,text="Menu").pack()
        Button(frame1,text="Home",pady=13,padx=20,bg="salmon",command=login_user).pack(pady=4)
        Button(frame1,text="Doctor",pady=13,padx=19,bg="yellow",command=doctors).pack(pady=4)
        Button(frame1,text="Patient",pady=13,padx=18,bg="forest green",command=Patients).pack(pady=4)
        Button(frame1,text="Appoinment",pady=13,padx=3,bg="pale green",command=Appoinment).pack(pady=4)
        Button(frame1,text="Exit",pady=13,padx=28,bg="violet",command=quit).pack(pady=4)
        
        frame1.pack(side="left",fill="y")

        frame2 = Frame(screen2,bd=2,bg="grey")
        Label(frame2,text="Admin Dashboard").pack(side="left")
        frame2.pack(side="top",fill="both")

        frame4 = Frame(screen2,bd=3,bg="white")

    
        Button(frame4,text="Doctors",bg="olive drab",padx=40,pady=5,command=doctors_view).pack(side="left",padx=10)
        Button(frame4,text="Patients",bg="pale goldenrod",padx=40,pady=5,command=patients_view).pack(side="left",padx=10)
        

        frame4.pack(fill="both")


        global user_val
        global pass_val
        global new_pass
        global user_entry
        global pass_entry
        global newpass_entry

        user_val = StringVar()
        pass_val = StringVar()
        new_pass = StringVar()

        frame3 = Frame(screen2,bd=3)

        Label(frame3,text="User Name",font=("arial bold",10)).pack()
        user_entry = Entry(frame3,textvariable=user_val).pack()
        Label(frame3,text="Old Password",font=("arial bold",10)).pack()
        pass_entry = Entry(frame3,show="*",textvariable=pass_val).pack()
        Label(frame3,text="New Password",font=("arial bold",10)).pack()
        pass_entry = Entry(frame3,show="*",textvariable=new_pass).pack()

        Button(frame3,text="Create",bg="blue",padx=5,pady=10,command=create_new_password).pack(pady=10)
        
        frame3.pack(pady=20)

    else:
        msg.showerror("error","Incorrect Username or Password\n please enter a valid password")
        

# Home screen  
def Home():
    global screen
    screen = Tk()
    screen.geometry("1000x400")
    screen.maxsize(1000,400)
    screen.title("Hospital Management System/By Sumit Godwan")

    frame  = Frame(screen,bd=2)
    image1 = Image.open("hospital1_home.jpeg")
    photo = ImageTk.PhotoImage(image1)
    label = Label(frame,image=photo)
    label.pack()
    frame.pack(side="right",anchor="ne")

    global userval
    global passval
    global user_entry
    global pass_entry

    userval = StringVar()
    passval = StringVar()

    frame = Frame(screen,bd=5)

    b1 = Button(frame,text="Switch To Sign Up",relief="sunken",command=signup).pack(pady=30,padx=20)
    Label(frame,text="Login",font=("arial bold",20)).pack(padx=30)
    Label(frame,text="User Name",font=("arial bold",10)).pack()
    user_entry = Entry(frame,textvariable=userval).pack()
    Label(frame,text="Password",font=("arial bold",10)).pack()
    pass_entry = Entry(frame,show="*",textvariable=passval).pack()

    f = Frame(frame,bd=2)
    Button(f,text="Login",command=login_user).pack(side='left',pady=5,padx=3)
    Button(f,text="Clear",command=quit).pack(side='left',pady=5)
    f.pack()

    frame.pack(fill="both")
    


    screen.mainloop()




Home()
