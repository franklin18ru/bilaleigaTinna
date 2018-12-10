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
label1 = Label(root, text="Velja dagsetningu",bg="#5A6D7C",fg="white")
line1 = Label(root, text="____________________________",bg="#5A6D7C",fg="white")
line2 = Label(root, text="____________________________",bg="#5A6D7C",fg="white")
start = Label(root, text="Til (dd.mm.yyyy): ",bg="#5A6D7C",fg="white")
end = Label(root, text="Frá (dd.mm.yyyy): ",bg="#5A6D7C",fg="white")

#Create entry fields
startInput = Entry(root, width=20, font=("Courier", 20)) #input for the date, should be on format 'dd.mm.yyyy'
endInput = Entry(root, width=20, font=("Courier", 20)) #same ^^


#Create buttons
back = Button(root, text="Esc - Til baka", bg="#C8C8C8", fg="black", width=18, height=1)
confirm = Button(root, text="Staðfesta", bg="#C8C8C8", fg="black", width=18, height=1)

#################################################################################

#configure labels
bilaleigaTinna.config(font=("Courier", 32))
label1.config(font=("Courier", 24))
start.config(font=("Courier", 24))
end.config(font=("Courier", 24))
confirm.config(font=("Courier", 16))
back.config(font=("Courier",16))
line1.config(font=("Courier", 28))
line2.config(font=("Courier", 28))


#Position widgets

#positioning everything on the screen
bilaleigaTinna.grid(row=1, column=3)
label1.grid(row=3, column=3)
start.grid(row=4, column=2)
startInput.grid(row=4, column=3)
end.grid(row=5, column=2)
endInput.grid(row=5, column=3)
confirm.grid(row=10, column=4)
back.grid(row=10, column=2)
line1.grid(row=2,column=3)
line2.grid(row=9,column=3)
 



#position frame
root.grid_rowconfigure(0, weight=3)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(5, weight=2)
root.grid_rowconfigure(9, weight=2)
root.grid_rowconfigure(11, weight=5)
root.grid_columnconfigure(0, weight=10)
root.grid_columnconfigure(6, weight=10)



#################################################################################


root.mainloop()