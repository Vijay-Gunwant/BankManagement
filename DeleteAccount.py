# Tkinter is used to develop this project
import tkinter
from tkinter import *
from tkinter import messagebox

def DeleteAcc():
    pass

def toLogin():
    Delete_Account.destroy()
    import LoginPage


def toHome():
    Delete_Account.destroy()
    import HomePage


# Useful Variables
BackgroundColor = "#c6cdcf"
ButtonColor = "#c8dbde"

Delete_Account = tkinter.Tk()
# Window Setting
Delete_Account.geometry("500x500")
Delete_Account.resizable(False, False)
Delete_Account.title("Realities Bank - Change Password")
Delete_Account.iconphoto(False, PhotoImage(file="./Images/bank.png"))
Delete_Account.config(bg=BackgroundColor)

# Logo Of Bank
logo = PhotoImage(file="Images/BankLogo.png")
BankLogo = Label(image=logo, bg=BackgroundColor)
BankLogo.place(x=30, y=0)



# Password Label
Account_NumberLabel = Label(text="Account Number", font="Roboto 15 bold", bg=BackgroundColor)
Account_NumberLabel.place(x=100, y=185)
Account_NumberTextField = Entry(Delete_Account, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3)
Account_NumberTextField.place(x=102, y=215)

# Submit Button
Submit = Button(text="Delete Account", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
                relief=RAISED, width=15, activebackground=ButtonColor, command=DeleteAcc)
Submit.place(x=145, y=260)

# Back Button
Back = Button(text="Back", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
              relief=RAISED, activebackground=ButtonColor, command=toLogin)
Back.place(x=5, y=450)

# Home Button
Home = Button(text="Home", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
              relief=RAISED, activebackground=ButtonColor, command=toHome)
Home.place(x=420, y=450)
Delete_Account.mainloop()
