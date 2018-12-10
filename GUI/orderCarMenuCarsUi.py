import tkinter as tk
import csv
class OrderCarMenuCarsUi(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#5A6D7C")
        screen_width = self.winfo_screenwidth() #Gets the screen width
        screen_height = self.winfo_screenheight() #Gets the screen height
        self.winfo_toplevel().configure(bg="#5A6D7C") # Changes background color of frame
        self.winfo_toplevel().geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame
    

        #Create labels
        bilaleigaTinna = tk.Label(self, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")

        # A lable that should change for what the user clicks on:
        label2 = tk.Label(self, text="Bílar",bg="#5A6D7C",fg="white") #setting the default value as Bílar

        # Here there should be an if statement to change the lable to the correct word:
        label2.config(text="Jeppar") #changing the default value to what the user selected on the site before

        line1 = tk.Label(self, text="____________________________",bg="#5A6D7C",fg="white")
        line2 = tk.Label(self, text="____________________________",bg="#5A6D7C",fg="white")
        back = tk.Button(self, text="Esc - Til baka", bg="#C8C8C8", fg="black", width=18, height=1)

        option_frame = tk.Frame(self)#trying to make a scroll-able frame for all the cars, wont work


        #Open the cars file and printing the content in buttons
        with open('data/cars.csv', 'r', newline="") as cars:
            csv_reader = csv.reader(cars)
            next(csv_reader)
            row_num = 4
            column_num = 2
            counter = 0
            for item in csv_reader:
                if item[1] == "Jeppi": #Here "Jeppi" should change to what the user selected on the site before
                    label1 = Button(self, text=item[2] ,bg="#424242",fg="white", width=22, height=2)
                    label1.config(font=("Courier", 16))
                    label1.grid(row = row_num, column=column_num)
                    counter += 1
                    column_num += 1
                    if counter == 3:
                        row_num += 1
                        counter = 0
                        column_num = 2   
            #option_frame.pack(fill="x",side="top")

        # configure labels
        bilaleigaTinna.config(font=("Courier", 32))
        back.config(font=("Courier",16))
        line1.config(font=("Courier", 28))
        line2.config(font=("Courier", 28))
        label2.config(font=("Courier", 26)) #the changable label



        # positioning everything on the screen
        bilaleigaTinna.grid(row=1, column=3)
        label2.grid(row=3,column=3)
        back.grid(row=10, column=3)
        line1.grid(row=2,column=3)
        line2.grid(row=9,column=3)
        


        # position frame
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(5, weight=2)
        self.grid_rowconfigure(9, weight=2)
        self.grid_rowconfigure(11, weight=5)
        self.grid_columnconfigure(0, weight=10)
        self.grid_columnconfigure(6, weight=10)
        option_frame.grid_columnconfigure(0, weight=10)
        option_frame.grid_columnconfigure(6, weight=10)
        option_frame.grid_rowconfigure(0, weight=3)
        option_frame.grid_rowconfigure(1, weight=0)
        option_frame.grid_rowconfigure(3, weight=1)
        option_frame.grid_rowconfigure(5, weight=2)

        #####