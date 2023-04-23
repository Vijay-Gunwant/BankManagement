# Tkinter is used to develop this project
import tkinter
from tkinter import *
from tkinter import messagebox


def createAcc():
    pass


def toHome():
    Create_Account.destroy()
    import HomePage


# Useful Variables
BackgroundColor = "#c6cdcf"
ButtonColor = "#c8dbde"

Create_Account = tkinter.Tk()
# Window Setting
Create_Account.geometry("500x500")
Create_Account.resizable(False, False)
Create_Account.title("Realities Bank - Create New Account")
Create_Account.iconphoto(False, PhotoImage(file="./Images/bank.png"))
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
DOBLabel = Label(text="DOB(DD-MM-YYYY)", font="Roboto 15 bold", bg=BackgroundColor)
DOBLabel.place(x=100, y=250)
DOBTextField = Entry(Create_Account, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3, show="*")
DOBTextField.place(x=102, y=280)

# Phone Number Label
Phone_NumberLabel = Label(text="Phone Number", font="Roboto 15 bold", bg=BackgroundColor)
Phone_NumberLabel.place(x=100, y=315)
Phone_NumberTextField = Entry(Create_Account, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3)
Phone_NumberTextField.place(x=102, y=345)

# Submit Button
Submit = Button(text="Create Account", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
                relief=RAISED, width=15, activebackground=ButtonColor, command=createAcc)
Submit.place(x=145, y=400)

# Back Button
Back = Button(text="Back", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
              relief=RAISED, activebackground=ButtonColor, command=toHome)
Back.place(x=5, y=450)

Create_Account.mainloop()
