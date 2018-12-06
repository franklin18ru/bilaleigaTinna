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


# A lable that should change for what the user clicks on:
label1 = Label(root, text="Bílar",bg="#5A6D7C",fg="white") #setting a default value
label1.config(font=("Courier", 24)) #setting font
#here there should be an if statement to change the lable to the correct word:
label1.config(text="Jeppar") #changing the default value
label1.grid(row=3, column=3) #printing new value




cars = ["Toyoya Hilux", "Suzuki", "Range Rover", "G-Class", "Apa bíll"]
row_num = 3
column_num = 2
counter = 0
for item in cars:
    label1 = Button(root, text=item ,bg="#424242",fg="white", width=22, height=2)
    label1.config(font=("Courier", 16))
    label1.grid(row = row_num, column=column_num)
    counter += 1
    column_num +=1
    if counter == 3:
        row_num += 1
        counter = 0
        column_num = 2



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



line1 = Label(root, text="____________________________",bg="#5A6D7C",fg="white")
line2 = Label(root, text="____________________________",bg="#5A6D7C",fg="white")


# #Create buttons
# jeep = Button(root, text="1. Jeppar", bg="#424242", fg="white", width=22, height=2)
# small_car = Button(root, text="2. Smábílar", bg="#424242", fg="white", width=22, height=2)
# sedan = Button(root, text="3. Fólksbílar", bg="#424242", fg="white", width=22, height=2)
# luxury_car = Button(root, text="4. Lúxurbílar", bg="#424242", fg="white", width=22, height=2)
# all_cars = Button(root, text="5. Allir bílar", bg="#424242", fg="white", width=22, height=2)
# back = Button(root, text="Esc - Til baka", bg="#C8C8C8", fg="black", width=18, height=1)

# ###

# #configure labels
bilaleigaTinna.config(font=("Courier", 32))
# label1.config(font=("Courier", 24))
# jeep.config( font=("Courier",16))
# small_car.config( font=("Courier",16))
# sedan.config( font=("Courier",16))
# luxury_car.config( font=("Courier",16))
# all_cars.config( font=("Courier",16))
# back.config(font=("Courier",16))
line1.config(font=("Courier", 28))
line2.config(font=("Courier", 28))



# #positioning everything on the screen
bilaleigaTinna.grid(row=1, column=3)
# label1.grid(row=3, column=3)
# jeep.grid(row=4, column=2)
# small_car.grid(row=4, column=3)
# sedan.grid(row=4, column=4)
# luxury_car.grid(row=8, column=2)
# all_cars.grid(row=8, column=3)
# back.grid(row=10, column=3)
line1.grid(row=2,column=3)
line2.grid(row=9,column=3)
 


# #position frame
root.grid_rowconfigure(0, weight=3)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(5, weight=2)
root.grid_rowconfigure(9, weight=2)
root.grid_rowconfigure(11, weight=5)
root.grid_columnconfigure(0, weight=10)
root.grid_columnconfigure(6, weight=10)


# #####


root.mainloop()