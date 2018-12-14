import tkinter as tk
import csv
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import carsMenuUi
from services import findCar

class CarsSearchUi(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#5A6D7C")
        screen_width = self.winfo_screenwidth() #Gets the screen width
        screen_height = self.winfo_screenheight() #Gets the screen height
        self.winfo_toplevel().configure(bg="#5A6D7C") # Changes background color of frame
        self.winfo_toplevel().geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame
    
        #Create Labels
        bilaleigaTinna = tk.Label(self, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
        label1 = tk.Label(self, text="Bílar",bg="#5A6D7C",fg="white")
        line1 = tk.Label(self, text="_____________________________",bg="#5A6D7C",fg="white")
        self.car = tk.Label(self, text="Sláðu inn bílnúmer:",bg="#5A6D7C",fg="white")
        line2 = tk.Label(self, text="_____________________________",bg="#5A6D7C",fg="white")

        self.leftFrame = tk.Frame(self, bg="#5A6D7C")
        self.leftFrame.grid(row=4,column=1, columnspan=2)

        self.rightFrame=tk.Frame(self, bg="#5A6D7C")
        self.rightFrame.grid(row=4,column=5, columnspan=2)

        #Create the entry fields
        self.carInput = tk.Entry(self, width=20, font=("Courier", 20))
        #Create Buttons
        escape_button = tk.Button(self, text="Esc - Til baka", bg="#9E4848", fg="white", width=15, height=1, command=lambda: esc(controller))
        confirm_button = tk.Button(self, text="Staðfesta", bg="#448F42", fg="white", width=15, height=1, command=lambda:confirm(self,controller))


        #configure labels
        bilaleigaTinna.config(font=("Courier", 32))
        label1.config(font=("Courier", 28))
        escape_button.config(font=("Courier", 16))
        confirm_button.config(font=("Courier", 16))
        line1.config(font=("Courier", 28))
        line2.config(font=("Courier", 28))
        self.car.config(font=("Courier", 16))
        self.carInput.config(font=("Courier", 16))


        #Position widgets
        bilaleigaTinna.grid(row=1, column=0,columnspan = 8)
        label1.grid(row=3, column=0,columnspan = 8)
        self.car.grid(row=4, column=1)
        line1.grid(row=2,column=0,columnspan = 8)
        line2.grid(row=9,column=0,columnspan = 8)
        self.carInput.grid(row=4, column=4,columnspan = 1)
        escape_button.grid(row=10, column=1)
        confirm_button.grid(row=10, column=4)

        
        #position frame
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(3, weight=1)
        
        self.grid_rowconfigure(8, weight=1)

        self.grid_rowconfigure(11, weight=1)
        self.grid_rowconfigure(9, weight=1)

        self.grid_rowconfigure(12, weight=3)


        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(7, weight=1)


        def esc(self):
            controller.show_frame(carsMenuUi.CarsMenuUi)

        def confirm(self,controller):
            # Search for car then change the frame to see info about the car #
            carInput = self.carInput.get()
            self.instance = findCar.FindCar(carInput)
            self.car.grid_forget()
            escape_button.grid_forget()
            confirm_button.grid_forget()
            self.carInput.grid_forget()
            self.back_button = tk.Button(self, text="Esc - Til baka", bg="#9E4848", fg="white", width=15, height=1, command=lambda: back(self,controller))
            self.delete_button = tk.Button(self, text="Eyða", bg="#9E4848", fg="white", width=15, height=1, command=lambda: back(self,controller))
            self.edit_button = tk.Button(self, text="Breyta/Uppfæra", bg="#448F42", fg="white", width=15, height=1, command=lambda:back(self,controller))
            self.back_button.config(font=("Courier", 16))
            self.delete_button.config(font=("Courier", 16))
            self.edit_button.config(font=("Courier", 16))
            self.back_button.grid(row=10, column=1,columnspan=1)
            self.delete_button.grid(row=10, column=5,columnspan=1)
            self.edit_button.grid(row=10, column=4,columnspan=1)
            self.showCarNameLabel = tk.Label(self.leftFrame, text="Bíll")
            self.showCarModelLabel = tk.Label(self.rightFrame, text="Árgerð")
            self.showCarLicenseLabel = tk.Label(self.leftFrame, text="Bílnúmer")
            self.showCarSeatsLabel = tk.Label(self.rightFrame, text="Fjöldi sæta")
            
            self.showCarName = tk.Label(self.leftFrame, text=self.instance.car[1][1])
            self.showCarModel = tk.Label(self.rightFrame, text=self.instance.car[1][2])
            self.showCarLicense = tk.Label(self.leftFrame, text=self.instance.car[0])
            self.showCarSeats = tk.Label(self.rightFrame, text=self.instance.car[1][3])

            self.showCarNameLabel.config(font=("Courier", 22), bg="#5A6D7C", fg="white")
            self.showCarModelLabel.config(font=("Courier", 22), bg="#5A6D7C", fg="white")
            self.showCarLicenseLabel.config(font=("Courier", 22), bg="#5A6D7C", fg="white")
            self.showCarSeatsLabel.config(font=("Courier", 22), bg="#5A6D7C", fg="white")

            self.showCarNameLabel.grid(row=0, column=0, columnspan=3, pady=10)
            self.showCarModelLabel.grid(row=0, column=0, columnspan=3, pady=10)
            self.showCarLicenseLabel.grid(row=3, column=0, columnspan=3, pady=10)
            self.showCarSeatsLabel.grid(row=3, column=0, columnspan=3, pady=10)
            
            self.showCarName.config(font=("Courier", 16), bg="#5A6D7C", fg="white")
            self.showCarModel.config(font=("Courier", 16), bg="#5A6D7C", fg="white")
            self.showCarLicense.config(font=("Courier", 16), bg="#5A6D7C", fg="white")
            self.showCarSeats.config(font=("Courier", 16), bg="#5A6D7C", fg="white")

            self.showCarName.grid(row=1, column=0, columnspan=3)
            self.showCarModel.grid(row=1, column=0, columnspan=3)
            self.showCarLicense.grid(row=4, column=0, columnspan=3)
            self.showCarSeats.grid(row=4, column=0, columnspan=3)


            # cars_dictionary[licenseplate] = (typef,brand,model,seats)
        def back(self,controller):
            self.back_button.grid_forget()
            self.delete_button.grid_forget()
            self.edit_button.grid_forget()
            self.showCarName.grid_forget()
            self.showCarModel.grid_forget()
            self.showCarLicense.grid_forget()
            self.showCarSeats.grid_forget()

            self.showCarNameLabel.grid_forget()
            self.showCarModelLabel.grid_forget()
            self.showCarLicenseLabel.grid_forget()
            self.showCarSeatsLabel.grid_forget()

            self.car.grid(row=4, column=1)
            self.carInput.grid(row=4, column=4,columnspan = 1)
            escape_button.grid(row=10, column=1)
            confirm_button.grid(row=10, column=4)