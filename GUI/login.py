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
label1 = Label(root, text="Innskráning",bg="#5A6D7C",fg="white")
username = Label(root, text="Starfsnúmer:",bg="#5A6D7C",fg="white")
password = Label(root, text="Lykilorð:",bg="#5A6D7C",fg="white")



#Create the entry fields
usernameInput = Entry(root, width=20, font=("Courier", 20))
passwordInput = Entry(root, show="*", width=20, font=("Courier", 20))


#Create buttons
confirm = Button(root, width=10, height=5, font=("Courier", 20))

#################################################################################

#configure labels
bilaleigaTinna.config(font=("Courier", 32))
label1.config(font=("Courier", 28))
username.config(font=("Courier", 22))
password.config(font=("Courier", 22))


#Position widgets

#labels
bilaleigaTinna.grid(row=1, column=2, sticky = NSEW)
label1.grid(row=3, column=2, sticky = NSEW)
username.grid(row=4, column=0, sticky = E)
password.grid(row=5, column=0, sticky = E)

#Entries
usernameInput.grid(row=4, column=2)
passwordInput.grid(row=5, column=2)

#position frame
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(6, weight=3)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(6, weight=1)


#################################################################################


root.mainloop() 