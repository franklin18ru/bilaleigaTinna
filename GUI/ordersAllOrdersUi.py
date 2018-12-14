import tkinter as tk
import csv
import ordersUi



class OrdersAllOrdersUi(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#5A6D7C")
        screen_width = self.winfo_screenwidth() #Gets the screen width
        screen_height = self.winfo_screenheight() #Gets the screen height
        self.winfo_toplevel().configure(bg="#5A6D7C") # Changes background color of frame
        self.winfo_toplevel().geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame
    
        #Create labels
        bilaleigaTinna = tk.Label(self, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
        label2 = tk.Label(self, text="Pantanir",bg="#5A6D7C",fg="white") 

        line1 = tk.Label(self, text="_____________________________",bg="#5A6D7C",fg="white")
        line2 = tk.Label(self, text="_____________________________",bg="#5A6D7C",fg="white")

        back = tk.Button(self, text="Esc - Til baka", bg="#9E4848", fg="white", width=15, height=1, command=lambda: esc(controller))

        option_frame = tk.Frame(self)#trying to make a scroll-able frame for all the cars, wont work


        #Open the leases file and printing the content in buttons
        with open('data/leases.csv', 'r', newline="") as cars:
            csv_reader = csv.reader(cars)
            next(csv_reader)
            row_num = 4
            column_num = 2
            counter = 0
            
            for item in csv_reader:
                
                label1 = tk.Button(self, text=item[1] ,bg="#424242",fg="white", width=22, height=2)
                label1.config(font=("Courier", 16))
                label1.grid(row = row_num, column=column_num)
                
                counter += 1
                column_num += 1
                
                if counter == 3:
                    row_num += 1
                    counter = 0
                    column_num = 2   

        # configure labels
        bilaleigaTinna.config(font=("Courier", 32))
        back.config(font=("Courier",16))
        line1.config(font=("Courier", 28))
        line2.config(font=("Courier", 28))
        label2.config(font=("Courier", 26)) #the changable label



        # positioning everything on the screen
        bilaleigaTinna.grid(row=1, column=0,columnspan = 8)
        label2.grid(row=3,column=0,columnspan = 8)
        back.grid(row=10, column=1,columnspan = 2)
        line1.grid(row=2,column=0,columnspan = 8)
        line2.grid(row=9,column=0,columnspan = 8)
        


        # position frame
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(5, weight=2)
        self.grid_rowconfigure(9, weight=2)
        self.grid_rowconfigure(11, weight=5) 
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(6, weight=2)

        def esc(self):
            controller.show_frame(ordersUi.OrdersUi)
    
        #####