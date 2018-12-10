# Multi-frame tkinter application v2.3
import os
import sys
import tkinter as tk
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from services.login import loginVerification
import loginUI
import menuUI

class MainUi(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.frames = {}
        
        for F in (loginUI.LoginUi, menuUI.MenuUi):
            frame = F(container, self)
            self.frames[F] = frame
            
            frame.grid(row = 0, column = 0, sticky="nsew")
        
        self.show_frame(loginUI.LoginUi)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
if __name__ == "__main__":
    app = MainUi() 
    app.mainloop()