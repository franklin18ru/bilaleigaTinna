import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import tkinter as tk
import ordersUi
from services import findOrder


class OrdersSearchCustomerUi(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#5A6D7C")
        screen_width = self.winfo_screenwidth() #Gets the screen width
        screen_height = self.winfo_screenheight() #Gets the screen height
        self.winfo_toplevel().configure(bg="#5A6D7C") # Changes background color of frame
        self.winfo_toplevel().geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame
    

        bilaleigaTinna = tk.Label(self, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
        label1 = tk.Label(self, text="Pantanir",bg="#5A6D7C",fg="white")
        line1 = tk.Label(self, text="____________________________",bg="#5A6D7C",fg="white")

        ssn = tk.Label(self, text="Sláðu inn kennitölu \n eða nafn viðskiptavinar \n eða bílnúmer:",bg="#5A6D7C",fg="white")

        line2 = tk.Label(self, text="____________________________",bg="#5A6D7C",fg="white")






        #Create the entry fields
        self.userInput = tk.Entry(self, width=20, font=("Courier", 20))

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
        ssn.config(font=("Courier", 16))





        #Position widgets

        #labels
        bilaleigaTinna.grid(row=1, column=0,columnspan = 8)
        label1.grid(row=3, column=0,columnspan = 8)
        

        ssn.grid(row=4, column=1)

        #escape_button.grid(row=10, column=3)
        escape_button.grid(row=10, column=1)
        confirm_button.grid(row=10, column=4)
        line1.grid(row=2,column=0,columnspan = 8)
        line2.grid(row=9,column=0,columnspan = 8)

        self.userInput.grid(row=4, column=4,columnspan = 1)




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
            controller.show_frame(ordersUi.OrdersUi)


        def confirm(self,controller):
            userInput = self.userInput.get()
            self.instance = findOrder.FindOrder(userInput)
            escape_button.grid_forget()
            confirm_button.grid_forget()
            ssn.grid_forget()
            self.userInput.grid_forget()
            self.back_button = tk.Button(self, text="Esc - Til baka", bg="#9E4848", fg="white", width=15, height=1, command=lambda: back(self,controller))
            self.delete_button = tk.Button(self, text="Eyða", bg="#9E4848", fg="white", width=15, height=1, command=lambda: back(self,controller))
            self.edit_button = tk.Button(self, text="Breyta/Uppfæra", bg="#448F42", fg="white", width=15, height=1, command=lambda:back(self,controller))
            self.back_button.config(font=("Courier", 16))
            self.delete_button.config(font=("Courier", 16))
            self.edit_button.config(font=("Courier", 16))
            self.back_button.grid(row=10, column=1,columnspan=1)
            self.delete_button.grid(row=10, column=3,columnspan=1)
            self.edit_button.grid(row=10, column=2,columnspan=1)
        def back(self,controller):
            self.back_button.grid_forget()
            self.delete_button.grid_forget()
            self.edit_button.grid_forget()
            escape_button.grid(row=10, column=1)
            confirm_button.grid(row=10, column=4)
            self.userInput.grid(row=4, column=4,columnspan = 1)
            ssn.grid(row=4, column=1)