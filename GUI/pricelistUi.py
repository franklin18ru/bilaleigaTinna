import tkinter as tk
import csv
class PriceListUi(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#5A6D7C")
        screen_width = self.winfo_screenwidth() #Gets the screen width
        screen_height = self.winfo_screenheight() #Gets the screen height
        self.winfo_toplevel().configure(bg="#5A6D7C") # Changes background color of frame
        self.winfo_toplevel().geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame

        bilaleigaTinna = tk.Label(self, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
        label1 = tk.Label(self, text="Verðskrá",bg="#5A6D7C",fg="white")
        label2 = tk.Label(self,
                        #text="",
                        bd=4,
                        bg="#5A6D7C",
                        relief="ridge",
                        #font="Times 32",
                        width=90,
                        height=20)

<<<<<<< HEAD
root.title("Pantanir")
screen_width = root.winfo_screenwidth() #Gets the screen width
screen_height = root.winfo_screenheight() #Gets the screen height
root.configure(bg="#5A67C") # Changes background color of frame
root.geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame
=======
        line1 = tk.Label(self, text="____________________________",bg="#5A6D7C",fg="white")
        line2 = tk.Label(self, text="____________________________",bg="#5A6D7C",fg="white")
>>>>>>> a5feac545581284a6c672c2610b7099de8dbed99





        #Create Buttons
        edit = tk.Button(self, text="Edit", bg="white", fg="black", width=15, height=1)


        #configure labels
        bilaleigaTinna.config(font=("Courier", 32))
        label1.config(font=("Courier", 28))
        line1.config(font=("Courier", 28))
        line2.config(font=("Courier", 28))
        edit.config( font=("Courier", 16))




        #Position widgets

        #labels
        bilaleigaTinna.grid(row=1, column=3)
        label1.grid(row=3, column=3)
        label2.grid(row=7, column=3)
        line1.grid(row=2,column=3)
        line2.grid(row=10,column=3)
        edit.grid(row=9, column= 3)




        #position frame
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(11, weight=2)
        self.grid_rowconfigure(9, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(7, weight=1)
