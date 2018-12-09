from tkinter import *

root = Tk()

root.title("Skrá viðskiptavin")
screen_width = root.winfo_screenwidth() #Gets the screen width
screen_height = root.winfo_screenheight() #Gets the screen height
root.configure(bg="#5A6D7C") # Changes background color of frame
root.geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame



bilaleigaTinna = Label(root, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
label1 = Label(root, text="Skila bíl",bg="#5A6D7C",fg="white")
line1 = Label(root, text="____________________________",bg="#5A6D7C",fg="white")
license_plate = Label(root, text="Sláðu inn bílnúmer:",bg="#5A6D7C",fg="white")
line2 = Label(root, text="____________________________",bg="#5A6D7C",fg="white")2



#Create the entry fields
license_plateInput = Entry(root, width=20, font=("Courier", 20))



#Create Buttons
escape_button = Button(root, text="Esc - Til baka", bg="#9E4848", fg="white", width=15, height=1)
confirm_button = Button(root, text="Staðfesta", bg="#448F42", fg="white", width=15, height=1)





#configure labels
bilaleigaTinna.config(font=("Courier", 32))
label1.config(font=("Courier", 28))
escape_button.config(font=("Courier", 16))
confirm_button.config(font=("Courier", 16))
line1.config(font=("Courier", 28))
line2.config(font=("Courier", 28))
license_plate.config(font=("Courier", 16))



#Position widgets

#labels
bilaleigaTinna.grid(row=1, column=3)
label1.grid(row=3, column=3)
license_plate.grid(row=5, column=2)

escape_button.grid(row=10, column=2)
confirm_button.grid(row=10, column=4)
line1.grid(row=2,column=3)
line2.grid(row=9,column=3)

license_plateInput.grid(row=5, column=3)


root.grid_rowconfigure(0, weight=2)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)
root.grid_rowconfigure(3, weight=2)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_rowconfigure(7, weight=1)
root.grid_rowconfigure(8, weight=1)
root.grid_rowconfigure(9, weight=1)
root.grid_rowconfigure(11, weight=5)

root.grid_columnconfigure(0, weight=10)
#root.grid_columnconfigure(1, weight=50)
root.grid_columnconfigure(6, weight=10)


root.mainloop()
