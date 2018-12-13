import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import tkinter as tk
import menuUi
import orderCarDateUi
import orderCarMenuCarsUi
from services import makeOrder
from GUI import mainUi
import orderCarMenuCarsUi
class OrderCarUi(tk.Frame):
#create frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#5A6D7C")
        screen_width = self.winfo_screenwidth() #Gets the screen width
        screen_height = self.winfo_screenheight() #Gets the screen height
        self.winfo_toplevel().configure(bg="#5A6D7C") # Changes background color of frame
        self.winfo_toplevel().geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame

        #Create labels
        bilaleigaTinna = tk.Label(self, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
        label1 = tk.Label(self, text="Panta bíl",bg="#5A6D7C",fg="white")
        line1 = tk.Label(self, text="____________________________",bg="#5A6D7C",fg="white")
        line2 = tk.Label(self, text="____________________________",bg="#5A6D7C",fg="white")
        carFrame = tk.Frame(self,bg="#5A6D7C")
        #Create buttons
        jeep = tk.Button(self, text="1. Jeppar", bg="#424242", fg="white", width=22, height=2,           command=lambda: chooseCar(controller,"Jeppi"))
        small_car = tk.Button(self, text="2. Smábílar", bg="#424242", fg="white", width=22, height=2,    command=lambda: chooseCar(controller,"Smabíll"))
        sedan = tk.Button(self, text="3. Fólksbílar", bg="#424242", fg="white", width=22, height=2,      command=lambda: chooseCar(controller,"Fólksbíll"))
        luxury_car = tk.Button(self, text="4. Lúxurbílar", bg="#424242", fg="white", width=22, height=2, command=lambda: chooseCar(controller,"Lúxusbíll"))
        all_cars = tk.Button(self, text="5. Allir bílar", bg="#424242", fg="white", width=22, height=2,  command=lambda: chooseCar(controller,""))
        back = tk.Button(self, text="Esc - Til baka",bg="#9E4848", fg="white", width=18, height=1,       command=lambda: esc(controller))

        #################################################################################

        #configure labels
        bilaleigaTinna.config(font=("Courier", 32))
        label1.config(font=("Courier", 24))
        jeep.config( font=("Courier",16))
        small_car.config( font=("Courier",16))
        sedan.config( font=("Courier",16))
        luxury_car.config( font=("Courier",16))
        all_cars.config( font=("Courier",16))
        back.config(font=("Courier",16))
        line1.config(font=("Courier", 28))
        line2.config(font=("Courier", 28))


        #Position widgets

        #positioning everything on the screen
        bilaleigaTinna.grid(row=1, column=3)
        label1.grid(row=3, column=3)
        carFrame.grid(row=4, column=0, columnspan=10)
        jeep.grid(row=4, column=2)
        small_car.grid(row=4, column=3)
        sedan.grid(row=4, column=4)
        luxury_car.grid(row=8, column=2)
        all_cars.grid(row=8, column=3)
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


        def esc(self):
            controller.show_frame(orderCarDateUi.OrderCarDateUi)

        def chooseCar(self, carType):
            controller.order.getCarsByType(carType)
            jeep.grid_forget()
            small_car.grid_forget()
            sedan.grid_forget()
            luxury_car.grid_forget()
            all_cars.grid_forget()
            row_num = 4
            column_num = 2
            counter = 0
            for item in controller.order.cars:
                carButton = tk.Button(carFrame, text=item ,bg="#424242",fg="white", width=22, height=2)
                #carButton.pack(side="left")
                carButton.config(font=("Courier", 16))
                # carButton.grid(row = row_num, column=column_num)
                
                carButton.grid(row = row_num, column=column_num)
                counter += 1
                column_num += 1
                if counter == 3:
                    row_num += 1
                    counter = 0
                    column_num = 2 
            # controller.show_frame(orderCarMenuCarsUi.OrderCarMenuCarsUi)
            
            
        #################################################################################
