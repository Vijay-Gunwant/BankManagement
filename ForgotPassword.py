import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql

def changePass(AccNo,Password,Confirm):

    if AccNo == "" or Password == "" or Confirm == "":
        messagebox.showwarning("Empty Values","Please Enter Some Valid Values")
        return
    con = mysql.connect(host="localhost", user="root", password="vijay@1234", database="bank")
    cursor = con.cursor()
    cursor.execute("SELECT Acc,Password FROM customer")
    result = cursor.fetchall()
    for Acount,Pass in result:
        if AccNo == str(Acount):
            if Password== Confirm:
                cursor.execute(f"UPDATE customer SET Password = '{Password}' where Acc = '{AccNo}'")
                con.commit()
                messagebox.showinfo("Password Changed", "Your Password is Changed")
            else:
                messagebox.showerror("Values Not Match", "Confirm Password is not as same as Password")
        else:
            messagebox.showerror("Security Code Error", "Please Enter Correct Account Number")

def toLogin(Forgot_Password):
    Forgot_Password.destroy()
    from LoginPage import Login_Create
    Login_Create()


def Reset_Creator():
    BackgroundColor = "#c6cdcf"
    ButtonColor = "#c8dbde"
    Forgot_Password = tkinter.Tk()
    # Window Setting
    Forgot_Password.geometry("500x500")
    Forgot_Password.resizable(False, False)
    Forgot_Password.title("Realities Bank - Change Password")
    Forgot_Password.iconbitmap("./Images/bank.ico")
    Forgot_Password.config(bg=BackgroundColor)

    # Logo Of Bank
    logo = PhotoImage(file="./Images/BankLogo.png")
    BankLogo = Label(Forgot_Password,image=logo, bg=BackgroundColor)
    BankLogo.place(x=30, y=0)

    # AccNo Label
    AccNoLabel = Label(Forgot_Password,text="Account Number", font="Roboto 15 bold", bg=BackgroundColor)
    AccNoLabel.place(x=100, y=150)
    AccNoTextField = Entry(Forgot_Password, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3)
    AccNoTextField.place(x=102, y=180)

    # Password Label
    PasswordLabel = Label(Forgot_Password,text="Password", font="Roboto 15 bold", bg=BackgroundColor)
    PasswordLabel.place(x=100, y=220)
    PasswordTextField = Entry(Forgot_Password, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3, show="*")
    PasswordTextField.place(x=102, y=250)

    # Confirm Password Label
    Confirm_PasswordLabel = Label(Forgot_Password,text="Confirm Password", font="Roboto 15 bold", bg=BackgroundColor)
    Confirm_PasswordLabel.place(x=100, y=290)
    Confirm_PasswordTextField = Entry(Forgot_Password, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3,
                                      show="*")
    Confirm_PasswordTextField.place(x=102, y=320)

    # Submit Button
    Submit = Button(Forgot_Password,text="Reset Password", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
                    relief=RAISED, width=15, activebackground=ButtonColor, command=lambda:changePass(AccNoTextField.get(),PasswordTextField.get(),Confirm_PasswordTextField.get()))
    Submit.place(x=145, y=370)

    # Back Button
    Back = Button(Forgot_Password,text="Back", font="Roboto 15 bold", cursor="hand2", relief=RAISED,
                  activebackground=BackgroundColor, command=lambda:toLogin(Forgot_Password))
    Back.place(x=5, y=450)
    Forgot_Password.mainloop()












