import tkinter as tk
from tkinter.ttk import *
class Window1:
    def __init__(self, master):
        window = Frame(master)
        label = Label(window, text="Rooms").grid(row=0,column=0)
        # take the data 
        lst = [(1,'Raj','Mumbai',19), 
            (2,'Aaryan','Pune',18), 
            (3,'Vaishnavi','Mumbai',20), 
            (4,'Rachna','Mumbai',21), 
            (5,'Shubham','Delhi',21)] 
        # find total number of rows and 
        # columns in list 
        rows = len(lst) 
        cols = len(lst[0]) 
        gridLabels = []
        for r in range(rows):
            for c in range(cols):
                gridLabels.append(Label(window, text=lst[r][c],borderwidth=1 ).grid(row=r+1,column=c+1))
        window.pack()
        # Create labels, entries,buttons
    def button_click(self):
        pass
        # If button is clicked, run this method and open window 2

class Window2:
    def __init__(self, master):
        x = 0
        #create buttons,entries,etc
    def button_method(self):
        #run this when button click to close window
        self.master.destroy()

def main(): #run mainnloop  
    root = tk.Tk()
    app = Window1(root)
    root.mainloop()

if __name__ == '__main__':
    main()