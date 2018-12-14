import tkinter as tk
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from GUI import mainUi
import orderCarUi
import menuUi
from services import finishOrder

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
        email = tk.Label(self, text="Netfang:",bg="#5A6D7C",fg="white")
        phone = tk.Label(self, text="Símanúmer:",bg="#5A6D7C",fg="white")
        line2 = tk.Label(self, text="____________________________",bg="#5A6D7C",fg="white")






        #Create the entry fields
        self.fullnameInput = tk.Entry(self, width=20, font=("Courier", 20))
        self.ssnInput = tk.Entry(self, width=20, font=("Courier", 20))
        self.emailInput = tk.Entry(self, width=20, font=("Courier", 20))
        self.phoneInput = tk.Entry(self, width=20, font=("Courier", 20))







        #Create Buttons
        escape_button = tk.Button(self, text="Esc - Til baka", bg="#9E4848", fg="white", width=15, height=1, command=lambda: esc(controller))
        confirm_button = tk.Button(self, text="Staðfesta", bg="#448F42", fg="white", width=15, height=1, command=lambda: confirm(self,controller))





        #configure labels
        bilaleigaTinna.config(font=("Courier", 32))
        label1.config(font=("Courier", 28))
        escape_button.config(font=("Courier", 16))
        confirm_button.config(font=("Courier", 16))
        line1.config(font=("Courier", 28))
        line2.config(font=("Courier", 28))
        full_name.config(font=("Courier", 16))
        ssn.config(font=("Courier", 16))
        email.config(font=("Courier", 16))
        phone.config(font=("Courier", 16))



        #Position widgets

        #labels
        bilaleigaTinna.grid(row=1, column=3)
        label1.grid(row=3, column=3)
        full_name.grid(row=4, column=2)
        ssn.grid(row=5, column=2)
        email.grid(row=7, column=2) #added email
        phone.grid(row=8, column=2) #added phone number

        escape_button.grid(row=10, column=2)
        confirm_button.grid(row=10, column=4)
        line1.grid(row=2,column=3)
        line2.grid(row=9,column=3)

        self.fullnameInput.grid(row=4, column=3)
        self.ssnInput.grid(row=5, column=3)
        self.emailInput.grid(row=7, column=3)
        self.phoneInput.grid(row=8, column=3)


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


        def esc(self):
            controller.show_frame(orderCarUi.OrderCarUi)

        def confirm(self,controller):
            self.instance = finishOrder.FinishOrder(controller.car,controller.leaseStart,controller.leaseEnd)
            fullnameinput = self.fullnameInput.get()
            ssninput = self.ssnInput.get()
            emailinput = self.emailInput.get()
            phoneinput = self.phoneInput.get()
            check = self.instance.checkIfCustomerExists(ssninput)
            if not check:
                self.instance.addCostumerToData(fullnameinput,ssninput,emailinput,phoneinput)
            self.instance.addLeaseToData(fullnameinput,ssninput,controller.leaseStart,controller.leaseEnd,self.instance.licensePlate)
            controller.show_frame(menuUi.MenuUi)
        
            
             