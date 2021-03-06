import tkinter as tk
import menuUi
import carsSearchUi
import carsUi
import carsAddCarUi

class CarsMenuUi(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#5A6D7C")
        screen_width = self.winfo_screenwidth() #Gets the screen width
        screen_height = self.winfo_screenheight() #Gets the screen height
        self.winfo_toplevel().configure(bg="#5A6D7C") # Changes background color of frame
        self.winfo_toplevel().geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame

        bilaleigaTinna = tk.Label(self, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
        label1 = tk.Label(self, text="Bílar",bg="#5A6D7C",fg="white")
        line1 = tk.Label(self, text="_____________________________",bg="#5A6D7C",fg="white")
        line2 = tk.Label(self, text="_____________________________",bg="#5A6D7C",fg="white")

        #Create Buttons
        #Making functions so that the buttons work, returning users to the site they want from the button they click
        search_car = tk.Button(self,    text="1. Leita af bíl", bg="#424242", fg="white", width=22, height=3, command=lambda: switchCarsSearch(controller))
        all_cars = tk.Button(self,   text="2. Allir bílar", bg="#424242", fg="white", width=22, height=3, command=lambda: switchCars(controller))
        add_car = tk.Button(self,text="2. Bæta við bíl", bg="#424242", fg="white", width=22, height=3, command=lambda: switchCarsAddCar(controller))
        escape_button = tk.Button(self, text="Esc - Til baka", bg="#9E4848", fg="white", width=15, height=1, command=lambda: esc(controller))


        #configure labels
        bilaleigaTinna.config(font=("Courier", 32))
        label1.config(font=("Courier", 28))
        search_car.config( font=("Courier",16))
        all_cars.config( font=("Courier",16))
        add_car.config( font =("Courier",16))
        #costomer_allorders.config( font=("Courier",16))
        escape_button.config( font=("Courier", 16))
        line1.config(font=("Courier", 28))
        line2.config(font=("Courier", 28))


        #Position widgets
        bilaleigaTinna.grid(row=1, column=3)
        label1.grid(row=3, column=3)
        search_car.grid(row=4, column=3)
        all_cars.grid(row=5, column=3)
        add_car.grid(row=6, column=3)
        escape_button.grid(row=10, column= 0,columnspan = 4)
        line1.grid(row=2,column=3)
        line2.grid(row=9,column=3)


        #position frame
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(11, weight=1)
        self.grid_rowconfigure(9, weight=1)
        self.grid_rowconfigure(12, weight=3)

        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(7, weight=2)


       

        def esc(self): #returns user back the the main menu page if he clicks on til baka
            controller.show_frame(menuUi.MenuUi)

        def switchCarsSearch(self): #returns user to the carsSearch if he click on leita af bíl
            controller.show_frame(carsSearchUi.CarsSearchUi)

        def switchCars(self): #returns user to cars if he clicks on allir bílar
            controller.show_frame(carsUi.CarsUi)

        def switchCarsAddCar(self): #returns user to carsAddCar if he clicks on bæta við bíl
            controller.show_frame(carsAddCarUi.CarsAddCarUi)


