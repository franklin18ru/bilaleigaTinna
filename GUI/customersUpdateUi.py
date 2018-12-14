import tkinter as tk
import customersSearchUi
import customersUi


class CustomersUpdateUi(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#5A6D7C")
        screen_width = self.winfo_screenwidth() #Gets the screen width
        screen_height = self.winfo_screenheight() #Gets the screen height
        self.winfo_toplevel().configure(bg="#5A6D7C") # Changes background color of frame
        self.winfo_toplevel().geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame

        bilaleigaTinna = tk.Label(self, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
        line1 = tk.Label(self, text="_______________________________",bg="#5A6D7C",fg="white")
        customer = tk.Label(self, text="Viðskiptavinir",bg="#5A6D7C",fg="white")
        line2 = tk.Label(self, text="_______________________________",bg="#5A6D7C",fg="white")
        name = tk.Label(self, text="Nafn",bg="#5A6D7C",fg="white")
        ssn = tk.Label(self, text="Kennitala",bg="#5A6D7C",fg="white")
        email = tk.Label(self, text="Netfang",bg="#5A6D7C",fg="white")
        phonenr = tk.Label(self, text="Símanúmer",bg="#5A6D7C",fg="white")


        #Entry boxes
        name_entry = tk.Entry(self, width=20, font=("Courier", 20))
        ssn_entry = tk.Entry(self, width=20, font=("Courier", 20))
        email_entry = tk.Entry(self, width=20, font=("Courier", 20))
        phonenr_entry = tk.Entry(self, width=20, font=("Courier", 20))



        #Create Buttons to activate functions that return the users to the page they want
        escape_button = tk.Button(self, text="Esc - Til baka", bg="#9E4848", fg="white", width=15, height=1, command=lambda: esc(controller))
        confirm = tk.Button(self, text="Staðfesta", bg="#448F42", fg="white", width=15, height=1)

        #configure labels
        bilaleigaTinna.config(font=("Courier", 32))
        customer.config(font=("Courier", 28))
        name.config(font=("Courier", 16))
        ssn.config(font=("Courier", 16))
        email.config(font=("Courier", 16))
        phonenr.config(font=("Courier", 16))
        name_entry.config(font=("Courier", 16))
        ssn_entry.config(font=("Courier", 16))
        email_entry.config(font=("Courier", 16))
        phonenr_entry.config(font=("Courier", 16))

        line1.config(font=("Courier", 28))
        line2.config(font=("Courier", 28))
        confirm.config( font=("Courier", 16))
        escape_button.config( font=("Courier", 16))

        #labels
        bilaleigaTinna.grid(row=1, column=0,columnspan = 8)
        line1.grid(row=2, column=0,columnspan = 8)
        customer.grid(row=3, column=0, columnspan=8)
        
        name.grid(row=4, column=0, columnspan=2)
        ssn.grid(row=4, column=1, columnspan=2)
        email.grid(row=4, column=2, columnspan=2)
        phonenr.grid(row=4, column=3, columnspan=2)
        name_entry.grid(row=5, column=0, columnspan=2)
        ssn_entry.grid(row=5, column=1, columnspan=2)
        email_entry.grid(row=5, column=2, columnspan=2)
        phonenr_entry.grid(row=5, column=3, columnspan=2)

        line2.grid(row=10,column =0, columnspan = 8)
        confirm.grid(row=11, column= 2, columnspan = 2 )
        escape_button.grid(row=11, column=0, columnspan = 3)

        #position frame
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(11, weight=1)
        self.grid_rowconfigure(9, weight=1)
        self.grid_rowconfigure(12, weight=3)

        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(7, weight=2)

        
        def esc(self):
            controller.show_frame(customersUi.CustomersUi)
