from tkinter import *
#import tkinter as tk
import csv

#create frame
root = Tk()
root.title("Bílaleiga Tinna")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.configure(bg="#5A6D7C")
root.geometry(str(screen_width)+"x"+str(screen_height))



#Create labels
bilaleigaTinna = Label(root, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")

# A lable that should change for what the user clicks on:
label2 = Label(root, text="Bílar",bg="#5A6D7C",fg="white") #setting the default value as Bílar

# Here there should be an if statement to change the lable to the correct word:
label2.config(text="Jeppar") #changing the default value

line1 = Label(root, text="____________________________",bg="#5A6D7C",fg="white")
line2 = Label(root, text="____________________________",bg="#5A6D7C",fg="white")
back = Button(root, text="Esc - Til baka", bg="#C8C8C8", fg="black", width=18, height=1)

option_frame = Frame(root)#trying to make a scroll-able frame for all the cars, wont work


#Open the cars file and printing the content in buttons
with open('data/cars.csv', 'r', newline="") as cars:
    csv_reader = csv.reader(cars)
    next(csv_reader)
    row_num = 4
    column_num = 2
    counter = 0
    for item in csv_reader:
        label1 = Button(root, text=item[2] ,bg="#424242",fg="white", width=22, height=2)
        label1.config(font=("Courier", 16))
        label1.grid(row = row_num, column=column_num)
        counter += 1
        column_num += 1
        if counter == 3:
            row_num += 1
            counter = 0
            column_num = 2   
    #option_frame.pack(fill="x",side="top")

# configure labels
bilaleigaTinna.config(font=("Courier", 32))
back.config(font=("Courier",16))
line1.config(font=("Courier", 28))
line2.config(font=("Courier", 28))
label2.config(font=("Courier", 26)) #the changable label



# positioning everything on the screen
bilaleigaTinna.grid(row=1, column=3)
label2.grid(row=3,column=3)
back.grid(row=0, column=2)
line1.grid(row=2,column=3)
line2.grid(row=9,column=3)
 


# position frame
root.grid_rowconfigure(0, weight=3)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(5, weight=2)
root.grid_rowconfigure(9, weight=2)
root.grid_rowconfigure(11, weight=5)
root.grid_columnconfigure(0, weight=10)
root.grid_columnconfigure(6, weight=10)
option_frame.grid_columnconfigure(0, weight=10)
option_frame.grid_columnconfigure(6, weight=10)
option_frame.grid_rowconfigure(0, weight=3)
option_frame.grid_rowconfigure(1, weight=0)
option_frame.grid_rowconfigure(3, weight=1)
option_frame.grid_rowconfigure(5, weight=2)

#####


root.mainloop()