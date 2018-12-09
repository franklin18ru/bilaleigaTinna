# Multi-frame tkinter application v2.3
import os
import sys
import tkinter as tk
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from services.login import loginVerification

class MainUi(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        
        for F in (LoginUi, MenuUi):
            frame = F(container, self)
            self.frames[F] = frame
            
            frame.grid(row = 0, column = 0, sticky="nsew")
        
        self.show_frame(LoginUi)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

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
        self.usernameInput = int(self.usernameInput.get())
        self.passwordInput = self.passwordInput.get()
        verifyLogin = loginVerification(self.usernameInput,self.passwordInput)
        verification = verifyLogin.verify()
        if verification == False:
            error = tk.Button(self, text="Rangt starfsnúmer eða lykilorð", bg="red", fg="white",font=("Courier",14))
            error.pack()
        if verification == True:
            controller.show_frame(MenuUi)

        

class MenuUi(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#5A6D7C")
        #create frame

        #Create labels
        bilaleigaTinna = tk.Label(self, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
        label1 = tk.Label(self, text="Valmynd",bg="#5A6D7C",fg="white")
        line1 = tk.Label(self, text="____________________________",bg="#5A6D7C",fg="white")
        line2 = tk.Label(self, text="____________________________",bg="#5A6D7C",fg="white")

        #Create buttons
        order_car = tk.Button(self,    text="1. Panta bíl", bg="#424242", fg="white", width=22, height=2)
        return_car = Button(root,   text="2. Skila bíl", bg="#424242", fg="white", width=22, height=2)
        orders = Button(root,       text="3. Pantanir", bg="#424242", fg="white", width=22, height=2)
        prices = Button(root,       text="4. Verðskrá", bg="#424242", fg="white", width=22, height=2)
        cars = Button(root,         text="5. Bílar", bg="#424242", fg="white", width=22, height=2)
        customers = Button(root,    text="6. Viðskiptavinir", bg="#424242", fg="white", width=22, height=2)
        back = Button(root,         text="Esc - Til baka", bg="#C8C8C8", fg="black", width=18, height=1)

        #################################################################################

        #configure labels
        bilaleigaTinna.config(font=("Courier", 32))
        label1.config(font=("Courier", 24))
        order_car.config( font=("Courier",16))
        return_car.config( font=("Courier",16))
        orders.config( font=("Courier",16))
        prices.config( font=("Courier",16))
        cars.config( font=("Courier",16))
        customers.config( font=("Courier",16))
        back.config(font=("Courier",16))
        line1.config(font=("Courier", 28))
        line2.config(font=("Courier", 28))


        #Position widgets

        #labels
        bilaleigaTinna.grid(row=1, column=3)
        label1.grid(row=3, column=3)
        order_car.grid(row=4, column=2)
        return_car.grid(row=4, column=3)
        orders.grid(row=4, column=4)
        prices.grid(row=8, column=2)
        cars.grid(row=8, column=3)
        customers.grid(row=8, column=4)
        back.grid(row=10, column=3)
        line1.grid(row=2,column=3)
        line2.grid(row=9,column=3)



        #position frame
        root.grid_rowconfigure(0, weight=3)
        root.grid_rowconfigure(1, weight=0)
        root.grid_rowconfigure(3, weight=1)
        root.grid_rowconfigure(5, weight=2)
        root.grid_rowconfigure(9, weight=2)
        root.grid_rowconfigure(11, weight=5)
        root.grid_columnconfigure(0, weight=10)
        root.grid_columnconfigure(6, weight=10)


if __name__ == "__main__":
    app = MainUi() 
    app.mainloop()