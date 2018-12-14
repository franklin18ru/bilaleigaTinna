import tkinter as tk
import menuUi
import ordersSearchCustomerUi
import ordersAllOrdersUi

class OrdersUi(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#5A6D7C")
        screen_width = self.winfo_screenwidth() #Gets the screen width
        screen_height = self.winfo_screenheight() #Gets the screen height
        self.winfo_toplevel().configure(bg="#5A6D7C") # Changes background color of frame
        self.winfo_toplevel().geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame

        bilaleigaTinna = tk.Label(self, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")         #creating labels
        label1 = tk.Label(self, text="Pantanir",bg="#5A6D7C",fg="white")
        line1 = tk.Label(self, text="_____________________________",bg="#5A6D7C",fg="white")
        line2 = tk.Label(self, text="_____________________________",bg="#5A6D7C",fg="white")


        #Create Buttons and calling a few functions
        costomer_order = tk.Button(self,    text="1. Leita af pöntun", bg="#424242", fg="white", width=22, height=3, command=lambda: switchOrdersSearchCustomer(controller))
        costomer_allorders = tk.Button(self,   text="2. Allar pantanir", bg="#424242", fg="white", width=22, height=3, command=lambda: switchOrdersAllOrders(controller))
        escape_button = tk.Button(self, text="Esc - Til baka", bg="#9E4848", fg="white", width=15, height=1, command=lambda: esc(controller))


        #configure labels
        bilaleigaTinna.config(font=("Courier", 32))
        label1.config(font=("Courier", 28))
        costomer_order.config( font=("Courier",16))
        costomer_allorders.config( font=("Courier",16))
        escape_button.config( font=("Courier", 16))
        line1.config(font=("Courier", 28))
        line2.config(font=("Courier", 28))


        #Position widgets

        bilaleigaTinna.grid(row=1, column=3)
        label1.grid(row=3, column=3)
        costomer_order.grid(row=4, column=3)
        costomer_allorders.grid(row=5, column=3)
        escape_button.grid(row=10, column=0,columnspan = 4)
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


        #Function that takes you to the menu when button is clicked
        def esc(self):
            controller.show_frame(menuUi.MenuUi)

        #Function that takes you to ordersSearchCustomerUi site when button is clicked
        def switchOrdersSearchCustomer(self):
            controller.show_frame(ordersSearchCustomerUi.OrdersSearchCustomerUi)

        #Function that takes you to ordersAllOrdersUi site when button is clicked
        def switchOrdersAllOrders(self):
            controller.show_frame(ordersAllOrdersUi.OrdersAllOrdersUi)