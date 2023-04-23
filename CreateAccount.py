# Tkinter is used to develop this project
import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
from random import randint
import re


def createAcc(Create, Name, PAN, DOB, Phone):
    if Name == "" or PAN == "" or DOB == "":
        messagebox.showwarning("Invalid Details!", "Values Can't Be Empty")
        return
    for x in Name:
        if x.isalpha() or x.isspace():
            continue
        messagebox.showerror("Invalid Name", "Name Can't have numbers/Special Characters")
        return
    if len(PAN) != 10 or not PAN.isalnum():
        messagebox.showerror("Invalid PAN Number", "Please Enter Correct PAN Number")
        return
    if not re.compile('\d\d\d\d-\d\d-\d\d').search(DOB):
        messagebox.showerror("Invalid Date", "Date Should be the format YYYY-MM-DD")
        return
    if len(str(Phone)) != 10:
        messagebox.showerror("Invalid Phone Number", "Phone Number should be of Length 10")
        return

    con = mysql.connect(host="localhost", user="root", password="vijay@1234", database="bank")
    cursor = con.cursor()
    cursor.execute('SELECT * FROM customer')
    AccNo = randint(1000, 9999)
    Password = randint(1000, 9999)
    result = cursor.fetchall()
    if result:
        a = False
        while not a:
            AccNo = randint(1000, 9999)
            for y in result:
                if y[4] == str(AccNo):
                    a = False
                    break
                else:
                    a = True

        for x in result:
            if x[1] == PAN:
                messagebox.showerror("Repeated Details", "Account Already Exist")
                return
        x = False
        while not x:
            Password = randint(1000, 9999)
            for y in result:
                if y[6] == str(Password):
                    x = False
                    break
                else:
                    x = True
    cursor.execute(f"INSERT INTO customer VALUES ('{Name}' , '{PAN}','{DOB}',{Phone},{AccNo},{0},{Password})")
    messagebox.showinfo("Action Successful", "Account Created Successfully")
    con.commit()
    Create.destroy()
    from AccInfo import AccInfo
    AccInfo(Name, PAN, DOB, Phone, AccNo, Password, 0)


def toHome(Create):
    Create.destroy()
    from HomePage import Home_Creator
    Home_Creator()


def SignUp():
    # Useful Variables
    BackgroundColor = "#c6cdcf"
    ButtonColor = "#c8dbde"

    Create_Account = tkinter.Tk()
    # Window Setting
    Create_Account.geometry("500x500")
    Create_Account.resizable(False, False)
    Create_Account.title("Realities Bank - Create New Account")
    Create_Account.iconbitmap("Images/bank.ico")
    Create_Account.config(bg=BackgroundColor)

    # Logo Of Bank
    logo = PhotoImage(file="Images/BankLogo.png")
    BankLogo = Label(image=logo, bg=BackgroundColor)
    BankLogo.place(x=30, y=0)

    # Name Label
    NameLabel = Label(text="Full Name(As on PAN Card)", font="Roboto 15 bold", bg=BackgroundColor)
    NameLabel.place(x=100, y=120)
    NameTextField = Entry(Create_Account, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3)
    NameTextField.place(x=102, y=150)

    # PAN Number Label
    PAN_NumberLabel = Label(text="PAN Number", font="Roboto 15 bold", bg=BackgroundColor)
    PAN_NumberLabel.place(x=100, y=185)
    PAN_NumberTextField = Entry(Create_Account, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3)
    PAN_NumberTextField.place(x=102, y=215)

    # Date Of Birth Label
    DOBLabel = Label(text="DOB(YYYY-MM-DD)", font="Roboto 15 bold", bg=BackgroundColor)
    DOBLabel.place(x=100, y=250)
    DOBTextField = Entry(Create_Account, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3)
    DOBTextField.place(x=102, y=280)

    # Phone Number Label
    Phone_NumberLabel = Label(text="Phone Number", font="Roboto 15 bold", bg=BackgroundColor)
    Phone_NumberLabel.place(x=100, y=315)
    Phone_NumberTextField = Entry(Create_Account, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3)
    Phone_NumberTextField.place(x=102, y=345)

    # Submit Button
    Submit = Button(text="Create Account", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
                    relief=RAISED, width=15, activebackground=ButtonColor,
                    command=lambda: createAcc(Create_Account, NameTextField.get(), PAN_NumberTextField.get(),
                                              DOBTextField.get(), Phone_NumberTextField.get()))
    Submit.place(x=145, y=400)

    # Back Button
    Back = Button(text="Back", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
                  relief=RAISED, activebackground=ButtonColor, command=lambda: toHome(Create_Account))
    Back.place(x=5, y=450)

    Create_Account.mainloop()

