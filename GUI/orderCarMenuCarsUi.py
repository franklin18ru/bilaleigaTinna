import tkinter as tk
import csv
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from services import makeOrder
import orderCarDateUi
from GUI import mainUi



class OrderCarMenuCarsUi(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#5A6D7C")
        screen_width = self.winfo_screenwidth() #Gets the screen width
        screen_height = self.winfo_screenheight() #Gets the screen height
        self.winfo_toplevel().configure(bg="#5A6D7C") # Changes background color of frame
        self.winfo_toplevel().geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame
    

        #Create labels
        bilaleigaTinna = tk.Label(self, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
        label2 = tk.Label(self, text="Bílar",bg="#5A6D7C",fg="white") #setting the default value as Bílar
        #label2.config(text="Jeppar") #changing the default value to what the user selected on the site before
        line1 = tk.Label(self, text="____________________________",bg="#5A6D7C",fg="white")
        line2 = tk.Label(self, text="____________________________",bg="#5A6D7C",fg="white")
        #Creating button and putting in a function in command
        back = tk.Button(self, text="Esc - Til baka", bg="#C8C8C8", fg="black", width=18, height=1)
        testButton = tk.Button(self, text="test", bg="#C8C8C8", fg="black", width=18, height=1, command=lambda:self.showCars(controller))
        
        #configure labels
        bilaleigaTinna.config(font=("Courier", 32))
        back.config(font=("Courier",16))
        line1.config(font=("Courier", 28))
        line2.config(font=("Courier", 28))
        label2.config(font=("Courier", 26))

        # positioning everything on the screen
        bilaleigaTinna.grid(row=1, column=3)
        label2.grid(row=3,column=3)
        testButton.grid(row=8, column=3)
        back.grid(row=10, column=3)
        line1.grid(row=2,column=3)
        line2.grid(row=9,column=3)
        
        # position frame
        self.grid_rowconfigure(0, weight=3)     #Spaces inbetween rows
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(5, weight=2)
        self.grid_rowconfigure(9, weight=2)
        self.grid_rowconfigure(11, weight=5)

        self.grid_columnconfigure(0, weight=10) #Spaces inbetween columns
        self.grid_columnconfigure(6, weight=10)
        