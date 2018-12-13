import tkinter as tk
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


        infoFrame = tk.Frame(self,bg="black")

        bilaleigaTinna = tk.Label(self, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
        label1 = tk.Label(self, text="Skila bíl",bg="#5A6D7C",fg="white")
        line1 = tk.Label(self, text="____________________________",bg="#5A6D7C",fg="white")
        license_plate = tk.Label(self, text="Sláðu inn bílnúmer:",bg="#5A6D7C",fg="white")
        line2 = tk.Label(self, text="____________________________",bg="#5A6D7C",fg="white")



        #Create the entry fields
        self.license_plateInput = tk.Entry(self, width=20, font=("Courier", 20))



        #Create Buttons
        escape_button = tk.Button(self, text="Esc - Til baka", bg="#9E4848", fg="white", width=15, height=1, command=lambda: esc(controller))
        confirm_button = tk.Button(self, text="Staðfesta", bg="#448F42", fg="white", width=15, height=1, command=lambda: getCarByLicensePlate(self,controller))





        #configure tk.labels
        bilaleigaTinna.config(font=("Courier", 32))
        label1.config(font=("Courier", 28))
        escape_button.config(font=("Courier", 16))
        confirm_button.config(font=("Courier", 16))
        line1.config(font=("Courier", 28))
        line2.config(font=("Courier", 28))
        license_plate.config(font=("Courier", 16))



        #Position widgets

        #tk.labels
        bilaleigaTinna.grid(row=1, column=3)
        label1.grid(row=3, column=3)
        license_plate.grid(row=5, column=2)
        infoFrame.grid(row=5,column=2)
        escape_button.grid(row=10, column=0, columnspan=10)
        confirm_button.grid(row=10, column=4)
        line1.grid(row=2,column=3)
        line2.grid(row=9,column=3)

        self.license_plateInput.grid(row=5, column=3)


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
        #self.grid_columnconfigure(1, weight=50)
        self.grid_columnconfigure(6, weight=10)

        def esc(self):
            controller.show_frame(menuUi.MenuUi)
        
        def getCarByLicensePlate(self,controller):
            licensePlate = self.license_plateInput.get()
            returnCar = returnOrder.ReturnOrder(licensePlate)
            label1.grid_forget()
            license_plate.grid_forget()
            self.license_plateInput.grid_forget()
            controller.returnCarOrder(returnCar)
            renter = tk.Label(infoFrame, text="Leigjandi",bg="#3F4A52",fg="white")
            car = tk.Label(infoFrame, text="Bíll",bg="#3F4A52",fg="white")
            return_button = tk.Button(self, text="Skila", bg="#448F42", fg="white", width=15, height=1, command=lambda: returnCarButton(self,controller))
            renter.pack()
            car.pack()
            return_button.pack()
            # birta retrunCarReturnUi med alla taka og allt ;)#
            # controller.show_frame(returnCarReturnUi.ReturnCarReturnUi)
            
        def returnCarButton(self,controller):
            controller.carReturn.returnCar()
            controller.show_frame(menuUi.MenuUi)


