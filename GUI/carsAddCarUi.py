import tkinter as tk
import csv
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import carsMenuUi
from services import addCar



class CarsAddCarUi(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#5A6D7C")
        screen_width = self.winfo_screenwidth() #Gets the screen width
        screen_height = self.winfo_screenheight() #Gets the screen height
        self.winfo_toplevel().configure(bg="#5A6D7C") # Changes background color of frame
        self.winfo_toplevel().geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame
    


        bilaleigaTinna = tk.Label(self, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white") 
        label1 = tk.Label(self, text="Bæta við bíl",bg="#5A6D7C",fg="white")
        line1 = tk.Label(self, text="_____________________________",bg="#5A6D7C",fg="white")
        car_type = tk.Label(self, text="Tegund bíls:",bg="#5A6D7C",fg="white")
        brand = tk.Label(self, text="Framleiðandi:",bg="#5A6D7C",fg="white")
        model = tk.Label(self, text="Árgerð:",bg="#5A6D7C",fg="white")
        seats = tk.Label(self, text="Sæti",bg="#5A6D7C",fg="white")
        licenseplate = tk.Label(self, text="Bílnúmer:",bg="#5A6D7C",fg="white")
        line2 = tk.Label(self, text="_____________________________",bg="#5A6D7C",fg="white")



        # Create a Tkinter variable
        self.tkvar =tk.StringVar()

        # Dictionary with options
        
        choices = ['Smabill','Jeppi','Folksbill','Luxusbill']
        self.tkvar.set('Smabill') # set the default option

        #Create the entry fields
        car_typeInput = tk.OptionMenu(self, self.tkvar, *choices, command=self.dc) #creating a dropdown menu
        #car_typeInput = tk.Entry(self, width=20, font=("Courier", 20))
        self.brandInput = tk.Entry(self, width=20, font=("Courier", 20))
        self.modelInput = tk.Entry(self, width=20, font=("Courier", 20))
        self.seatsInput = tk.Entry(self, width=20, font=("Courier", 20))
        self.licenseplateInput = tk.Entry(self, width=20, font=("Courier", 20))







        #Create Buttons
        escape_button = tk.Button(self, text="Esc - Til baka", bg="#9E4848", fg="white", width=15, height=1,command=lambda: self.esc(controller))
        confirm_button = tk.Button(self, text="Staðfesta", bg="#448F42", fg="white", width=15, height=1, command=lambda: self.confirm(controller))





        #configure labels
        bilaleigaTinna.config(font=("Courier", 32))
        label1.config(font=("Courier", 28))
        escape_button.config(font=("Courier", 16))
        confirm_button.config(font=("Courier", 16))
        line1.config(font=("Courier", 28))
        line2.config(font=("Courier", 28))
        car_type.config(font=("Courier", 16))
        brand.config(font=("Courier", 16))
        model.config(font=("Courier", 16))
        seats.config(font=("Courier", 16))
        licenseplate.config(font=("Courier", 16))



        #Position widgets

        #labels
        bilaleigaTinna.grid(row=1, column=0,columnspan = 8)
        label1.grid(row=3, column=0,columnspan = 8)
        car_type.grid(row=4, column=1)
        brand.grid(row=5, column=1)
        model.grid(row=6, column=1)
        seats.grid(row=7, column=1) #added email
        licenseplate.grid(row=8, column=1) #added phone number
        escape_button.grid(row=10, column=1)
        confirm_button.grid(row=10, column=3)
        line1.grid(row=2,column=0,columnspan = 8)
        line2.grid(row=9,column=0,columnspan = 8)
        car_typeInput.grid(row=4, column=2)
        self.brandInput.grid(row=5, column=2)
        self.modelInput.grid(row=6, column=2)
        self.seatsInput.grid(row=7, column=2)
        self.licenseplateInput.grid(row=8, column=2)


       #position frame
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_rowconfigure(8, weight=1)

        self.grid_rowconfigure(11, weight=1)
        self.grid_rowconfigure(9, weight=1)

        self.grid_rowconfigure(12, weight=3)



        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(7, weight=2)

        
        
    def esc(self, controller):
        controller.show_frame(carsMenuUi.CarsMenuUi) #returns user back to the menu page

    def dc(self, value): #fetches value from the drop down menu
        self.value = value 

    def confirm(self,controller): #adds all the user input to the csv file and then returns the user to the menu again
        typeinput = self.value
        brandinput = self.brandInput.get()
        modelinput = self.modelInput.get()
        seatsinput = self.seatsInput.get()
        licenseplateinput = self.licenseplateInput.get()
        self.instance = addCar.AddCar(licenseplateinput,typeinput,brandinput,modelinput,seatsinput)
        self.brandInput.delete(0,"end")
        self.modelInput.delete(0,"end")
        self.seatsInput.delete(0,"end")
        self.licenseplateInput.delete(0,"end")
        controller.show_frame(carsMenuUi.CarsMenuUi)