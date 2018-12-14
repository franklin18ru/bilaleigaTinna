import tkinter as tk
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import menuUi
from services import returnOrder
import returnCarReturnUi


class ReturnCarUi(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#5A6D7C")
        screen_width = self.winfo_screenwidth() #Gets the screen width
        screen_height = self.winfo_screenheight() #Gets the screen height
        self.winfo_toplevel().configure(bg="#5A6D7C") # Changes background color of frame
        self.winfo_toplevel().geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame


        renterFrame = tk.Frame(self, bg="#5A6D7C")
        carFrame = tk.Frame(self, bg="#5A6D7C")


        bilaleigaTinna = tk.Label(self, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
        label1 = tk.Label(self, text="Skila bíl",bg="#5A6D7C",fg="white")
        line1 = tk.Label(self, text="____________________________",bg="#5A6D7C",fg="white")
        license_plate = tk.Label(self, text="Sláðu inn bílnúmer:",bg="#5A6D7C",fg="white")
        line2 = tk.Label(self, text="____________________________",bg="#5A6D7C",fg="white")

        #Create the entry fields
        self.license_plateInput = tk.Entry(self, width=20, font=("Courier", 20))


        #Create Buttons
        back_button = tk.Button(self, text="Esc - Til baka", bg="#9E4848", fg="white", width=15, height=1, command=lambda: esc(controller))
        confirm_button = tk.Button(self, text="Staðfesta", bg="#448F42", fg="white", width=15, height=1, command=lambda: getCarByLicensePlate(self,controller))


        #configure tk.labels
        bilaleigaTinna.config(font=("Courier", 32))
        label1.config(font=("Courier", 28))
        back_button.config(font=("Courier", 16))
        confirm_button.config(font=("Courier", 16))
        line1.config(font=("Courier", 28))
        line2.config(font=("Courier", 28))
        license_plate.config(font=("Courier", 16))

        #Position widgets
        bilaleigaTinna.grid(row=1, column=0, columnspan=8)
        label1.grid(row=3, column=0, columnspan=8)
        license_plate.grid(row=4, column=1) #column = 2
        renterFrame.grid(row=5, column=2)
        carFrame.grid(row=6, column=2)
        back_button.grid(row=10, column=1, columnspan = 1) #column = 0
        confirm_button.grid(row=10, column=5, columnspan=1) #column = 4
        line1.grid(row=2,column=0, columnspan=8)
        line2.grid(row=9,column=0, columnspan=8)

        self.license_plateInput.grid(row=4, column=4, columnspan=1) #column = 3


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
 
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(7, weight=2)

        def esc(self):
            controller.show_frame(menuUi.MenuUi)
        

        def getCarByLicensePlate(self,controller):
            licensePlate = self.license_plateInput.get()
            returnCar = returnOrder.ReturnOrder(licensePlate)
            label1.grid_forget()
            license_plate.grid_forget()
            self.license_plateInput.grid_forget()
            back_button.grid_forget()
            confirm_button.grid_forget()
            controller.returnCarOrder(returnCar)
            self.renter = tk.Label(renterFrame, text="Leigjandi",bg="#5A6D7C",fg="white")
            self.renterName = tk.Label(renterFrame, text="Nafn: "+ returnCar.carOrder[1][0], bg="#5A6D7C", fg="white")
            self.renterSSN = tk.Label(renterFrame, text="Kennitala: "+ str(returnCar.carOrder[0]), bg="#5A6D7C", fg="white")
            self.renter.config(font=("Courier", 32))
            self.renterName.config(font=("Courier", 18))
            self.renterSSN.config(font=("Courier", 18))
            self.car = tk.Label(carFrame, text="Bíll",bg="#5A6D7C",fg="white")
            self.carName = tk.Label(carFrame, text="Tegund Bíls: "+ returnCar.car[1][1], bg="#5A6D7C", fg="white")
            self.carLicensePlate=tk.Label(carFrame, text="Bílnúmer: "+ returnCar.car[0], bg="#5A6D7C", fg="white")
            self.car.config(font=("Courier", 32))
            self.carName.config(font=("Courier", 18))
            self.carLicensePlate.config(font=("Courier", 18))
            
            
            self.return_button = tk.Button(self, text="Skila", bg="#448F42", fg="white", width=15, height=1, command=lambda: returnCarButton(self,controller))
            self.renter.pack()
            self.renterName.pack(side="top")
            self.renterSSN.pack(side="top")
            self.car.pack()
            self.carName.pack(side="top")
            self.carLicensePlate.pack(side="top")
            self.return_button.config(font=("Courier", 16))
            self.return_button.grid(row=10, column=4)
            self.escape_button = tk.Button(self, text="Esc - Til baka", bg="#9E4848", fg="white", width=15, height=1, command=lambda: goBack(self))
            self.escape_button.config(font=("Courier", 16))
            self.escape_button.grid(row=10, column=1)
            # birta retrunCarReturnUi med alla taka og allt ;)#
            # controller.show_frame(returnCarReturnUi.ReturnCarReturnUi)

        def returnCarButton(self,controller):
            controller.carReturn.returnCar()
            self.license_plateInput.delete(0,"end")
            self.renter.pack_forget()
            self.renterName.pack_forget()
            self.renterSSN.pack_forget()
            self.car.pack_forget()
            self.carName.pack_forget()
            self.carLicensePlate.pack_forget()
            self.return_button.grid_forget()
            self.escape_button.grid_forget()
            bilaleigaTinna.grid(row=1, column=0, columnspan=10)
            label1.grid(row=3, column=0, columnspan=10)
            license_plate.grid(row=5, column=1)
            renterFrame.grid(row=5, column=2)
            back_button.grid(row=8, column=1)
            confirm_button.grid(row=8, column=3)
            line1.grid(row=2,column=0, columnspan=10)
            line2.grid(row=7,column=0, columnspan=10)
            self.license_plateInput.grid(row=5, column=2)
            controller.show_frame(menuUi.MenuUi)
            


        def goBack(self):
            #remove information widgets
            self.renter.pack_forget()
            self.renterName.pack_forget()
            self.renterSSN.pack_forget()
            self.car.pack_forget()
            self.carName.pack_forget()
            self.carLicensePlate.pack_forget()
            self.return_button.grid_forget()
            self.escape_button.grid_forget()

            #Add previous widgets to frame
            bilaleigaTinna.grid(row=1, column=0, columnspan=10)
            label1.grid(row=3, column=0, columnspan=10)
            license_plate.grid(row=5, column=1)
            renterFrame.grid(row=5, column=2)
            back_button.grid(row=8, column=1)
            confirm_button.grid(row=8, column=3)
            line1.grid(row=2,column=0, columnspan=10)
            line2.grid(row=7,column=0, columnspan=10)
            self.license_plateInput.grid(row=5, column=2)
            
            self.grid_rowconfigure(0, weight=2)
            self.grid_rowconfigure(2, weight=0)
            self.grid_rowconfigure(1, weight=0)
            self.grid_rowconfigure(4, weight=1)
            self.grid_rowconfigure(3, weight=1)
            self.grid_rowconfigure(8, weight=1)
    
            self.grid_rowconfigure(11, weight=1)
            self.grid_rowconfigure(9, weight=1)
            self.grid_rowconfigure(12, weight=3)
    
            self.grid_columnconfigure(0, weight=2)
            self.grid_columnconfigure(7, weight=2)

            



