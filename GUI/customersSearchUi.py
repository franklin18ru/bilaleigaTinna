from tkinter import *
import csv

root = Tk()

root.title("Pantanir")
screen_width = root.winfo_screenwidth() #Gets the screen width
screen_height = root.winfo_screenheight() #Gets the screen height
root.configure(bg="#5A6D7C") # Changes background color of frame
root.geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame


bilaleigaTinna = Label(root, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
line1 = Label(root, text="_______________________________",bg="#5A6D7C",fg="white")
customer = Label(root, text="Viðskiptavinir",bg="#5A6D7C",fg="white")

name_ssn = Label(root, text="Sláðu inn nafn/kennitölu \nviðskiptavinar",bg="#5A6D7C",fg="white")
user_input = Entry(root, width=20, font=("Courier", 20))

line2 = Label(root, text="_______________________________",bg="#5A6D7C",fg="white")


#Create Buttons
escape_button = Button(root, text="Esc - Til baka", bg="#9E4848", fg="white", width=15, height=1)
confirm = Button(root, text="Staðfesta", bg="#448F42", fg="white", width=15, height=1)


#configure labels
bilaleigaTinna.config(font=("Courier", 32))
customer.config(font=("Courier", 28))
name_ssn.config(font=("Courier", 16))
user_input.config(font=("Courier", 16))

line1.config(font=("Courier", 28))
line2.config(font=("Courier", 28))
confirm.config( font=("Courier", 16))
escape_button.config( font=("Courier", 16))


#labels
bilaleigaTinna.grid(row=1, column=0,columnspan = 8)
line1.grid(row=2, column=0,columnspan = 8)
customer.grid(row=3, column=0, columnspan = 8)

name_ssn.grid(row=4, column=0)
user_input.grid(row=4,column=1)

line2.grid(row=10,column =0, columnspan = 8)

confirm.grid(row=11, column= 2, columnspan = 2 )
escape_button.grid(row=11, column=0, columnspan = 3)




#position frame

root.grid_rowconfigure(0, weight=2)
root.grid_rowconfigure(2, weight=0)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(11, weight=1)
root.grid_rowconfigure(9, weight=1)

root.grid_rowconfigure(12, weight=3)



root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(7, weight=2)


root.mainloop()
