import tkinter as tk
from mainUi import MainUi


class LoginUi(MainUi):
    def __init__(self,*args,**kwargs):
    #Create labels
        bilaleigaTinna = tk.Label(self, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
        label1 = tk.Label(self, text="Innskráning",bg="#5A6D7C",fg="white")
        username = tk.Label(self, text="Starfsnúmer:",bg="#5A6D7C",fg="white")
        password = tk.Label(self, text="Lykilorð:",bg="#5A6D7C",fg="white")



        #Create the entry fields
        usernameInput = tk.Entry(self, width=20, font=("Courier", 20))
        passwordInput = tk.Entry(self, show="*", width=20, font=("Courier", 20))


        #Create buttons
        confirm = Button(root, text="Innskrá", bg="#424242", fg="white", width=8, height=1,font=("Courier",16), command=verify)
        #################################################################################

        #configure labels
        bilaleigaTinna.config(font=("Courier", 32))
        label1.config(font=("Courier", 28))
        username.config(font=("Courier", 22))
        password.config(font=("Courier", 22))



        # #Position widgets

        #labels
        bilaleigaTinna.grid(row=1, column=2, sticky = NSEW)
        label1.grid(row=3, column=2, sticky = "NSEW")
        username.grid(row=4, column=0, sticky = "E")
        password.grid(row=5, column=0, sticky = "E")

        #Entries
        usernameInput.grid(row=4, column=2)
        passwordInput.grid(row=5, column=2)
        # confirm.grid(row=6, column=2)

        #position frame
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_rowconfigure(9, weight=3)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(9, weight=1)

root = LoginUi()
root.mainloop()