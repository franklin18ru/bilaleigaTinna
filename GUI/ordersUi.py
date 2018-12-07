from tkinter import *

root = Tk()

root.title("Pantanir")
screen_width = root.winfo_screenwidth() #Gets the screen width
screen_height = root.winfo_screenheight() #Gets the screen height
root.configure(bg="#5A6D7C") # Changes background color of frame
root.geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame







bilaleigaTinna = Label(root, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
label1 = Label(root, text="Pantanir",bg="#5A6D7C",fg="white")
line1 = Label(root, text="____________________________",bg="#5A6D7C",fg="white")
line2 = Label(root, text="____________________________",bg="#5A6D7C",fg="white")


#Create Buttons
costumer_name = Button(root,    text="1. Leita eftir \n viðskiptavini", bg="#424242", fg="white", width=22, height=3)
costumer_ssn = Button(root,   text="2. Leita eftir bíl", bg="#424242", fg="white", width=22, height=3)
costumer_car = Button(root,       text="3. Allar pantanir", bg="#424242", fg="white", width=22, height=3)
confirm = Button(root, text="Esc - Til baka", bg="white", fg="black", width=15, height=1)






#configure labels
bilaleigaTinna.config(font=("Courier", 32))
label1.config(font=("Courier", 28))
costumer_name.config( font=("Courier",16))
costumer_ssn.config( font=("Courier",16))
costumer_car.config( font=("Courier",16))
confirm.config( font=("Courier", 16))
line1.config(font=("Courier", 28))
line2.config(font=("Courier", 28))


#Position widgets

#labels
bilaleigaTinna.grid(row=1, column=3)
label1.grid(row=3, column=3)
costumer_name.grid(row=5, column=2)
costumer_ssn.grid(row=5, column=3)
costumer_car.grid(row=5, column=4)
confirm.grid(row=10, column=3)
line1.grid(row=2,column=3)
line2.grid(row=9,column=3)



#position frame

#root.grid_rowconfigure(1, weight=1)
#root.grid_rowconfigure(2, weight=1)
#root.grid_rowconfigure(7, weight=1)
#root.grid_columnconfigure(0, weight=1)
#root.grid_columnconfigure(7, weight=1)

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






root.mainloop()
