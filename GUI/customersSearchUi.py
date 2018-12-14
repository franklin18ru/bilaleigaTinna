import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import tkinter as tk
import customersMenuUi
from services import findCustomer


class CustomersSearchUi(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#5A6D7C")
        screen_width = self.winfo_screenwidth() #Gets the screen width
        screen_height = self.winfo_screenheight() #Gets the screen height
        self.winfo_toplevel().configure(bg="#5A6D7C") # Changes background color of frame
        self.winfo_toplevel().geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame

        bilaleigaTinna = tk.Label(self, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
        line1 = tk.Label(self, text="_______________________________",bg="#5A6D7C",fg="white")
        customer = tk.Label(self, text="Viðskiptavinir",bg="#5A6D7C",fg="white")
        name_ssn = tk.Label(self, text="Sláðu inn nafn/kennitölu \nviðskiptavinar",bg="#5A6D7C",fg="white")
        self.user_input = tk.Entry(self, width=20, font=("Courier", 20))
        line2 = tk.Label(self, text="_______________________________",bg="#5A6D7C",fg="white")

        self.leftFrame = tk.Frame(self, bg="#5A6D7C")
        self.leftFrame.grid(row=5,column=1, columnspan=2)

        self.rightFrame=tk.Frame(self, bg="#5A6D7C")
        self.rightFrame.grid(row=5,column=5, columnspan=2)

        #Create Buttons to activate functions that return the users to the page they want
        escape_button = tk.Button(self, text="Esc - Til baka", bg="#9E4848", fg="white", width=15, height=1, command=lambda: esc(self,controller))
        confirm_button = tk.Button(self, text="Staðfesta", bg="#448F42", fg="white", width=15, height=1, command=lambda: confirm(self,controller))

        #configure labels
        bilaleigaTinna.config(font=("Courier", 32))
        customer.config(font=("Courier", 28))
        name_ssn.config(font=("Courier", 16))
        self.user_input.config(font=("Courier", 16))

        line1.config(font=("Courier", 28))
        line2.config(font=("Courier", 28))
        
        escape_button.config( font=("Courier", 16))
        confirm_button.config( font=("Courier", 16))

        #labels
        bilaleigaTinna.grid(row=1, column=0,columnspan = 8)
        line1.grid(row=2, column=0,columnspan = 8)
        customer.grid(row=3, column=0, columnspan = 8)
        name_ssn.grid(row=4, column=1)
        self.user_input.grid(row=4,column=4,columnspan = 1)
        line2.grid(row=9,column =0, columnspan = 8)
        
        escape_button.grid(row=10, column=1)
        confirm_button.grid(row=10, column= 4)

        #position frame
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(8, weight=1)
        self.grid_rowconfigure(9, weight=1)
        self.grid_rowconfigure(11, weight=1)
        self.grid_rowconfigure(12, weight=3)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(7, weight=1)


        def esc(self,controller): #clearing the user input and returning him to the customersMenu page
            self.user_input.delete(0,"end")
            controller.show_frame(customersMenuUi.CustomersMenuUi)

        def confirm(self,controller):
            userinput = self.user_input.get()
            self.instance = findCustomer.FindCustomer(userinput) #creating instance as the findCustomer file from services

            #deleting the old info on the last page and creating the new info
            escape_button.grid_forget()
            confirm_button.grid_forget()
            name_ssn.grid_forget()
            self.user_input.grid_forget()
            self.back_button = tk.Button(self, text="Esc - Til baka", bg="#9E4848", fg="white", width=15, height=1, command=lambda: back(self,controller))
            self.delete_button = tk.Button(self, text="Eyða", bg="#9E4848", fg="white", width=15, height=1, command=lambda: delete(self,controller))
            self.edit_button = tk.Button(self, text="Breyta/Uppfæra", bg="#448F42", fg="white", width=15, height=1, command=lambda:edit(self,controller))
            self.back_button.config(font=("Courier", 16))
            self.delete_button.config(font=("Courier", 16))
            self.edit_button.config(font=("Courier", 16))
            self.back_button.grid(row=10, column=2)
            self.edit_button.grid(row=10, column=4,columnspan=1)
            self.delete_button.grid(row=10, column=6)

            
            self.showCustomerNameLabel = tk.Label(self.leftFrame, text="Nafn")
            self.showCustomerSsnLabel = tk.Label(self.rightFrame, text="Kennitala")
            self.showCustomerEmailLabel = tk.Label(self.leftFrame, text="Email")
            self.showCustomerPhoneLabel = tk.Label(self.rightFrame, text="Sími")

            self.showCustomerName = tk.Label(self.leftFrame, text=self.instance.customer[1][0])
            self.showCustomerSsn = tk.Label(self.rightFrame, text=self.instance.customer[0])
            self.showCustomerEmail = tk.Label(self.leftFrame, text=self.instance.customer[1][1])
            self.showCustomerPhone = tk.Label(self.rightFrame, text=self.instance.customer[1][2])

            self.showCustomerNameLabel.config(font=("Courier", 22), bg="#5A6D7C", fg="white")
            self.showCustomerSsnLabel.config(font=("Courier", 22), bg="#5A6D7C", fg="white")
            self.showCustomerEmailLabel.config(font=("Courier", 22), bg="#5A6D7C", fg="white")
            self.showCustomerPhoneLabel.config(font=("Courier", 22), bg="#5A6D7C", fg="white")

            self.showCustomerNameLabel.grid(row=0, column=0, columnspan=3, pady=10)
            self.entryname = tk.Entry(self.leftFrame,width=20, font=("Courier", 20))
            self.entryname.insert(0,self.instance.customer[1][0])
            self.showCustomerSsnLabel.grid(row=0, column=0, columnspan=3, pady=10)
            self.entryssn = tk.Entry(self.rightFrame,width=20, font=("Courier", 20))
            self.entryssn.insert(0,self.instance.customer[0])
            self.showCustomerEmailLabel.grid(row=3, column=0, columnspan=3, pady=10)
            self.entryemail = tk.Entry(self.leftFrame,width=20, font=("Courier", 20))
            self.entryemail.insert(0,self.instance.customer[1][1])
            self.showCustomerPhoneLabel.grid(row=3, column=0, columnspan=3, pady=10)
            self.entryphone = tk.Entry(self.rightFrame,width=20, font=("Courier", 20))
            self.entryphone.insert(0,self.instance.customer[1][2])
            
            self.showCustomerName.config(font=("Courier", 16), bg="#5A6D7C", fg="white")
            self.showCustomerSsn.config(font=("Courier", 16), bg="#5A6D7C", fg="white")
            self.showCustomerEmail.config(font=("Courier", 16), bg="#5A6D7C", fg="white")
            self.showCustomerPhone.config(font=("Courier", 16), bg="#5A6D7C", fg="white")

            self.showCustomerName.grid(row=1, column=0, columnspan=3)
            self.showCustomerSsn.grid(row=1, column=0, columnspan=3)
            self.showCustomerEmail.grid(row=4, column=0, columnspan=3)
            self.showCustomerPhone.grid(row=4, column=0, columnspan=3)


        def back(self,controller):
            self.user_input.grid(row=4,column=4,columnspan = 1)
            name_ssn.grid(row=4, column=1)
            escape_button.grid(row=10, column=1,columnspan = 4)
            confirm_button.grid(row=10, column=2,columnspan = 4)
            
            self.entryname.grid_forget()
            self.entryssn.grid_forget()
            self.entryemail.grid_forget()
            self.entryphone.grid_forget()
            self.showCustomerNameLabel.destroy()
            self.showCustomerSsnLabel.destroy()
            self.showCustomerEmailLabel.destroy()
            self.showCustomerPhoneLabel.destroy()
            self.showCustomerName.destroy()
            self.showCustomerSsn.destroy()
            self.showCustomerEmail.destroy()
            self.showCustomerPhone.destroy()
            self.back_button.destroy()
            self.delete_button.destroy()
            self.edit_button.destroy()


        def edit(self,controller):
            self.showCustomerName.destroy()
            self.showCustomerSsn.destroy()
            self.showCustomerEmail.destroy()
            self.showCustomerPhone.destroy()
            self.back_button.destroy()
            self.delete_button.destroy()
            self.edit_button.destroy()
            self.edit_button = tk.Button(self, text="Staðfesta", bg="#448F42", fg="white", width=15, height=1, command=lambda:change(self,controller))
            self.back_button = tk.Button(self, text="Esc - Til baka", bg="#9E4848", fg="white", width=15, height=1, command=lambda: back(self,controller))
            self.edit_button.config(font=("Courier", 16))
            self.back_button.config(font=("Courier", 16))
            self.edit_button.grid(row=10, column=5)
            self.back_button.grid(row=10, column=2)

            self.entryname.grid(row=1, column=0, columnspan=3)
            self.entryssn.grid(row=1, column=0, columnspan=3)
            self.entryemail.grid(row=4, column=0, columnspan=32)
            self.entryphone.grid(row=4, column=0, columnspan=3)


        def change(self,controller):
            newname = self.entryname.get()
            newssn = self.entryssn.get()
            newemail = self.entryemail.get()
            newphone = self.entryphone.get()
            newdata = [newname,newssn,newemail,newphone]
            self.instance.editCustomer(newdata)

            self.edit_button.grid_forget()
            self.back_button.grid_forget()
            self.entryname.grid_forget()
            self.entryssn.grid_forget()
            self.entryemail.grid_forget()
            self.entryphone.grid_forget()

            self.showCustomerNameLabel.grid_forget()
            self.showCustomerSsnLabel.grid_forget()
            self.showCustomerEmailLabel.grid_forget()
            self.showCustomerPhoneLabel.grid_forget()
            self.user_input.delete(0,"end")
            name_ssn.grid(row=4, column=1)
            self.user_input.grid(row=4,column=4,columnspan = 1)
            escape_button.grid(row=10, column=3)
            confirm_button.grid(row=10, column= 4)

            controller.show_frame(customersMenuUi.CustomersMenuUi)

        def delete(self,controller):
            name = self.instance.customer[1][0]
            ssn = self.instance.customer[0] 
            self.instance.deleteCustomer(name,ssn)
            controller.show_frame(customersMenuUi.CustomersMenuUi)