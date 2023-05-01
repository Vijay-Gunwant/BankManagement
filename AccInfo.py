import tkinter
from tkinter import *
import os
from tkinter import messagebox
import re
import mysql.connector as mysql


def toReset(Acc):
    Acc.destroy()
    from ForgotPassword import Reset_Creator
    Reset_Creator()


def toBack(Acc,AccNo):
    Acc.destroy()
    from Menu import Options_Creator
    Options_Creator(AccNo)


def SaveDetails(Name, PAN, DOB, Phone, AccNo, Password, Cash):
    details = f"Name = {Name}\nPAN  = {PAN}\nDOB  = {DOB}\nPhone = {Phone}\nAccNo = {AccNo}\nPassword = {Password}\nCash = {Cash}"
    fileName = open(f"./Imp/{Name}.txt", "w+")
    fileName.write(details)
    fileName.close()
    os.system(f"notepad ./Imp/{Name}.txt")


def UpdateDetails(Acc_Info, Name, PAN, DOB, Phone, AccNo, Pass, Cash):
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
    cursor.execute("SELECT * FROM customer")
    result = cursor.fetchall()
    for x in result:
        if x[1] == PAN and str(x[4]) != AccNo:
            messagebox.showerror("PAN Number Duplicate", "PAN Number is already present")
            return
    cursor.execute(f"UPDATE customer SET Name='{Name}',PAN='{PAN}',DOB='{DOB}',Phone={Phone} WHERE Acc = {AccNo};")
    con.commit()
    Acc_Info.destroy()
    AccInfo(Name, PAN, DOB, Phone, AccNo, Pass, Cash)


def AccInfo(Name, PAN, DOB, Phone, AccNo, Password, Cash):
    # Useful Variables
    BackgroundColor = "#c6cdcf"
    ButtonColor = "#c8dbde"

    Acc_Info = tkinter.Tk()
    # Window Setting
    Acc_Info.geometry("800x500")
    Acc_Info.resizable(False, False)
    Acc_Info.title("Realities Bank - Create New Account")
    Acc_Info.iconbitmap("Images/bank.ico")
    Acc_Info.config(bg=BackgroundColor)

    # Logo Of Bank
    logo = PhotoImage(file="Images/BankLogo.png")
    BankLogo = Label(Acc_Info, image=logo, bg=BackgroundColor)
    BankLogo.place(x=150, y=0)

    # Name Label
    NameLabel = Label(Acc_Info, text="Full Name", font="Roboto 15 bold", bg=BackgroundColor)
    NameLabel.place(x=100, y=120)
    NameTextField = Entry(Acc_Info, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3)
    NameTextField.insert(0, Name)
    NameTextField.place(x=102, y=150)

    # PAN Number Label
    PAN_NumberLabel = Label(Acc_Info, text="PAN Number", font="Roboto 15 bold", bg=BackgroundColor)
    PAN_NumberLabel.place(x=100, y=185)
    PAN_NumberTextField = Entry(Acc_Info, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3)
    PAN_NumberTextField.insert(0, PAN)
    PAN_NumberTextField.place(x=102, y=215)

    # Date Of Birth Label
    DOBLabel = Label(Acc_Info, text="DOB(YYYY-MM-DD)", font="Roboto 15 bold", bg=BackgroundColor)
    DOBLabel.place(x=100, y=250)
    DOBTextField = Entry(Acc_Info, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3)
    DOBTextField.insert(0, DOB)
    DOBTextField.place(x=102, y=280)

    # Phone Number Label
    Phone_NumberLabel = Label(Acc_Info, text="Phone Number", font="Roboto 15 bold", bg=BackgroundColor)
    Phone_NumberLabel.place(x=100, y=315)
    Phone_NumberTextField = Entry(Acc_Info, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3)
    Phone_NumberTextField.insert(0, Phone)
    Phone_NumberTextField.place(x=102, y=345)

    # AccNo. Label
    AccNoLabel = Label(Acc_Info, text="Account Number", font="Roboto 15 bold", bg=BackgroundColor)
    AccNoLabel.place(x=430, y=120)
    AccNoTextField = Entry(Acc_Info, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3)
    AccNoTextField.insert(0, AccNo)
    AccNoTextField.config(state="disabled")
    AccNoTextField.place(x=432, y=150)

    # Password Number Label
    PasswordLabel = Label(Acc_Info, text="Password", font="Roboto 15 bold", bg=BackgroundColor)
    PasswordLabel.place(x=430, y=185)
    PasswordTextField = Entry(Acc_Info, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3)
    PasswordTextField.insert(0, Password)
    PasswordTextField.config(state="disabled")
    PasswordTextField.place(x=432, y=215)

    # Cash Label
    CashLabel = Label(Acc_Info, text="Balance Amount", font="Roboto 15 bold", bg=BackgroundColor)
    CashLabel.place(x=430, y=250)
    CashTextField = Entry(Acc_Info, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3)
    CashTextField.insert(0, Cash)
    CashTextField.config(state="disabled")
    CashTextField.place(x=432, y=280)

    # Update Button
    Update = Button(Acc_Info, text="Update Details?", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
                    relief=RAISED, activebackground=ButtonColor,
                    command=lambda: UpdateDetails(Acc_Info, NameTextField.get(), PAN_NumberTextField.get(),
                                                  DOBTextField.get(),
                                                  Phone_NumberTextField.get(), AccNoTextField.get(),
                                                  PasswordTextField.get(), CashTextField.get()))
    Update.place(x=300, y=400)

    # Message Label
    MessageLabel = Label(Acc_Info, text="Edit Your Details And Press The Button", font="Roboto 12 bold",
                         bg=BackgroundColor)
    MessageLabel.place(x=230, y=450)

    # Save Button
    Save = Button(Acc_Info, text="Save Details", font="Roboto 12 bold", bg=ButtonColor, cursor="hand2",
                  relief=RAISED, activebackground=ButtonColor,
                  command=lambda: SaveDetails(Name, PAN, DOB, Phone, AccNo, Password, Cash))
    Save.place(x=430, y=330)
    # Reset Password Button
    Reset = Button(Acc_Info, text="Reset Password", font="Roboto 12 bold", bg=ButtonColor, cursor="hand2",
                   relief=RAISED, activebackground=ButtonColor,
                   command=lambda: toReset(Acc_Info))
    Reset.place(x=550, y=330)

    # Back Button
    Back = Button(Acc_Info, text="Back", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
                  relief=RAISED, activebackground=ButtonColor, command=lambda: toBack(Acc_Info,AccNo))
    Back.place(x=5, y=450)

    Acc_Info.mainloop()

