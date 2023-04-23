# Tkinter is used to develop this project
import tkinter
from tkinter import *
from tkinter import messagebox


def toMenu():
    pass


def toHome():
    Show_Info.destroy()
    import HomePage


# Useful Variables
BackgroundColor = "#c6cdcf"
ButtonColor = "#c8dbde"

Show_Info = tkinter.Tk()
# Window Setting
Show_Info.geometry("500x500")
Show_Info.resizable(False, False)
Show_Info.title("Realities Bank - Create New Account")
Show_Info.iconphoto(False, PhotoImage(file="./Images/bank.png"))
Show_Info.config(bg=BackgroundColor)

# Logo Of Bank
logo = PhotoImage(file="Images/BankLogo.png")
BankLogo = Label(image=logo, bg=BackgroundColor)
BankLogo.place(x=30, y=0)

# Name
NameLabel = Label(text="Full Name(As on PAN Card)", font="Roboto 15 bold", bg=BackgroundColor)
NameLabel.place(x=100, y=120)
NameTextField = Entry(Show_Info, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3,state="disabled")
NameTextField.place(x=102, y=150)

# PAN Number
PAN_NumberLabel = Label(text="PAN Number", font="Roboto 15 bold", bg=BackgroundColor)
PAN_NumberLabel.place(x=100, y=185)
PAN_NumberTextField = Entry(Show_Info, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3,state="disabled")
PAN_NumberTextField.place(x=102, y=215)

# Date Of Birth
DOBLabel = Label(text="DOB(DD-MM-YYYY)", font="Roboto 15 bold", bg=BackgroundColor)
DOBLabel.place(x=100, y=250)
DOBTextField = Entry(Show_Info, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3,state="disabled")
DOBTextField.place(x=102, y=280)

# Phone Number
Phone_NumberLabel = Label(text="Phone Number", font="Roboto 15 bold", bg=BackgroundColor)
Phone_NumberLabel.place(x=100, y=315)
Phone_NumberTextField = Entry(Show_Info, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3,state="disabled")
Phone_NumberTextField.place(x=102, y=345)

# Back Button
Back = Button(text="Back", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
              relief=RAISED, activebackground=ButtonColor, command=toMenu)
Back.place(x=5, y=450)

Show_Info.mainloop()
