from tkinter import *

root = Tk()

root.title("Pantanir")
screen_width = root.winfo_screenwidth() #Gets the screen width
screen_height = root.winfo_screenheight() #Gets the screen height
root.configure(bg="#5A6D7C") # Changes background color of frame
root.geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame







bilaleigaTinna = Label(root, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
label1 = Label(root, text="Verðskrá",bg="#5A6D7C",fg="white")
line1 = Label(root, text="____________________________",bg="#5A6D7C",fg="white")
line2 = Label(root, text="____________________________",bg="#5A6D7C",fg="white")




#Create Buttons
edit = Button(root, text="Edit", bg="white", fg="black", width=15, height=1)


#configure labels
bilaleigaTinna.config(font=("Courier", 32))
label1.config(font=("Courier", 28))
line1.config(font=("Courier", 28))
line2.config(font=("Courier", 28))
edit.config( font=("Courier", 16))




#Position widgets

#labels
bilaleigaTinna.grid(row=1, column=3)
label1.grid(row=3, column=3)
line1.grid(row=2,column=3)
line2.grid(row=5,column=3)
edit.grid(row=1, column= 4)



root.mainloop()