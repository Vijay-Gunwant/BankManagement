# Tkinter is used to develop this project
import tkinter
from tkinter import *
from tkinter import messagebox


def toLogin():
    Login_Page.destroy()
    import HomePage


def checkLogin():
   pass


def toResetPage():
    Login_Page.destroy()
    import ForgotPassword


# Useful Variables
BackgroundColor = "#c6cdcf"
ButtonColor = "#c8dbde"

Login_Page = tkinter.Tk()
# Window Setting
Login_Page.geometry("500x500")
Login_Page.resizable(False, False)
Login_Page.title("Realities Bank - Login Page")
Login_Page.iconphoto(False, PhotoImage(file="./Images/bank.png"))
Login_Page.config(bg=BackgroundColor)

# Logo Of Bank
logo = PhotoImage(file="Images/BankLogo.png")
BankLogo = Label(image=logo, bg=BackgroundColor)
BankLogo.place(x=30, y=0)

# Username Label
UsernameLabel = Label(text="Username", font="Roboto 15 bold", bg=BackgroundColor)
UsernameLabel.place(x=100, y=150)
UserNameTextField = Entry(Login_Page, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3)
UserNameTextField.place(x=102, y=180)

# Password Label
PasswordLabel = Label(text="Password", font="Roboto 15 bold", bg=BackgroundColor)
PasswordLabel.place(x=100, y=220)
PasswordTextField = Entry(Login_Page, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3, show="*")
PasswordTextField.place(x=102, y=250)

# Forgot Password
ForgotPasswordLabel = Button(text="Forgot Password?", font="Roboto 10 bold", bg=BackgroundColor, cursor="hand2",
                             bd=0, activebackground=BackgroundColor, activeforeground="firebrick1", command=toResetPage)
ForgotPasswordLabel.place(x=265, y=283)

# Submit Button
Submit = Button(text="Login", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
                relief=RAISED, width=15, activebackground=ButtonColor, command=checkLogin)
Submit.place(x=145, y=330)

# Back Button
Back = Button(text="Back", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
              relief=RAISED, activebackground=ButtonColor, command=toLogin)
Back.place(x=5, y=450)
Login_Page.mainloop()


