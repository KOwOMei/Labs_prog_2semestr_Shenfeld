import tkinter as tk

class IceCreamStandGUI:
    def __init__(self, flavors):
        self.flavors = flavors
        self.window = tk.Tk()
        self.window.title("Ice Cream Cafe Menu")
        
        tk.Label(self.window, text="List of ice cream flavors:").grid(row=0, column=0)
        
        for i in range(len(self.flavors)):
            tk.Label(self.window, text=self.flavors[i]).grid(row=i+1, column=0)

myIceCreamStandGUI = IceCreamStandGUI(["vanilla", "strawberry", "chocolate", "caramel"])
myIceCreamStandGUI.window.mainloop()
