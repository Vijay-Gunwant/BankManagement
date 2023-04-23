# Tkinter is used to develop this project
import tkinter
from tkinter import *


def toHome():
    Menu.destroy()
    import HomePage


# Useful Variables
BackgroundColor = "#c6cdcf"
ButtonColor = "#c8dbde"

Menu = tkinter.Tk()
# Window Setting
Menu.geometry("500x500")
Menu.resizable(False, False)
Menu.title("Realities Bank - Create New Account")
Menu.iconphoto(False, PhotoImage(file="./Images/bank.png"))
Menu.config(bg=BackgroundColor)

# Logo Of Bank
logo = PhotoImage(file="Images/BankLogo.png")
BankLogo = Label(image=logo, bg=BackgroundColor)
BankLogo.place(x=30, y=0)

# Show Info Button
Submit = Button(text="Show Info", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
                relief=RAISED, width=15, activebackground=ButtonColor)
Submit.place(x=145, y=120)
# Update Info Button
Submit = Button(text="Update Info", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
                relief=RAISED, width=15, activebackground=ButtonColor)
Submit.place(x=145, y=170)

# Delete Button
Submit = Button(text="Delete Account", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
                relief=RAISED, width=15, activebackground=ButtonColor)
Submit.place(x=145, y=220)
# Transfer Money Button
Submit = Button(text="Transfer Money", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
                relief=RAISED, width=15, activebackground=ButtonColor)
Submit.place(x=145, y=270)
# Exit Button
Submit = Button(text="Exit", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
                relief=RAISED, width=15, activebackground=ButtonColor)
Submit.place(x=145, y=320)


# Back Button
Back = Button(text="Back", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
              relief=RAISED, activebackground=ButtonColor, command=toHome)
Back.place(x=5, y=450)

Menu.mainloop()
