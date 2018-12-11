import tkinter as tk
from data_access import carsDataAccess

class OrderCarDateUi(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#5A6D7C")
        screen_width = self.winfo_screenwidth() #Gets the screen width
        screen_height = self.winfo_screenheight() #Gets the screen height
        self.winfo_toplevel().configure(bg="#5A6D7C") # Changes background color of frame
        self.winfo_toplevel().geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame
    
        #Create labels
        bilaleigaTinna = tk.Label(self, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
        label1 = tk.Label(self, text="Velja dagsetningu",bg="#5A6D7C",fg="white")
        line1 = tk.Label(self, text="____________________________",bg="#5A6D7C",fg="white")
        line2 = tk.Label(self, text="____________________________",bg="#5A6D7C",fg="white")
        start = tk.Label(self, text="Til (dd.mm.yyyy): ",bg="#5A6D7C",fg="white")
        end = tk.Label(self, text="Frá (dd.mm.yyyy): ",bg="#5A6D7C",fg="white")

        #Create entry fields
        self.startInput = tk.Entry(self, width=20, font=("Courier", 20)) #input for the date, should be on format 'dd.mm.yyyy'
        self.endInput = tk.Entry(self, width=20, font=("Courier", 20)) #same ^^


        #Create buttons
        back = tk.Button(self, text="Esc - Til baka", bg="#C8C8C8", fg="black", width=18, height=1)
        confirm = tk.Button(self, text="Staðfesta", bg="#C8C8C8", fg="black", width=18, height=1)

        #################################################################################

        #configure labels
        bilaleigaTinna.config(font=("Courier", 32))
        label1.config(font=("Courier", 24))
        start.config(font=("Courier", 24))
        end.config(font=("Courier", 24))
        confirm.config(font=("Courier", 16))
        back.config(font=("Courier",16))
        line1.config(font=("Courier", 28))
        line2.config(font=("Courier", 28))


        #Position widgets

        #positioning everything on the screen
        bilaleigaTinna.grid(row=1, column=3)
        label1.grid(row=3, column=3)
        start.grid(row=4, column=2)
        self.startInput.grid(row=4, column=3)
        end.grid(row=5, column=2)
        self.endInput.grid(row=5, column=3)
        confirm.grid(row=10, column=4)
        back.grid(row=10, column=2)
        line1.grid(row=2,column=3)
        line2.grid(row=9,column=3)
        



        #position frame
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(5, weight=2)
        self.grid_rowconfigure(9, weight=2)
        self.grid_rowconfigure(11, weight=5)
        self.grid_columnconfigure(0, weight=10)
        self.grid_columnconfigure(6, weight=10)

        def getCarsByDate(self):
            startInput = self.startInput.get()
            endInput = self.endInput.get()

            cars = carsDataAccess.CarsDataAccess()
            cars.getAvailableCars(startInput, endInput)
        ################################################################################