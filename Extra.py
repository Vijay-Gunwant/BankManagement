# Tkinter is used to develop this project
import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql


class ForgotPassword:
    BackgroundColor = "#c6cdcf"
    ButtonColor = "#c8dbde"
    Forgot_Password = tkinter.Tk()
    Security_CodeTextField = Entry(Forgot_Password, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3)
    Confirm_PasswordTextField = Entry(Forgot_Password, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3, show="*")
    PasswordTextField = Entry(Forgot_Password, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3, show="*")

    def toLogin(self):
        self.Forgot_Password.destroy()
        from LoginPage import LoginPage
        LoginPage()

    def changePass(self):
        if self.Security_CodeTextField.get() == "0000":
            if self.PasswordTextField.get() == self.Confirm_PasswordTextField.get():
                con = mysql.connect(host="localhost", user="root", password="vijay@1234", database="bank")
                cursor = con.cursor()
                cursor.execute("")
                messagebox.showinfo("Password Changed", "Your Password is Changed")
            else:
                messagebox.showerror("Values Not Match", "Confirm Password is not as same as Password")
        else:
            messagebox.showerror("Security Code Error", "Please Enter Correct Security Code")
        self.Forgot_Password.destroy()
        from LoginPage import LoginPage
        LoginPage()

    def __init__(self):
        # Window Setting
        self.Forgot_Password.geometry("500x500")
        self.Forgot_Password.resizable(False, False)
        self.Forgot_Password.title("Realities Bank - Change Password")
        self.Forgot_Password.iconphoto(False, PhotoImage(file="./Images/bank.png"))
        self.Forgot_Password.config(bg=self.BackgroundColor)

        # Logo Of Bank
        logo = PhotoImage(file="Images/BankLogo.png")
        BankLogo = Label(image=logo, bg=self.BackgroundColor)
        BankLogo.place(x=30, y=0)

        # Security Code Label
        Security_CodeLabel = Label(text="Security Code", font="Roboto 15 bold", bg=self.BackgroundColor)
        Security_CodeLabel.place(x=100, y=150)
        self.Security_CodeTextField.place(x=102, y=180)

        # Password Label
        PasswordLabel = Label(text="Password", font="Roboto 15 bold", bg=self.BackgroundColor)
        PasswordLabel.place(x=100, y=220)
        self.PasswordTextField.place(x=102, y=250)

        # Confirm Password Label
        Confirm_PasswordLabel = Label(text="Confirm Password", font="Roboto 15 bold", bg=self.BackgroundColor)
        Confirm_PasswordLabel.place(x=100, y=290)

        self.Confirm_PasswordTextField.place(x=102, y=320)

        # Submit Button
        Submit = Button(text="Reset Password", font="Roboto 15 bold", bg=self.ButtonColor, cursor="hand2",
                        relief=RAISED, width=15, activebackground=self.ButtonColor, command=self.changePass)
        Submit.place(x=145, y=370)

        # Back Button
        Back = Button(text="Back", font="Roboto 15 bold", cursor="hand2", relief=RAISED,
                      activebackground=self.BackgroundColor, command=self.toLogin)
        Back.place(x=5, y=450)
        self.Forgot_Password.mainloop()


ForgotPassword()
