from tkinter import *

root = Tk()

root.title("Pantanir")
screen_width = root.winfo_screenwidth() #Gets the screen width
screen_height = root.winfo_screenheight() #Gets the screen height
root.configure(bg="#5A6D7C") # Changes background color of frame
root.geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame







bilaleigaTinna = Label(root, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
label1 = Label(root, text="Pantanir",bg="#5A6D7C",fg="white")
line1 = Label(root, text="____________________________",bg="#5A6D7C",fg="white")
line2 = Label(root, text="____________________________",bg="#5A6D7C",fg="white")


#Create Buttons
costomer_order = Button(root,    text="1. Leita af pöntun", bg="#424242", fg="white", width=22, height=3)
costomer_allorders = Button(root,   text="2. Allar pantanir", bg="#424242", fg="white", width=22, height=3)
#costomer_allorders = Button(root,       text="3. Allar pantanir", bg="#424242", fg="white", width=22, height=3)
escape_button = Button(root, text="Esc - Til baka", bg="white", fg="black", width=15, height=1)

#ef klikkað er á "Leita eftir viðskiptavini" þá keyrist upp orders_search_customerUi skjalið
#ef klikkað er á "Leita eftir bíl" þá keyrist upp orders_search_customerUi nema með öðruvísi texta
#ef klikað er  á "Allar pantanir" ________________________________''_______________________________




#configure labels
bilaleigaTinna.config(font=("Courier", 32))
label1.config(font=("Courier", 28))
costomer_order.config( font=("Courier",16))
costomer_allorders.config( font=("Courier",16))
#costomer_allorders.config( font=("Courier",16))
escape_button.config( font=("Courier", 16))
line1.config(font=("Courier", 28))
line2.config(font=("Courier", 28))


#Position widgets

#labels
bilaleigaTinna.grid(row=1, column=3)
label1.grid(row=3, column=3)
costomer_order.grid(row=4, column=3)
costomer_allorders.grid(row=5, column=3)
#costomer_allorders.grid(row=5, column=4)
escape_button.grid(row=10, column=3)
line1.grid(row=2,column=3)
line2.grid(row=9,column=3)



#position frame
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(3, weight=0)
root.grid_rowconfigure(11, weight=2)
root.grid_rowconfigure(9, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(7, weight=1)

#root.grid_rowconfigure(0, weight=3)
#root.grid_rowconfigure(1, weight=0)
#root.grid_rowconfigure(2, weight=1)
#root.grid_rowconfigure(3, weight=1)
#root.grid_rowconfigure(5, weight=2)
#root.grid_rowconfigure(9, weight=2)
#root.grid_rowconfigure(11, weight=5)
#root.grid_columnconfigure(0, weight=10)
#root.grid_columnconfigure(7, weight=10)
#root.grid_columnconfigure(1, weight=0)






root.mainloop()
