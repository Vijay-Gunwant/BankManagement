# Tkinter is used to develop this project
import tkinter
from tkinter import *


def toLogin():
    Home_Page.destroy()
    import LoginPage


def toSignup():
    Home_Page.destroy()
    import CreateAccount


# Useful Variables
BackgroundColor = "#c6cdcf"
ButtonColor = "#c8dbde"
Home_Page = tkinter.Tk()

# Window Setting
Home_Page.geometry("500x500")
Home_Page.resizable(False, False)
Home_Page.title("Realities Bank - Home Page")
Home_Page.iconphoto(False, PhotoImage(file="./Images/bank.png"))
Home_Page.config(bg=BackgroundColor)

# Logo Of Bank
logo = PhotoImage(file="Images/BankLogo.png")
BankLogo = Label(image=logo, bg=BackgroundColor)
BankLogo.place(x=30, y=0)

# Login Button
ButtonImage1 = PhotoImage(file="Images/login.png")
Login = Button(image=ButtonImage1, bg=BackgroundColor, cursor="hand2", bd=0,
               relief=FLAT, activebackground=BackgroundColor, command=toLogin)
Login.place(x=160, y=220)

# Signup Label
SignupLabel = Label(text="Don't have an account?", font="Roboto 15 bold", bg=BackgroundColor)
SignupLabel.place(x=120, y=280)
# Signup Button
ButtonImage2 = PhotoImage(file="Images/signup.png")
Login = Button(image=ButtonImage2, font="Roboto 20 bold", bg=BackgroundColor, cursor="hand2", bd=0,
               relief=FLAT, activebackground=BackgroundColor, command=toSignup)
Login.place(x=150, y=310)
Home_Page.mainloop()
