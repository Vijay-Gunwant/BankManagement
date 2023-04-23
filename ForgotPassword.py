# Tkinter is used to develop this project
import tkinter
from tkinter import *
from tkinter import messagebox


def changePass():
    if Security_CodeTextField.get() == "0000":
        if PasswordTextField.get() == Confirm_PasswordTextField.get():
            messagebox.showinfo("Password Changed", "Your Password is Changed")
        else:
            messagebox.showerror("Values Not Match", "Confirm Password is not as same as Password")
    else:
        messagebox.showerror("Security Code Error", "Please Enter Correct Security Code")

    Forgot_Password.destroy()
    import LoginPage


def toLogin():
    Forgot_Password.destroy()
    import LoginPage


# Useful Variables
BackgroundColor = "#c6cdcf"
ButtonColor = "#c8dbde"

Forgot_Password = tkinter.Tk()
# Window Setting
Forgot_Password.geometry("500x500")
Forgot_Password.resizable(False, False)
Forgot_Password.title("Realities Bank - Change Password")
Forgot_Password.iconphoto(False, PhotoImage(file="./Images/bank.png"))
Forgot_Password.config(bg=BackgroundColor)

# Logo Of Bank
logo = PhotoImage(file="Images/BankLogo.png")
BankLogo = Label(image=logo, bg=BackgroundColor)
BankLogo.place(x=30, y=0)

# Security Code Label
Security_CodeLabel = Label(text="Security Code", font="Roboto 15 bold", bg=BackgroundColor)
Security_CodeLabel.place(x=100, y=150)
Security_CodeTextField = Entry(Forgot_Password, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3)
Security_CodeTextField.place(x=102, y=180)

# Password Label
PasswordLabel = Label(text="Password", font="Roboto 15 bold", bg=BackgroundColor)
PasswordLabel.place(x=100, y=220)
PasswordTextField = Entry(Forgot_Password, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3, show="*")
PasswordTextField.place(x=102, y=250)

# Confirm Password Label
Confirm_PasswordLabel = Label(text="Confirm Password", font="Roboto 15 bold", bg=BackgroundColor)
Confirm_PasswordLabel.place(x=100, y=290)
Confirm_PasswordTextField = Entry(Forgot_Password, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3, show="*")
Confirm_PasswordTextField.place(x=102, y=320)

# Submit Button
Submit = Button(text="Reset Password", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
                relief=RAISED, width=15, activebackground=ButtonColor, command=changePass)
Submit.place(x=145, y=370)

# Back Button
Back = Button(text="Back", font="Roboto 15 bold", cursor="hand2",
              relief=RAISED, activebackground=BackgroundColor, command=toLogin)
Back.place(x=5, y=450)
Forgot_Password.mainloop()
