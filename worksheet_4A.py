"""
Stage: Development-01
@author: Umut Kalay, 120202016
@author: Yusuf Arda Altın, 119202054

Stage : Development -02
@author: Hamza Sallam 120200013
@author: Abdulrahman Aorfahli 119200028

"""

from ast import Break
from stat import UF_IMMUTABLE
import tkinter as tk
username="test"
password="test"

class LoginWindow:
   

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
            self.Check_User() 
            
    def Check_User(self):
        if self.txtUsername.get() == username and self.txtPassword.get() == password:
            self.window.destroy() # destroy the login page to display the homepage
            HomePage()

        else:
            print("Invalid user information.")  


# a new class for the new window to handle new events and widgets            
class HomePage:

    # constructor
    def __init__(self):
        self.window = tk.Tk()
        # a price variable to check what user added to cart
        self.price = 0
        # counter for each item the user choose from supermarket
        self.tmcount =0
        self.ricount=0
        self.mlkcount=0
        self.window.configure(bg='#8CA0D7')
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
        self.lblLoggedin = tk.Label(text="Super Market ",bg='#8CA0D7') 
        self.lbltomato = tk.Label(text="fresh tomato $2",bg='#8CA0D7')
        self.tomatiocount = tk.Label(text="",bg='#8CA0D7')
        self.addtocart1 = tk.Button(text="add to cart",bg='#8CA0D7')
        self.lblrice = tk.Label(text="rice  $14",bg='#8CA0D7')
        self.ricecount = tk.Label(text="",bg='#8CA0D7')
        self.addtocart2 = tk.Button(text="add to cart",bg='#8CA0D7')
        self.lblmilk = tk.Label(text="milk  $6",bg='#8CA0D7')
        self.milkcount = tk.Label(text="",bg='#8CA0D7')
        self.addtocart3 = tk.Button(text="add to cart",bg='#8CA0D7')
        self.pay = tk.Button(text="Pay",bg='#8CA0D7')
        self.total_price= tk.Label(text="",bg='#8CA0D7')



    """
        Add GUI elements to the layout of the frame. If it is necessary,
        you can add more elements.
    """
    def _addGUIElementsToFrame(self):
        self.lblLoggedin.grid(row=0, column=1, padx=0, pady=5)

        self.lbltomato.grid(row=1, column=0, padx=10, pady=5)
        self.tomatiocount.grid(row=1, column=1, padx=2, pady=2)
        self.addtocart1.grid(row=1, column=2, padx=10, pady=5)
        
        self.lblrice.grid(row=2, column=0, padx=10, pady=5)
        self.ricecount.grid(row=2, column=1, padx=2, pady=5)
        self.addtocart2.grid(row=2, column=2, padx=2, pady=2)

        self.lblmilk.grid(row=3, column=0, padx=10, pady=5)
        self.milkcount.grid(row=3, column=1, padx=2, pady=5)
        self.addtocart3.grid(row=3, column=2, padx=2, pady=2)

        self.pay.grid(row=4,column=0,padx=10,pady=15)
        self.total_price.grid(row=4,column=1,padx=10,pady=5)

        self.addtocart1.bind("<Button-1>", self.handle_click)
        self.addtocart2.bind("<Button-1>", self.handle_click)
        self.addtocart3.bind("<Button-1>", self.handle_click)
        self.pay.bind("<Button-1>", self.handle_click)


    """
        Action listener for the buttons. If "event.widget" is from
        one of the buttons, apply the related operation.

        :param event: action event for detecting which button is clicked
    """

    def handle_click(self, event):
        #if user choose  an item, display how many he chose and add it to price to print final price
        if event.widget == self.addtocart1:
            self.price = self.price + 2
            self.tmcount +=1
            self.tomatiocount.config(text='{}'.format(self.tmcount))
        if event.widget == self.addtocart2:
            self.price = self.price + 14 
            self.ricount +=1
            self.ricecount.config(text='{}'.format(self.ricount))    
        if event.widget == self.addtocart3:
            self.price = self.price + 6     
            self.mlkcount +=1
            self.milkcount.config(text='{}'.format(self.mlkcount))   
        if event.widget == self.pay:    
            self.total_price.config(text="Total Price is: {}".format(self.price))
        

# main method for testing the application
if __name__ == "__main__":
    LoginWindow()
