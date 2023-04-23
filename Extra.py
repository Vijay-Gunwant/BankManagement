# Back Button
Back = Button(text="Back", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
              relief=RAISED, activebackground=ButtonColor, command=toLogin)
Back.place(x=5, y=450)

# Home Button
Home = Button(text="Home", font="Roboto 15 bold", bg=ButtonColor, cursor="hand2",
              relief=RAISED, activebackground=ButtonColor, command=toLogin)
Home.place(x=420, y=450)

def toLogin():
    Home_Page.destroy()
    import LoginPage


def exitHome():
    Home_Page.destroy()