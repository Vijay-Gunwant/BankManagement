# Tkinter is used to develop this project
import tkinter
from tkinter import *
from tkinter import messagebox


def changePass():
    pass


def toLogin():
    Account_Info.destroy()
    import LoginPage


# Useful Variables
BackgroundColor = "#c6cdcf"
ButtonColor = "#c8dbde"

Account_Info = tkinter.Tk()
# Window Setting
Account_Info.geometry("500x500")
Account_Info.resizable(False, False)
Account_Info.title("Realities Bank - Vital Account Information")
Account_Info.iconphoto(False, PhotoImage(file="./Images/bank.png"))
Account_Info.config(bg=BackgroundColor)

# Logo Of Bank
logo = PhotoImage(file="Images/BankLogo.png")
BankLogo = Label(image=logo, bg=BackgroundColor)
BankLogo.place(x=30, y=0)

# Security Code Label
NameLabel = Label(text="Name", font="Roboto 15 bold", bg=BackgroundColor)
NameLabel.place(x=100, y=150)
NameTextField = Entry(Account_Info, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3)
name = tkinter.StringVar(NameTextField, "Vijay")
NameTextField.config(state="readonly", textvariable=name)
NameTextField.place(x=102, y=180)

# Account Number Label
Account_NumberLabel = Label(text="Account Number", font="Roboto 15 bold", bg=BackgroundColor)
Account_NumberLabel.place(x=100, y=220)
Account_NumberTextField = Entry(Account_Info, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3)
AccNo = tkinter.StringVar(Account_NumberTextField, "1234")
Account_NumberTextField.config(state="readonly", textvariable=AccNo)
Account_NumberTextField.place(x=102, y=250)

# Confirm Account Number Label
PasswordLabel = Label(text="Password", font="Roboto 15 bold", bg=BackgroundColor)
PasswordLabel.place(x=100, y=290)
PasswordTextField = Entry(Account_Info, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3)
password = tkinter.StringVar(PasswordTextField, "1234")
PasswordTextField.config(state="readonly", textvariable=password)
PasswordTextField.place(x=102, y=320)

# Back Button
Back = Button(text="Back", font="Roboto 15 bold", cursor="hand2",
              relief=RAISED, activebackground=BackgroundColor, command=toLogin)
Back.place(x=5, y=450)
Account_Info.mainloop()
