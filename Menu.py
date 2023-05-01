# Tkinter is used to develop this project
import tkinter
from tkinter import *

import mysql.connector as mysql


def toTransfer(Options, AccNo):
    Options.destroy()
    from TransferMoney import Transfer_Creator
    con = mysql.connect(host="localhost", user="root", password="vijay@1234", database="bank")
    cursor = con.cursor()
    cursor.execute(f'SELECT Cash FROM customer WHERE Acc={AccNo}')
    result = cursor.fetchall()
    Transfer_Creator(AccNo, result[0][0])


def toHome(Options):
    Options.destroy()
    from HomePage import Home_Creator
    Home_Creator()


def toAcc(Options, AccNo):
    con = mysql.connect(host="localhost", user="root", password="vijay@1234", database="bank")
    cursor = con.cursor()
    cursor.execute(f'SELECT * FROM customer WHERE Acc={AccNo}')
    result = cursor.fetchall()
    Options.destroy()
    from AccInfo import AccInfo
    AccInfo(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4], result[0][6], result[0][5])


def Options_Creator(AccNo):
    # Useful Variables
    BackgroundColor = "#c6cdcf"
    ButtonColor = "#c8dbde"

    Options = tkinter.Tk()
    # Window Setting
    Options.geometry("500x500")
    Options.resizable(False, False)
    Options.title("Realities Bank - Create New Account")
    Options.iconbitmap("./Images/bank.ico")
    Options.config(bg=BackgroundColor)

    # Logo Of Bank
    logo = PhotoImage(file="Images/BankLogo.png")
    BankLogo = Label(image=logo, bg=BackgroundColor)
    BankLogo.place(x=30, y=0)

    # Show Info Button
    Show = Button(text="Show Info", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
                  relief=RAISED, width=15, activebackground=ButtonColor, command=lambda: toAcc(Options, AccNo))
    Show.place(x=145, y=200)
    # Transaction Info Button
    Transaction = Button(text="Transfer Money", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
                         relief=RAISED, width=15, activebackground=ButtonColor,
                         command=lambda: toTransfer(Options, AccNo))
    Transaction.place(x=145, y=260)
    # Exit Button
    Exit = Button(text="Exit", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
                  relief=RAISED, width=15, activebackground=ButtonColor, command=exit)
    Exit.place(x=145, y=320)

    # Back Button
    Back = Button(text="Back", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
                  relief=RAISED, activebackground=ButtonColor, command=lambda: toHome(Options))
    Back.place(x=5, y=450)

    Options.mainloop()
