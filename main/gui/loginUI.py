import sys
sys.path.append("..")
from tkinter import *

from services.login import loginVerification



def verify(usernameInput, passwordInput):
    instance = loginVerification(usernameInput,passwordInput)

#create frame
root = Tk()
root.title("Bílaleiga Tinna")
screen_width = root.winfo_screenwidth() #Gets the screen width
screen_height = root.winfo_screenheight() #Gets the screen height
root.configure(bg="#5A6D7C") # Changes background color of frame
root.geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame



#Create labels
bilaleigaTinna = Label(root, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
label1 = Label(root, text="Innskráning",bg="#5A6D7C",fg="white")
username = Label(root, text="Starfsnúmer:",bg="#5A6D7C",fg="white")
password = Label(root, text="Lykilorð:",bg="#5A6D7C",fg="white")



#Create the entry fields
usernameInput = Entry(root, width=20, font=("Courier", 20))
passwordInput = Entry(root, show="*", width=20, font=("Courier", 20))


#Create buttons
confirm = Button(root, text="Innskrá", bg="#424242", fg="white", width=8, height=1,font=("Courier",16), command=verify)

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
confirm.grid(row=6, column=2)

#position frame
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(7, weight=3)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(7, weight=1)


#################################################################################


root.mainloop() 