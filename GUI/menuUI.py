import tkinter as tk
import os
import sys
import tkinter as tk
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import loginUi
import mainUi
import orderCarUi
import returnCarUi
import ordersUi


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
        order_car = tk.Button(self,    text="1. Panta bíl", bg="#424242", fg="white", width=22, height=2, command=lambda: switchOrderCar(controller))
        return_car = tk.Button(self,   text="2. Skila bíl", bg="#424242", fg="white", width=22, height=2, command=lambda: switchReturnCar(controller))
        orders = tk.Button(self,       text="3. Pantanir", bg="#424242", fg="white", width=22, height=2)
        prices = tk.Button(self,       text="4. Verðskrá", bg="#424242", fg="white", width=22, height=2)
        cars = tk.Button(self,         text="5. Bílar", bg="#424242", fg="white", width=22, height=2)
        customers = tk.Button(self,    text="6. Viðskiptavinir", bg="#424242", fg="white", width=22, height=2)
        back = tk.Button(self,         text="Skrá þig út", bg="#C8C8C8", fg="black", width=18, height=1, command=lambda: logout(controller))

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
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(5, weight=2)
        self.grid_rowconfigure(9, weight=2)
        self.grid_rowconfigure(11, weight=5)
        self.grid_columnconfigure(0, weight=10)
        self.grid_columnconfigure(6, weight=10)

        def logout(self):
            controller.show_frame(loginUi.LoginUi)

        def switchOrderCar(self):
            controller.show_frame(orderCarUi.OrderCarUi)

        def switchReturnCar(self):
            controller.show_frame(returnCarUi.ReturnCarUi)

        def switchOrders(self):
            controller.show_frame(returnCarUi.ReturnCarUi)
        
