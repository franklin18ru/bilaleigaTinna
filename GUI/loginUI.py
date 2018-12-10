import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import tkinter as tk
import mainUi
import menuUi

from services.login import loginVerification


class LoginUi(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#5A6D7C")
        screen_width = self.winfo_screenwidth() #Gets the screen width
        screen_height = self.winfo_screenheight() #Gets the screen height
        self.winfo_toplevel().configure(bg="#5A6D7C") # Changes background color of frame
        self.winfo_toplevel().geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame
    
        #login frame
        loginFrame1 = tk.Frame(self, bg="#5A6D7C")
        loginFrame2 = tk.Frame(self, bg="#5A6D7C")

        #Create lables
        bilaleigaTinna = tk.Label(self, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
        label1 = tk.Label(self, text="Innskráning",bg="#5A6D7C",fg="white")
        username = tk.Label(loginFrame1, text="Starfsnúmer:",bg="#5A6D7C",fg="white")
        password = tk.Label(loginFrame2, text="Lykilorð:",bg="#5A6D7C",fg="white")

        #Create Entries
        self.usernameInput = tk.Entry(loginFrame1, width=20, font=("Courier", 20))
        self.passwordInput = tk.Entry(loginFrame2, show="*", width=20, font=("Courier", 20))

        #Configure Lables
        bilaleigaTinna.config(font=("Courier", 32))
        label1.config(font=("Courier", 28))
        username.config(font=("Courier", 22))
        password.config(font=("Courier", 22))

        
        #Show labels
        bilaleigaTinna.pack(side="top",fill="x")
        label1.pack( side="top",fill="x",ipady=100)

        #show loginframes
        loginFrame1.pack(fill="x",side="top")
        loginFrame2.pack(fill="x",side="top")

        #Show username and input
        username.pack(side="top",fill="x")
        self.usernameInput.pack(side="top")

        #show password and input
        password.pack(side="top", fill="x")
        self.passwordInput.pack(side="top")
        
        #Create buttons
        confirm = tk.Button(self, text="Innskrá", bg="#424242", fg="white", width=8, height=1,font=("Courier",16), command=lambda:self.verifyButton(controller))
        confirm.pack(side="top", pady="20",ipadx="105")

    def verifyButton(self, controller):
        usernameInput = int(self.usernameInput.get())
        passwordInput = self.passwordInput.get()
        self.passwordInput.delete(0, "end")
        self.usernameInput.delete(0, "end")
        verifyLogin = loginVerification(usernameInput,passwordInput)
        verification = verifyLogin.verify()
        if verification == False:
            try:
                self.error.destroy()
                self.error = tk.Label(self, text="Rangt starfsnúmer eða lykilorð", bg="red", fg="white",font=("Courier",14))
                self.error.pack()
            except Exception:
                self.error = tk.Label(self, text="Rangt starfsnúmer eða lykilorð", bg="red", fg="white",font=("Courier",14))
                self.error.pack()
        elif verification == True:
            try:
                self.error.destroy()
                controller.show_frame(menuUi.MenuUi)
            except Exception:
                controller.show_frame(menuUi.MenuUi)