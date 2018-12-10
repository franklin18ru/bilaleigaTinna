import tkinter as tk


class OrderCarCustomerInfoUi(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#5A6D7C")
        screen_width = self.winfo_screenwidth() #Gets the screen width
        screen_height = self.winfo_screenheight() #Gets the screen height
        self.winfo_toplevel().configure(bg="#5A6D7C") # Changes background color of frame
        self.winfo_toplevel().geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame
    


        bilaleigaTinna = tk.Label(self, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
        label1 = tk.Label(self, text="Viðskiptavinur",bg="#5A6D7C",fg="white")
        line1 = tk.Label(self, text="____________________________",bg="#5A6D7C",fg="white")
        full_name = tk.Label(self, text="Fullt nafn:",bg="#5A6D7C",fg="white")
        ssn = tk.Label(self, text="Kennitala:",bg="#5A6D7C",fg="white")
        country = tk.Label(self, text="Land:",bg="#5A6D7C",fg="white")
        email = tk.Label(self, text="Netfang:",bg="#5A6D7C",fg="white")
        phone = tk.Label(self, text="Símanúmer:",bg="#5A6D7C",fg="white")
        line2 = tk.Label(self, text="____________________________",bg="#5A6D7C",fg="white")






        #Create the entry fields
        fullnameInput = tk.Entry(self, width=20, font=("Courier", 20))
        ssnInput = tk.Entry(self, width=20, font=("Courier", 20))
        countryInput = tk.Entry(self, width=20, font=("Courier", 20))
        emailInput = tk.Entry(self, width=20, font=("Courier", 20))
        phoneInput = tk.Entry(self, width=20, font=("Courier", 20))







        #Create Buttons
        escape_button = tk.Button(self, text="Esc - Til baka", bg="white", fg="black", width=15, height=1)
        confirm_button = tk.Button(self, text="Staðfesta", bg="white", fg="black", width=15, height=1)





        #configure labels
        bilaleigaTinna.config(font=("Courier", 32))
        label1.config(font=("Courier", 28))
        escape_button.config(font=("Courier", 16))
        confirm_button.config(font=("Courier", 16))
        line1.config(font=("Courier", 28))
        line2.config(font=("Courier", 28))
        full_name.config(font=("Courier", 16))
        ssn.config(font=("Courier", 16))
        country.config(font=("Courier", 16))
        email.config(font=("Courier", 16))
        phone.config(font=("Courier", 16))



        #Position widgets

        #labels
        bilaleigaTinna.grid(row=1, column=3)
        label1.grid(row=3, column=3)
        full_name.grid(row=4, column=2)
        ssn.grid(row=5, column=2)
        country.grid(row=6, column=2)
        email.grid(row=7, column=2) #added email
        phone.grid(row=8, column=2) #added phone number

        escape_button.grid(row=10, column=2)
        confirm_button.grid(row=10, column=4)
        line1.grid(row=2,column=3)
        line2.grid(row=9,column=3)

        fullnameInput.grid(row=4, column=3)
        ssnInput.grid(row=5, column=3)
        countryInput.grid(row=6, column=3)
        emailInput.grid(row=7, column=3)
        phoneInput.grid(row=8, column=3)


        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=2)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_rowconfigure(8, weight=1)
        self.grid_rowconfigure(9, weight=1)
        self.grid_rowconfigure(11, weight=5)

        self.grid_columnconfigure(0, weight=10)
        self.grid_columnconfigure(6, weight=10)