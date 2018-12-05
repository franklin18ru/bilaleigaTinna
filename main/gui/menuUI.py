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
line1 = Label(root, text="____________________________",bg="#5A6D7C",fg="white")
line2 = Label(root, text="____________________________",bg="#5A6D7C",fg="white")

#Create buttons
new_order = Button(root,    text="1. Panta bíl", bg="#424242", fg="white", width=22, height=2)
return_car = Button(root,   text="2. Skila bíl", bg="#424242", fg="white", width=22, height=2)
orders = Button(root,       text="3. Pantanir", bg="#424242", fg="white", width=22, height=2)
prices = Button(root,       text="4. Verðskrá", bg="#424242", fg="white", width=22, height=2)
cars = Button(root,         text="5. Bílar", bg="#424242", fg="white", width=22, height=2)
customers = Button(root,    text="6. Viðskiptavnir", bg="#424242", fg="white", width=22, height=2)
back = Button(root,         text="Esc - Til baka", bg="#C8C8C8", fg="black", width=18, height=1)

#################################################################################

#configure labels
bilaleigaTinna.config(font=("Courier", 32))
label1.config(font=("Courier", 24))
new_order.config( font=("Courier",16))
return_car.config( font=("Courier",16))
orders.config( font=("Courier",16))
prices.config( font=("Courier",16))
cars.config( font=("Courier",16))
customers.config( font=("Courier",16))
back.config(font=("Courier",16))
line1.config(font=("Courier", 28))
line2.config(font=("Courier", 28))


#Position widgets

#labels
bilaleigaTinna.grid(row=1, column=3)
label1.grid(row=3, column=3)
new_order.grid(row=4, column=2)
return_car.grid(row=4, column=3)
orders.grid(row=4, column=5)
prices.grid(row=8, column=2)
cars.grid(row=8, column=3)
customers.grid(row=8, column=5)
back.grid(row=10, column=3)
line1.grid(row=2,column=3)
line2.grid(row=9,column=3)



#position frame
root.grid_rowconfigure(0, weight=3)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(5, weight=2)
root.grid_rowconfigure(9, weight=2)
root.grid_rowconfigure(11, weight=5)
root.grid_columnconfigure(0, weight=10)
root.grid_columnconfigure(6, weight=10)
root.grid_columnconfigure(1, weight=0)


#################################################################################


root.mainloop() 

