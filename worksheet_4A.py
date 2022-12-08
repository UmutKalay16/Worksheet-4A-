"""
    Stage: Development-01
    @author: Umut Kalay, 120202016
    @author: Yusuf Arda Altın, 119202054
"""

from ast import Break
from stat import UF_IMMUTABLE
import tkinter as tk


class LoginWindow:
    username="Arda Umut"
    password="CMPE 331"

    # constructor
    def __init__(self):
        self.window = tk.Tk()

        self._initializeGUI()
        self._addGUIElementsToFrame()

        # start the GUI frame
        self.window.mainloop() 

    """
        Initialize GUI elements. If it is necessary, you can add
        more elements.

        ! PLEASE RENAME THE OBJECTS ACCORDING TO THEIR PURPOSES !
        ! YOU CAN ADD MORE ELEMENTS IF IT IS NECESSARY !
    """
    def _initializeGUI(self):
        self.lblUsername = tk.Label(text="Username")
        self.lblPassword = tk.Label(text="Password")

        self.txtUsername = tk.Entry(text="")
        self.txtPassword = tk.Entry()

        self.btnCancel = tk.Button(text="Cancel")
        self.btnEnter = tk.Button(text="Login")

        self.btnCancel.bind("<Button-1>", self.handle_click)
        self.btnEnter.bind("<Button-1>", self.handle_click)


    """
        Add GUI elements to the layout of the frame. If it is necessary,
        you can add more elements.
    """
    def _addGUIElementsToFrame(self):
        self.lblUsername.grid(row=0, column=0, padx=10, pady=5)
        self.txtUsername.grid(row=0, column=1, padx=10, pady=5)

        self.lblPassword.grid(row=1, column=0, padx=10, pady=5)
        self.txtPassword.grid(row=1, column=1, padx=10, pady=5)

        self.btnCancel.grid(row=2, column=0, padx=10, pady=5)
        self.btnEnter.grid(row=2, column=1, padx=10, pady=5)


    """
        Action listener for the buttons. If "event.widget" is from
        one of the buttons, apply the related operation.

        :param event: action event for detecting which button is clicked
    """

    def handle_click(self, event):
        if event.widget == self.btnCancel:
            self.window.destroy()
        elif event.widget == self.btnEnter:
            self.Check_User("Arda Umut", "CMPE 331") 
            
    def Check_User(self, username, password):
        if self.txtUsername.get() == username and self.txtPassword.get() == password:
            self.after_login_window = tk.Tk()
            self.after_login_window.title('Supermarket Blank Page')

        else:
            print("Invalid user information.")  
  

# main method for testing the application
if __name__ == "__main__":
    LoginWindow()
