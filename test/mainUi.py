# Multi-frame tkinter application v2.3
import os
import sys
import tkinter as tk
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from services.login import loginVerification

class MainUi(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(LoginUi)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class LoginUi(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,bg="#5A6D7C")
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
        username.pack(side="left",fill="x")
        self.usernameInput.pack(side="right",fill="x")

        #show password and input
        password.pack(side="left", fill="x")
        self.passwordInput.pack(side="right",fill="x")
        
        #Create buttons
        confirm = tk.Button(self, text="Innskrá", bg="#424242", fg="white", width=8, height=1,font=("Courier",16), command=self.verifyButton)
        confirm.pack(side="right", pady="20",ipadx="105")

    def verifyButton(self):
        global usernameInput
        global passwordInput
        self.usernameInput = int(self.usernameInput.get())
        self.passwordInput = self.passwordInput.get()
        verifyLogin = loginVerification(self.usernameInput,self.passwordInput)
        verification = verifyLogin.verify()
        if verification == False:
            error = tk.Button(self, text="Rangt starfsnúmer eða lykilorð", bg="red", fg="white",font=("Courier",14))
            error.pack()
        if verification == True:
            tk.Button(self, text="Return to start page",
              command=lambda: master.switch_frame(MainUi))

        

class MenuUi(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page one").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(LoginUi)).pack()

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page two").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(LoginUi)).pack()

if __name__ == "__main__":
    app = MainUi()
    app.mainloop()