import tkinter as tk
import menuUi
import csv

class CustomersUi(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#5A6D7C")
        screen_width = self.winfo_screenwidth() #Gets the screen width
        screen_height = self.winfo_screenheight() #Gets the screen height
        self.winfo_toplevel().configure(bg="#5A6D7C") # Changes background color of frame
        self.winfo_toplevel().geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame






        bilaleigaTinna = tk.Label(self, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
        customer = tk.Label(self, text="Viðskiptavinir",bg="#5A6D7C",fg="white")
        full_name = tk.Label(self, text="Nafn",bg="#5A6D7C",fg="white")
        ssn = tk.Label(self, text="Kennitala",bg="#5A6D7C",fg="white")
        email = tk.Label(self, text="Email",bg="#5A6D7C",fg="white")
        phone_number = tk.Label(self, text="Símanúmer",bg="#5A6D7C",fg="white")
        line1 = tk.Label(self, text="_______________________________",bg="#5A6D7C",fg="white")
        line2 = tk.Label(self, text="_______________________________",bg="#5A6D7C",fg="white")


        #Create Buttons
        escape_button = tk.Button(self, text="Esc - Til baka", bg="#9E4848", fg="white", width=15, height=1, command=   
                                                                                                                     lambda:esc(controller))
        edit = tk.Button(self, text="Edit", bg="#448F42", fg="black", width=7, height=1)
        with open('data/customers.csv', 'r', newline="") as customers:
            csv_reader = csv.reader(customers)
            next(csv_reader)
            row_num = 5
            column_num = 0
            counter = 0
            for item in csv_reader:
                tk.label3 = tk.Label(self, text=item[0],bg="#5A6D7C",fg="white",width=22, height=2)
                tk.label3.config(font=("Courier", 16))
                tk.label3.grid(row = row_num, column=column_num)

                tk.label4 = tk.Label(self, text=item[1],bg="#5A6D7C",fg="white", width=22, height=2)
                tk.label4.config(font=("Courier", 16))
                tk.label4.grid(row = row_num, column=column_num+1)

                tk.label5 = tk.Label(self, text=item[2],bg="#5A6D7C",fg="white", width=22, height=2)
                tk.label5.config(font=("Courier", 16))
                tk.label5.grid(row = row_num, column=column_num+2)

                tk.label6 = tk.Label(self, text=item[3],bg="#5A6D7C",fg="white", width=22, height=2)
                tk.label6.config(font=("Courier", 16))
                tk.label6.grid(row = row_num, column=column_num+3)





                row_num += 1

            #column_num += 1



                


        #configure tk.labels
        bilaleigaTinna.config(font=("Courier", 32))
        customer.config(font=("Courier", 28))
        full_name.config(font=("Courier", 16))
        ssn.config(font=("Courier", 16))
        email.config(font=("Courier", 16))
        phone_number.config(font=("Courier", 16))

        line1.config(font=("Courier", 28))
        line2.config(font=("Courier", 28))
        edit.config( font=("Courier", 16))
        escape_button.config( font=("Courier", 16))





        #Position widgets

        #tk.labels
        bilaleigaTinna.grid(row=1, column=0,columnspan = 8)
        customer.grid(row=3, column=0, columnspan = 8)
        full_name.grid(row=4, column=0)
        ssn.grid(row=4,column=1)
        email.grid(row=4,column=2)
        phone_number.grid(row=4,column=3)
        line1.grid(row=2, column=0,columnspan = 8)
        line2.grid(row=10,column =0, columnspan = 8)

        edit.grid(row=11, column= 2, columnspan = 2 )
        escape_button.grid(row=11, column=0, columnspan = 3)




        #position frame

        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(11, weight=1)
        self.grid_rowconfigure(9, weight=1)

        self.grid_rowconfigure(12, weight=3)



        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(7, weight=2)


        def esc(self):
            controller.show_frame(menuUi.MenuUi)


