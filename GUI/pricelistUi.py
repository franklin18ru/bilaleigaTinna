import tkinter as tk
import menuUi
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from services import getPriceList


class PriceListUi(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#5A6D7C")
        screen_width = self.winfo_screenwidth() #Gets the screen width
        screen_height = self.winfo_screenheight() #Gets the screen height
        self.winfo_toplevel().configure(bg="#5A6D7C") # Changes background color of frame
        self.winfo_toplevel().geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame





        bilaleigaTinna = tk.Label(self, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
        label1 = tk.Label(self, text="Verðskrá",bg="#5A6D7C",fg="white")
        frame1 = tk.Frame(self,
                        
                        bd=4,
                        relief="ridge",
                        highlightbackground="white",
                        highlightcolor="white",
                        bg = "#5A6D7C")

        line1 = tk.Label(self, text="_____________________________",bg="#5A6D7C",fg="white")
        line2 = tk.Label(self, text="_____________________________",bg="#5A6D7C",fg="white")

        smabill = tk.Label(frame1, text="Smábíll",bg="#5A6D7C",fg="white",width=22, height=2)
        folksbill = tk.Label(frame1, text="Fólksbíll",bg="#5A6D7C",fg="white",width=22, height=2)
        jeppi = tk.Label(frame1, text="Jeppi",bg="#5A6D7C",fg="white",width=22, height=2)
        luxusbill = tk.Label(frame1, text="Lúxusbíll",bg="#5A6D7C",fg="white",width=22, height=2)
        
        


        #Create Buttons
        self.edit = tk.Button(self, text="Uppfæra", bg="#448F42", fg="white", width=10, height=1, command=lambda: editPriceList(self))
        self.escape_button = tk.Button(self, text="Esc - Til baka", bg="#9E4848", fg="white", width=15, height=1, command=lambda: esc(controller))


        # create service file and connect to data access and make edit work#
        self.instance = getPriceList.GetPriceList()
        row_num = 1
        column_num = 10
        

        self.listOfPrice = []
        self.listofEntry = []
        for item in self.instance.priceListDataAccess.pricelist:
            self.label4 = tk.Label(frame1, text=item +" kr." ,bg="#5A6D7C",fg="white", width=10, height=2)
            self.entry = tk.Entry(frame1)
            self.listofEntry.append(self.entry)
            self.entry.insert(0,item)
            self.listOfPrice.append(self.label4)
            self.label4.config(font=("Courier", 16))
            self.label4.grid(row = row_num, column=column_num)
            row_num+=1
            
        #configure labels
        bilaleigaTinna.config(font=("Courier", 32))
        label1.config(font=("Courier", 28))
        line1.config(font=("Courier", 28))
        line2.config(font=("Courier", 28))
        self.edit.config( font=("Courier", 16))
        self.escape_button.config( font=("Courier", 16))
        smabill.config(font=("Courier", 16))
        folksbill.config(font=("Courier", 16))
        jeppi.config(font=("Courier", 16))
        luxusbill.config(font=("Courier", 16))



        #labels
        bilaleigaTinna.grid(row=1, column=3)
        label1.grid(row=3, column=3)
        frame1.grid(row=7, column=3)
        line1.grid(row=2,column=3)
        line2.grid(row=10,column=3)
        self.escape_button.grid(row=11, column=0,columnspan = 4)
        self.edit.grid(row=11, column=3 ,columnspan = 5)
        smabill.grid(row=1,column=1)
        folksbill.grid(row=2,column=1)
        jeppi.grid(row=3,column=1)
        luxusbill.grid(row=4,column=1)


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
        


        def editPriceList(self):
            for succ in self.listOfPrice:
                succ.grid_forget()
            self.escape_button.grid_forget()
            self.edit.grid_forget()
            self.change = tk.Button(self, text="Uppfæra", bg="#448F42", fg="white", width=10, height=1, command=lambda: changePriceList(self))
            self.back_button = tk.Button(self, text="Esc - Til baka", bg="#9E4848", fg="white", width=15, height=1, command=lambda: showoldinfo(self))
            self.change.config( font=("Courier", 16))
            self.back_button.config( font=("Courier", 16))
            self.change.grid(row=11, column=3 ,columnspan = 5)
            self.back_button.grid(row=11, column=0,columnspan = 4)
            entry_row_num = 1
            entry_column_num = 10
            for item in self.listofEntry:
                item.grid(row = entry_row_num, column=entry_column_num)
                entry_row_num+=1
                
        def showoldinfo(self):
            self.back_button.grid_forget()
            self.change.grid_forget()
            for item in self.listofEntry:
                item.grid_forget()
            self.escape_button.grid(row=11, column=0,columnspan = 4)
            self.edit.grid(row=11, column=3 ,columnspan = 5)
            self.instance = getPriceList.GetPriceList()
            row_num = 1
            column_num = 10
            self.listOfPrice = []
            self.listofEntry = []
            for item in self.instance.priceListDataAccess.pricelist:
                self.label4 = tk.Label(frame1, text=item +" kr." ,bg="#5A6D7C",fg="white", width=10, height=2)
                self.entry = tk.Entry(frame1)
                self.listofEntry.append(self.entry)
                self.entry.insert(0,item)
                self.listOfPrice.append(self.label4)
                self.label4.config(font=("Courier", 16))
                self.label4.grid(row = row_num, column=column_num)
                row_num+=1


        def changePriceList(self):
            listi=[]
            for self.price in self.listofEntry:
                self.newprice = self.price.get()
                listi.append(self.newprice)
            self.instance.editPriceList(listi)
            showoldinfo(self)




        def esc(self):
            controller.show_frame(menuUi.MenuUi)

