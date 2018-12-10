import tkinter as tk

class ReturnCarReturnUi(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#5A6D7C")
        screen_width = self.winfo_screenwidth() #Gets the screen width
        screen_height = self.winfo_screenheight() #Gets the screen height
        self.winfo_toplevel().configure(bg="#5A6D7C") # Changes background color of frame
        self.winfo_toplevel().geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame


        bilaleigaTinna = tk.Label(self, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
        renter = tk.Label(grey_frame, text="Leigjandi",bg="#3F4A52",fg="white")
        line1 = tk.Label(self, text="____________________________",bg="#5A6D7C",fg="white")
        car = tk.Label(grey_frame, text="Bíll",bg="#3F4A52",fg="white")
        line2 = tk.Label(self, text="____________________________",bg="#5A6D7C",fg="white")




        #Create Buttons
        escape_button = tk.Button(self, text="Esc - Til baka", bg="#9E4848", fg="white", width=15, height=1)
        return_button = tk.Button(self, text="Skila", bg="#448F42", fg="white", width=15, height=1)





        #configure labels
        bilaleigaTinna.config(font=("Courier", 32))
        renter.config(font=("Courier", 20))
        escape_button.config(font=("Courier", 16))
        return_button.config(font=("Courier", 16))
        line1.config(font=("Courier", 28))
        line2.config(font=("Courier", 28))
        car.config(font=("Courier", 20))



        #Position widgets

        #labels
        bilaleigaTinna.grid(row=1, column=3)
        renter.grid(row=3, column=3)
        car.grid(row=5, column=3, ipady=30, ipadx=50)

        escape_button.grid(row=10, column=2)
        return_button.grid(row=10, column=4)
        line1.grid(row=2,column=3)
        line2.grid(row=9,column=3)

        grey_frame.grid(row=3, column=3)


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
        self.grid_columnconfigure(3, weight=50)
        self.grid_columnconfigure(6, weight=10)