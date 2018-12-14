# Multi-frame tkinter application v2.3
import os
import sys
import tkinter as tk
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from services.login import loginVerification
import loginUi
import menuUi
import orderCarDateUi
import returnCarUi
import ordersUi
import carsMenuUi
import pricelistUi
import customersUi
import orderCarUi
import orderCarMenuCarsUi
import carsUi
import carsSearchUi
import carsAddCarUi
import returnCarReturnUi
import ordersSearchCustomerUi
import customersUpdateUi
import customersSearchUi
import orderCarCustomerInfoUi
from services import makeOrder


class MainUi(tk.Tk):
    def __init__(self, *args, **kwargs):
        #Creates Frame.
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight = 1) # Rezises frame to the size of your monitor.
        container.grid_columnconfigure(0, weight = 1)
        self.frames = {}
        
        for F in (loginUi.LoginUi, menuUi.MenuUi, orderCarDateUi.OrderCarDateUi, 
                  returnCarUi.ReturnCarUi, ordersUi.OrdersUi, carsMenuUi.CarsMenuUi, customersSearchUi.CustomersSearchUi,
                  pricelistUi.PriceListUi, customersUi.CustomersUi, orderCarUi.OrderCarUi, customersUpdateUi.CustomersUpdateUi,
                  orderCarMenuCarsUi.OrderCarMenuCarsUi, carsUi.CarsUi, ordersSearchCustomerUi.OrdersSearchCustomerUi,
                  carsSearchUi.CarsSearchUi, returnCarReturnUi.ReturnCarReturnUi, carsAddCarUi.CarsAddCarUi,
                  orderCarCustomerInfoUi.OrderCarCustomerInfoUi): #Loops through and creates all frames
                  
            frame = F(container, self)
            self.frames[F] = frame
            
            frame.grid(row = 0, column = 0, sticky="nsew") #Positions the frame
        
        self.show_frame(loginUi.LoginUi)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise() #Displays the frames that's called for.
    
    def createOrder(self, order):
        self.order = order

    def returnCarOrder(self, carReturn):
        self.carReturn = carReturn


    

if __name__ == "__main__":
    app = MainUi() 
    app.mainloop()
