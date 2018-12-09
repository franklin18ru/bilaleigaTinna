import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import tkinter as tk
import mainUi
import menuUI

from services.login import loginVerification


class LoginUi(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#5A6D7C")
        screen_width = self.winfo_screenwidth() #Gets the screen width
        screen_height = self.winfo_screenheight() #Gets the screen height
        self.winfo_toplevel().configure(bg="#5A6D7C") # Changes background color of frame
        self.winfo_toplevel().geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame
    
        #login frame
        loginFrame1 = tk.Frame(self, bg="#5A6D7C")
        loginFrame2 = tk.Frame(self, bg="#5A6D7C")

        #Create lables
        bilaleigaTinna = tk.Label(self, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
        label1 = tk.Label(self, text="Innskráning",bg="#5A6D7C",fg="white")
        username = tk.Label(loginFrame1, text="Starfsnúmer:",bg="#5A6D7C",fg="white")
        password = tk.Label(loginFrame2, text="Lykilorð:",bg="#5A6D7C",fg="white")

        #Create Entries
        self.usernameInput = tk.Entry(loginFrame1, width=20, font=("Courier", 20))
        self.passwordInput = tk.Entry(loginFrame2, show="*", width=20, font=("Courier", 20))

        #Configure Lables
        bilaleigaTinna.config(font=("Courier", 32))
        label1.config(font=("Courier", 28))
        username.config(font=("Courier", 22))
        password.config(font=("Courier", 22))

        
        #Show labels
        bilaleigaTinna.pack(side="top",fill="x")
        label1.pack( side="top",fill="x",ipady=100)

        #show loginframes
        loginFrame1.pack(fill="x",side="top")
        loginFrame2.pack(fill="x",side="top")

        #Show username and input
        username.pack(side="top",fill="x")
        self.usernameInput.pack(side="top")

        #show password and input
        password.pack(side="top", fill="x")
        self.passwordInput.pack(side="top")
        
        #Create buttons
        confirm = tk.Button(self, text="Innskrá", bg="#424242", fg="white", width=8, height=1,font=("Courier",16), command=lambda:self.verifyButton(controller))
        confirm.pack(side="top", pady="20",ipadx="105")

    def verifyButton(self, controller):
        usernameInput = int(self.usernameInput.get())
        passwordInput = self.passwordInput.get()
        self.passwordInput.delete(0, "end")
        self.usernameInput.delete(0, "end")
        verifyLogin = loginVerification(usernameInput,passwordInput)
        verification = verifyLogin.verify()
        if verification == False:
            try:
                self.error.destroy()
                self.error = tk.Label(self, text="Rangt starfsnúmer eða lykilorð", bg="red", fg="white",font=("Courier",14))
                self.error.pack()
            except Exception:
                self.error = tk.Label(self, text="Rangt starfsnúmer eða lykilorð", bg="red", fg="white",font=("Courier",14))
                self.error.pack()
        elif verification == True:
            try:
                self.error.destroy()
                controller.show_frame(menuUI.MenuUi)
            except Exception:
                controller.show_frame(menuUI.MenuUi)
# def main():
#     verification = False
#     def runLoginUi():
#         def verify():
#             verifyButton(usernameInput,passwordInput,root)
#         def verifyButton(usernameInput, passwordInput, root):
#             global verification
#             usernameInput = int(usernameInput.get())
#             passwordInput = passwordInput.get()
#             verifyLogin = loginVerification(usernameInput,passwordInput)
#             verification = verifyLogin.verify()
#             if verification == True:
#                 END
#             if verification == False:
#                 error = Button(root, text="Rangt starfsnúmer eða lykilorð", bg="red", fg="white",font=("Courier",14))
#                 error.grid(row=8,column=2)


        
#         #create frame
#         root = Tk()
#         root.title("Bílaleiga Tinna")
#         screen_width = root.winfo_screenwidth() #Gets the screen width
#         screen_height = root.winfo_screenheight() #Gets the screen height
#         root.configure(bg="#5A6D7C") # Changes background color of frame
#         root.geometry(str(screen_width)+"x"+str(screen_height)) #Sets the size of frame


#         #Create labels
#         bilaleigaTinna = Label(root, text="Bílaleiga Tinna",bg="#5A6D7C",fg="white")
#         label1 = Label(root, text="Innskráning",bg="#5A6D7C",fg="white")
#         username = Label(root, text="Starfsnúmer:",bg="#5A6D7C",fg="white")
#         password = Label(root, text="Lykilorð:",bg="#5A6D7C",fg="white")



#         #Create the entry fields
#         usernameInput = Entry(root, width=20, font=("Courier", 20))
#         passwordInput = Entry(root, show="*", width=20, font=("Courier", 20))


#         #Create buttons
#         confirm = Button(root, text="Innskrá", bg="#424242", fg="white", width=8, height=1,font=("Courier",16), command=verify)
#         #################################################################################

#         #configure labels
#         bilaleigaTinna.config(font=("Courier", 32))
#         label1.config(font=("Courier", 28))
#         username.config(font=("Courier", 22))
#         password.config(font=("Courier", 22))



#         #Position widgets

#         #labels
#         bilaleigaTinna.grid(row=1, column=2, sticky = NSEW)
#         label1.grid(row=3, column=2, sticky = NSEW)
#         username.grid(row=4, column=0, sticky = E)
#         password.grid(row=5, column=0, sticky = E)

#         #Entries
#         usernameInput.grid(row=4, column=2)
#         passwordInput.grid(row=5, column=2)
#         confirm.grid(row=6, column=2)

#         #position frame
#         root.grid_rowconfigure(0, weight=1)
#         root.grid_rowconfigure(2, weight=1)
#         root.grid_rowconfigure(7, weight=1)
#         root.grid_rowconfigure(9, weight=3)
#         root.grid_columnconfigure(0, weight=1)
#         root.grid_columnconfigure(9, weight=1)


#         #################################################################################


#         root.mainloop()

#     runLoginUi()
#     return verification
# main()