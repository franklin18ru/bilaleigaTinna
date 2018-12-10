from tkinter import *
import csv

root = Tk()

root.title("Pantanir")
screen_width = root.winfo_screenwidth() #Gets the screen width
screen_height = root.winfo_screenheight() #Gets the screen height
root.configure(bg="#5A67C") # Changes background color of frame
root.geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame





bilaleigaTinna = Label(root, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
label1 = Label(root, text="Verðskrá",bg="#5A6D7C",fg="white")
label2 = Label(root,
                text="",
                bd=4,
                bg="#5A6D7C",
                relief="ridge",
                font="Times 32",
                width=90,
                height=20)

line1 = Label(root, text="____________________________",bg="#5A6D7C",fg="white")
line2 = Label(root, text="____________________________",bg="#5A6D7C",fg="white")





#Create Buttons
edit = Button(root, text="Edit", bg="white", fg="black", width=15, height=1)
escape_button = Button(root, text="Esc - Til baka", bg="#9E4848", fg="white", width=15, height=1)



with open('data/pricelist.csv', 'r', newline="") as pricelist:
    csv_reader = csv.reader(pricelist)
    next(csv_reader)
    row_num = 6
    column_num = 3
    counter = 0
    

    for item in csv_reader:
        label3 = Label(label2, text=item[0],bg="#5A6D7C",fg="white",width=22, height=2)
        label3.config(font=("Courier", 16))
        label3.grid(row = row_num, column=column_num)
        label4 = Label(label2, text=item[1] +" kr." ,bg="#5A6D7C",fg="white", width=22, height=2)
        label4.config(font=("Courier", 16))
        label4.grid(row = row_num, column=column_num+1)
        counter += 1
        if counter == 1:
            row_num += 1
            counter = 0
            column_num = 3
    
#label2 = Label(root,
            #text="",
            #bd=4,
            #bg="#5A6D7C",
            #relief="ridge",
            #font="Times 32",
            #width=40,
            #height=10,
            #anchor=CENTER)









#configure labels
bilaleigaTinna.config(font=("Courier", 32))
label1.config(font=("Courier", 28))
line1.config(font=("Courier", 28))
line2.config(font=("Courier", 28))
edit.config( font=("Courier", 16))
escape_button.config( font=("Courier", 16))





#Position widgets

#labels
bilaleigaTinna.grid(row=1, column=3)
label1.grid(row=3, column=3)
label2.grid(row=7, column=3)
line1.grid(row=2,column=3)
line2.grid(row=10,column=3)
edit.grid(row=9, column= 3)
escape_button.grid(row=11, column=3)




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
