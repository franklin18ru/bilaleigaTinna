from tkinter import *
import csv

root = Tk()

root.title("Pantanir")
screen_width = root.winfo_screenwidth() #Gets the screen width
screen_height = root.winfo_screenheight() #Gets the screen height
root.configure(bg="#5A6D7C") # Changes background color of frame
root.geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame







bilaleigaTinna = Label(root, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
customers = Label(root, text="Viðskiptavinir",bg="#5A6D7C",fg="white")
full_name = Label(root, text="Nafn",bg="#5A6D7C",fg="white")
ssn = Label(root, text="Kennitala",bg="#5A6D7C",fg="white")
email = Label(root, text="Email",bg="#5A6D7C",fg="white")
phone_number = Label(root, text="Símanúmer",bg="#5A6D7C",fg="white")
line1 = Label(root, text="____________________________",bg="#5A6D7C",fg="white")
line2 = Label(root, text="____________________________",bg="#5A6D7C",fg="white")


#Create Buttons
#escape_button = Button(root, text="Esc - Til baka", bg="#9E4848", fg="white", width=15, height=1)
#edit = Button(root, text="Edit", bg="white", fg="black", width=15, height=1)

with open('data/customers.csv', 'r', newline="") as customers:
    csv_reader = csv.reader(customers)
    next(csv_reader)
    row_num = 4
    column_num = 0
    counter = 0
    for item in csv_reader:
        label3 = Label(root, text=item,bg="#5A6D7C",fg="white",width=22, height=2)
        label3.config(font=("Courier", 16))
        label3.grid(row = row_num, column=column_num)
        #label4 = Label(label2, text=item[1] +" kr." ,bg="#5A6D7C",fg="white", width=22, height=2)
        #label4.config(font=("Courier", 16))
        #label4.grid(row = row_num, column=column_num+1)
        counter += 1
        if counter == 3:
            row_num += 1
            counter = 0
            column_num = 0

#configure labels
bilaleigaTinna.config(font=("Courier", 32))
customers.config(font=("Courier", 28))
full_name.config(font=("Courier", 16))
ssn.config(font=("Courier", 16))
email.config(font=("Courier", 16))
phone_number.config(font=("Courier", 16))

line1.config(font=("Courier", 28))
line2.config(font=("Courier", 28))
#edit.config( font=("Courier", 16))
#escape_button.config( font=("Courier", 16))





#Position widgets

#labels
bilaleigaTinna.grid(row=1, column=3)
customers.grid(row=2, column=3)
full_name.grid(row=3, column=0)
ssn.grid(row=3,column=1)
email.grid(row=3,column=4)
phone_number.grid(row=3,column=7)
line1.grid(row=2, column=3)
line2.grid(row=10,column =3)

#edit.grid(row=9, column= 3)
#escape_button.grid(row=11, column=3)




#position frame
root.grid_rowconfigure(0, weight=2)
root.grid_rowconfigure(2, weight=0)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(4, weight=0)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(11, weight=2)
root.grid_rowconfigure(9, weight=1)

root.grid_rowconfigure(12, weight=3)
#root.grid_rowconfigure(2, weight=0)
#root.grid_rowconfigure(2, weight=0)


root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(7, weight=1)


root.mainloop()