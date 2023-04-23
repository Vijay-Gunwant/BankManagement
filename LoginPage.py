from tkinter import *
import mysql.connector as mysql
from tkinter import messagebox


def toHome(Login):
    Login.destroy()
    from HomePage import Home_Creator
    Home_Creator()


def toResetPage(Login):
    Login.destroy()
    from ForgotPassword import Reset_Creator
    Reset_Creator()


def checkLogin(Login_Page, AccNoTextField, PasswordTextField):
    AccNo = AccNoTextField.get()
    Password = PasswordTextField.get()
    if AccNo == "" or Password == "":
        messagebox.showerror("Empty Values", "Please Enter Values")
    else:
        con = mysql.connect(host="localhost", user="root", password="vijay@1234", database="bank")
        cursor = con.cursor()
        cursor.execute("SELECT Acc,Password FROM customer")
        result = cursor.fetchall()
        if result:
            for x in result:
                if AccNo == str(x[0]) and Password == str(x[1]):
                    messagebox.showinfo("Process Successful", "Login Was Successful!")
                    Login_Page.destroy()
                    from Menu import Options_Creator
                    Options_Creator(x[0])
                    return
        messagebox.showerror("Invalid Details", "Invalid AccNo/Password")


def Login_Create():
    BackgroundColor = "#c6cdcf"
    ButtonColor = "#c8dbde"
    Login_Page = Tk()
    # Window Setting
    Login_Page.geometry("500x500")
    Login_Page.resizable(False, False)
    Login_Page.title("Realities Bank - Login Page")
    Login_Page.iconbitmap("./Images/bank.ico")
    Login_Page.config(bg=BackgroundColor)

    # Logo Of Bank
    logo = PhotoImage(file="Images/BankLogo.png")
    BankLogo = Label(image=logo, bg=BackgroundColor)
    BankLogo.place(x=30, y=0)

    # AccNo Label
    AccNoLabel = Label(text="Account Number", font="Roboto 15 bold", bg=BackgroundColor)
    AccNoLabel.place(x=100, y=150)
    AccNoTextField = Entry(Login_Page, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3)
    AccNoTextField.place(x=102, y=180)

    # Password Label
    PasswordLabel = Label(text="Password", font="Roboto 15 bold", bg=BackgroundColor)
    PasswordLabel.place(x=100, y=220)
    PasswordTextField = Entry(Login_Page, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3, show="*")
    PasswordTextField.place(x=102, y=250)

    # Forgot Password
    ForgotPasswordLabel = Button(text="Forgot Password?", font="Roboto 10 bold", bg=BackgroundColor,
                                 cursor="hand2",
                                 bd=0, activebackground=BackgroundColor, activeforeground="firebrick1",
                                 command=lambda: toResetPage(Login_Page))
    ForgotPasswordLabel.place(x=265, y=283)

    # Submit Button
    Submit = Button(text="Login", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
                    relief=RAISED, width=15, activebackground=ButtonColor,
                    command=lambda: checkLogin(Login_Page, AccNoTextField, PasswordTextField))
    Submit.place(x=145, y=330)

    # Back Button
    Back = Button(text="Back", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
                  relief=RAISED, activebackground=ButtonColor, command=lambda: toHome(Login_Page))
    Back.place(x=5, y=450)
    Login_Page.mainloop()
