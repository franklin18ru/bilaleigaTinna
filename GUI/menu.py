from tkinter import *

#create frame
root = Tk()
root.title("Bílaleiga Tinna")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.configure(bg="#5A6D7C")
root.geometry(str(screen_width)+"x"+str(screen_height))



#Create labels
bilaleigaTinna = Label(root, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
label1 = Label(root, text="Valmynd",bg="#5A6D7C",fg="white")


#Create buttons
new_order = Button(root,    text="1. Panta bíl", bg="#424242", fg="white", width=8, height=1)
return_car = Button(root,   text="2. Skila bíl", bg="#424242", fg="white", width=8, height=1)
orders = Button(root,       text="3. Pantanir", bg="#424242", fg="white", width=8, height=1)
prices = Button(root,       text="4. Verðskrá", bg="#424242", fg="white", width=8, height=1)
cars = Button(root,         text="5. Bílar", bg="#424242", fg="white", width=8, height=1)
customers = Button(root,    text="6. Viðskiptavnir", bg="#424242", fg="white", width=8, height=1)

#################################################################################

#configure labels
bilaleigaTinna.config(font=("Courier", 32))
label1.config(font=("Courier", 28))
new_order.config( font=("Courier",16))
return_car.config( font=("Courier",16))
orders.config( font=("Courier",16))
prices.config( font=("Courier",16))
cars.config( font=("Courier",16))
customers.config( font=("Courier",16))
# username.config(font=("Courier", 22))
# password.config(font=("Courier", 22))


#Position widgets

#labels
bilaleigaTinna.grid(row=1, column=2, sticky = NSEW)
label1.grid(row=3, column=2, sticky = NSEW)
# username.grid(row=4, column=0, sticky = E)
# password.grid(row=5, column=0, sticky = E)

#Entries
# usernameInput.grid(row=4, column=2)
# passwordInput.grid(row=5, column=2)
# confirm.grid(row=6, column=2)

#position frame
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(6, weight=3)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(6, weight=1)


#################################################################################


root.mainloop() 

