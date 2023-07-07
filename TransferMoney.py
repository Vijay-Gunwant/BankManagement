import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql


def TransferMoney(Transfer, AccNo, ToAcc, SendAmount):
    if ToAcc == "" or SendAmount == "":
        messagebox.showwarning("Empty Values", "Please Enter Some Valid Values")
        return
    if ToAcc == AccNo:
        messagebox.showwarning("Invalid Transaction", "you Cannot Transfer to Own Account")
        return
    con = mysql.connect(host="localhost", user="root", password="vijay@1234", database="bank")
    cursor = con.cursor()
    cursor.execute(f"SELECT Cash FROM customer WHERE Acc={AccNo};")
    result = cursor.fetchall()
    if float(SendAmount) > int(result[0][0]):
        messagebox.showerror("Less Balance", "Balance is Insufficient")
        return
    cash = float(result[0][0]) - float(SendAmount)
    cursor.execute(f"UPDATE customer SET Cash={cash} WHERE Acc = {AccNo};")
    con.commit()
    cursor.execute("SELECT Acc from customer")
    result = cursor.fetchall()
    for x in result:
        if ToAcc == str(x[0]):
            cursor.execute(f"SELECT Cash FROM customer WHERE Acc={ToAcc};")
            result2 = cursor.fetchall()
            final = float(result2[0][0]) + float(SendAmount)
            cursor.execute(f"UPDATE customer SET Cash={final} WHERE Acc={ToAcc};")
            messagebox.showinfo("Transaction Successful", "Money Transfer Complete")
            con.commit()
            Transfer.destroy()
            Transfer_Creator(AccNo, cash)
            return
    messagebox.showerror("Transfer Failed", "No Such Account Exist")


def toMenu(AccNo, Transfer):
    Transfer.destroy()
    from Menu import Options_Creator
    Options_Creator(AccNo)


def Transfer_Creator(AccNo, Cash):
    BackgroundColor = "#c6cdcf"
    ButtonColor = "#c8dbde"
    Transfer = tkinter.Tk()
    # Window Setting
    Transfer.geometry("500x500")
    Transfer.resizable(False, False)
    Transfer.title("Realities Bank - Change Password")
    Transfer.iconbitmap("./Images/bank.ico")
    Transfer.config(bg=BackgroundColor)

    # Logo Of Bank
    logo = PhotoImage(file="./Images/BankLogo.png")
    BankLogo = Label(Transfer, image=logo, bg=BackgroundColor)
    BankLogo.place(x=30, y=0)

    # Cash Label
    CashLabel = Label(Transfer, text="Balance Amount", font="Roboto 15 bold", bg=BackgroundColor)
    CashLabel.place(x=100, y=150)
    CashTextField = Entry(Transfer, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3)
    CashTextField.insert(0, Cash)
    CashTextField.config(state="disabled")
    CashTextField.place(x=102, y=180)

    # Account Number Label
    AccNoLabel = Label(Transfer, text="Transfer To(Account No.)", font="Roboto 15 bold", bg=BackgroundColor)
    AccNoLabel.place(x=100, y=220)
    AccNoTextField = Entry(Transfer, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3)
    AccNoTextField.place(x=102, y=250)

    # Money Label
    MoneyLabel = Label(Transfer, text="Enter Amount to transfer", font="Roboto 15 bold", bg=BackgroundColor)
    MoneyLabel.place(x=100, y=290)
    MoneyTextField = Entry(Transfer, width=25, relief=SUNKEN, font="Roboto 15 italic", bd=3, )
    MoneyTextField.place(x=102, y=320)

    # Submit Button
    Submit = Button(Transfer, text="Transfer", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
                    relief=RAISED, width=15, activebackground=ButtonColor,
                    command=lambda: TransferMoney(Transfer, AccNo, AccNoTextField.get(), MoneyTextField.get()))
    Submit.place(x=145, y=370)

    # Back Button
    Back = Button(Transfer, text="Back", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2", relief=RAISED,
                  activebackground=BackgroundColor, command=lambda: toMenu(AccNo, Transfer))
    Back.place(x=5, y=450)
    Transfer.mainloop()
