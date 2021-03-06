import os
import sys
import tkinter as tk
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import loginUi
import mainUi
import orderCarDateUi
import returnCarUi
import ordersUi
import carsMenuUi
import pricelistUi
import customersMenuUi

#ke
class MenuUi(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#5A6D7C")
        #create frame

        #Create labels
        bilaleigaTinna = tk.Label(self, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
        label1 = tk.Label(self, text="Valmynd",bg="#5A6D7C",fg="white")
        line1 = tk.Label(self, text="____________________________",bg="#5A6D7C",fg="white")
        line2 = tk.Label(self, text="____________________________",bg="#5A6D7C",fg="white")

        #Create buttons and commands
        order_car = tk.Button(self,    text="1. Panta bíl", bg="#424242", fg="white", width=22, height=2,  command=lambda: switchOrderCarDate(controller))
        return_car = tk.Button(self,   text="2. Skila bíl", bg="#424242", fg="white", width=22, height=2, command=lambda: switchReturnCar(controller))
        orders = tk.Button(self,       text="3. Pantanir", bg="#424242", fg="white", width=22, height=2,  command=lambda: switchOrders(controller))
        prices = tk.Button(self,       text="4. Verðskrá", bg="#424242", fg="white", width=22, height=2,  command=lambda: switchPrice(controller)) 
        cars = tk.Button(self,         text="5. Bílar", bg="#424242", fg="white", width=22, height=2,     command=lambda: switchCarsMenu(controller))
        customers = tk.Button(self,    text="6. Viðskiptavinir", bg="#424242", fg="white", width=22, height=2, command=lambda: switchCustomersMenu(controller))
        back = tk.Button(self,         text="Útskráning", bg="#9E4848", fg="white", width=15, height=2, command=lambda: logout(controller))

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

        #Positioning everything
        bilaleigaTinna.grid(row=1, column=0,columnspan = 8)
        label1.grid(row=3, column=0, columnspan = 8)
        order_car.grid(row=4, column=0, columnspan = 5)
        return_car.grid(row=4, column=0,columnspan = 8)
        orders.grid(row=4, column=2,columnspan = 5 )
        prices.grid(row=8, column=0, columnspan = 5)
        cars.grid(row=8, column=0, columnspan = 8)
        customers.grid(row=8, column=2, columnspan = 5)
        back.grid(row=0, column=0,columnspan = 1)
        line1.grid(row=2,column=0,columnspan = 8)
        line2.grid(row=9,column=0,columnspan = 8)



        #position frame
        self.grid_rowconfigure(0, weight=0)     #spaces inbetween rows
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(5, weight=2)
        self.grid_rowconfigure(9, weight=2)
        self.grid_rowconfigure(11, weight=5)

        self.grid_columnconfigure(1, weight=10) #spaces inbetween columns
        self.grid_columnconfigure(6, weight=10)
        #Function that takes you to the loginUi site when button is clicked
        def logout(self):
            controller.show_frame(loginUi.LoginUi)
        #Function that takes you to the orderCarDateUi site when button is clicked
        def switchOrderCarDate(self):
            controller.show_frame(orderCarDateUi.OrderCarDateUi)
        #Function that takes you to the returnCarUi site when button is clicked
        def switchReturnCar(self):
            controller.show_frame(returnCarUi.ReturnCarUi)
        #Function that takes you to the ordersUi site when button is clicked
        def switchOrders(self):
            controller.show_frame(ordersUi.OrdersUi)
        #Function that takes you to the carsMenuUi site when button is clicked
        def switchCarsMenu(self):
            controller.show_frame(carsMenuUi.CarsMenuUi)
        #Function that takes you to the pricelistUi site when button is clicked
        def switchPrice(self):
            controller.show_frame(pricelistUi.PriceListUi)
        #Function that takes you to the customersMenuUi site when button is clicked
        def switchCustomersMenu(self):
            controller.show_frame(customersMenuUi.CustomersMenuUi)
