import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) #The golden import line (No changing plz)
from GUI.loginUI import main
from GUI.menuUI import menuMain



login = main()

if login == True:
    menuMain()
