import tkinter as tk
from tkinter.ttk import *


class Window1:  # This window is for all the HOTEL ROOMS
    def __init__(self, master):
        window = Frame(master)
        self.master = master
        master.title("HOTEL ROOMS")
        label = Label(window, text="Rooms").grid(row=0, column=0)
        # take the data
        lst = [(11, 'K', 'Available'),
            (22, 'DQ', 'Available'),
            (13, 'DQK', 'Unavailable/Occupied'),
            (14, 'S', 'Unavailable/Dirty'),
            (35, 'S', 'Unavailable/Maintenance')]
        # find total number of rows and
        # columns in list
        rows = len(lst)
        cols = len(lst[0])
        gridLabels = []
        for r in range(rows):
            for c in range(cols):
                gridLabels.append(Label(window, text=lst[r][c], borderwidth=1).grid(row=r+1, column=c+1))
        window.pack()
        # Create labels, entries,buttons
        window_two_button = Button(master, text="Window 2", command=self.button_click)
        window_two_button.pack()

    def button_click(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window2(new_master)
        # If button is clicked, run this method and open window 2


class WindowTest:
    def __init__(self, master):
        x = 0

    # create buttons,entries,etc
    def button_method(self):
        # run this when button click to close window
        self.master.destroy()


class Window2:  # This window is for the 7-DAY LIST!
    def __init__(self, master):
        window = Frame(master)
        master.title("7-DAY LIST")
        label = Label(window, text="Rooms", background="pink").grid(row=0, column=0)
        # take the data
        lst = [(11, 'Raj', 'Mumbai', '', 'Marx.K', 'Marx.K', '', ''),
            (22, 'Aaryan', 'Pune', 'Bones.B', 'Bones.B', 'Bones.B', 'Bones.B', 'Bones.B'),
            (13, 'Vaishnavi', 'Mumbai', '', '', 'Lindberg.C', 'Lindberg.C', 'Lindberg.C'),
            (14, 'Rachna', 'Mumbai', '', '', '', 'Bamford.M', 'Bamford.M'),
            (35, 'Shubham', 'Delhi', '', '', '', '', 'Meyers.A')]
        # find total number of rows and
        # columns in list
        rows = len(lst)
        cols = len(lst[0])
        gridLabels = []
        for r in range(rows):
            for c in range(cols):
                gridLabels.append(Label(window, text=lst[r][c], borderwidth=1).grid(row=r+1, column=c+1))
        window.pack()
        # Create labels, entries,buttons

    def button_click(self):
        pass
        # If button is clicked, run this method and open window 2


class Window3:  # This window is for RESERVATION!
    def __init__(self, master):
        window = Frame(master)
        master.title("RESERVATIONS")
        label = Label(window, text="Rooms", background="pink").grid(row=0, column=0)
        # take the data
        lst = [(1, 'Raj', 'Mumbai', 19),
            (2, 'Aaryan', 'Pune', 18),
            (3, 'Vaishnavi', 'Mumbai', 20),
            (4, 'Rachna', 'Mumbai', 21),
            (5, 'Shubham', 'Delhi', 21)]
        # find total number of rows and
        # columns in list
        rows = len(lst)
        cols = len(lst[0])
        gridLabels = []
        for r in range(rows):
            for c in range(cols):
                gridLabels.append(Label(window, text=lst[r][c], borderwidth=1).grid(row=r+1, column=c+1))
        window.pack()
        # Create labels, entries,buttons

    def button_click(self):
        pass
        # If button is clicked, run this method and open window 2


class Window4:  # This window is for HOUSEKEEPING!
    def __init__(self, master):
        window = Frame(master)
        master.title("HOUSEKEEPING")
        label = Label(window, text="Rooms", background="pink").grid(row=0, column=0)
        # take the data
        lst = [('Server', 'Rm#', 'Type', 'Status', 'Bathroom', 'Towels', 'Sheets', 'Vacuum', 'Dusting', 'Electronics'),
            ('', '', '', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', '', '', '')]
        # find total number of rows and
        # columns in list
        rows = len(lst)
        cols = len(lst[0])
        gridLabels = []
        for r in range(rows):
            for c in range(cols):
                gridLabels.append(Label(window, text=lst[r][c], borderwidth=1).grid(row=r+1, column=c+1))
        window.pack()
        # Create labels, entries,buttons

    def button_click(self):
        pass
        # If button is clicked, run this method and open window 2


class Window5:  # This window is for GUEST PROFILE!
    def __init__(self, master):
        window = Frame(master)
        master.title("GUEST PROFILE")
        label = Label(window, text="Guests", background="pink").grid(row=0, column=0)
        # take the data
        lst = [('First Name', 'Last Name', 'Phone', 'Address', 'E-mail',  'ID Info (State, ID#)', 'Vehicle License Plate'),
            ('', '', '', '', '', '', ''),
            ('', '', '', '', '', '', ''),
            ('', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '')]
        # find total number of rows and
        # columns in list
        rows = len(lst)
        cols = len(lst[0])
        gridLabels = []
        for r in range(rows):
            for c in range(cols):
                gridLabels.append(Label(window, text=lst[r][c], borderwidth=1).grid(row=r+1, column=c+1))
        window.pack()
        # Create labels, entries,buttons

    def button_click(self):
        pass
        # If button is clicked, run this method and open window 2


class Window6:  # This window is for GUEST'S CURRENT STAY INFO!
    def __init__(self, master):
        window = Frame(master)
        master.title("GUEST'S CURRENT STAY INFO")
        label = Label(window, text="Guests", background="pink").grid(row=0, column=0)
        # take the data
        lst = [('Guest Name', 'Check In Date and Time', 'Expected Check Out Date and Time',  'Room Type', 'Room Number',
                'Room Rate ($/Day)', 'Total Charge', 'Payments Made', 'Balance'),
            ('', '', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', '', '')]
        # find total number of rows and
        # columns in list
        rows = len(lst)
        cols = len(lst[0])
        gridLabels = []
        for r in range(rows):
            for c in range(cols):
                gridLabels.append(Label(window, text=lst[r][c], borderwidth=1).grid(row=r+1, column=c+1))
        window.pack()
        # Create labels, entries,buttons

    def button_click(self):
        pass
        # If button is clicked, run this method and open window 2


class Window7:  # This window is for GUEST SEARCH!
    def __init__(self, master):
        window = Frame(master)
        master.title("GUEST SEARCH")
        label = Label(window, text="Search", background="pink").grid(row=0, column=0)
        # take the data
        lst = [('Guest First Name', 'Guest Last Name', 'Room Number', 'Phone Number', 'Street Address', 'Check In Date',
                'Checkout Date'),
               ('', '', '', '', '', '', '')]
        # find total number of rows and
        # columns in list
        rows = len(lst)
        cols = len(lst[0])
        gridLabels = []
        for r in range(rows):
            for c in range(cols):
                gridLabels.append(Label(window, text=lst[r][c], borderwidth=1).grid(row=r+1, column=c+1))
        window.pack()
        # Create labels, entries,buttons

    def button_click(self):
        pass
        # If button is clicked, run this method and open window 2


class Window8:  # This window is for DAILY REPORT!
    def __init__(self, master):
        window = Frame(master)
        master.title("DAILY REPORT")
        label = Label(window, text="Rooms", background="pink").grid(row=0, column=0)
        # take the data
        lst = [('Room Number', 'Guest Name', 'Date In', 'Date Out (if out)', 'Amount Paid'),
            (11, 'Aaryan', '11/12/13', '', '233.34'),
            ('', '', '', '', ''),
            ('', '', '', '', ''),
            ('', '', '', '', '')]
        # find total number of rows and
        # columns in list
        rows = len(lst)
        cols = len(lst[0])
        gridLabels = []
        for r in range(rows):
            for c in range(cols):
                gridLabels.append(Label(window, text=lst[r][c], borderwidth=1).grid(row=r+1, column=c+1))
        window.pack()
        # Create labels, entries,buttons
        # NEED TO GET A SUM OF THE CASH!

    def button_click(self):
        pass
        # If button is clicked, run this method and open window 2


def main():  # run mainloop
    root = tk.Tk()
    app = Window1(root)
    root.mainloop()


if __name__ == '__main__':
    main()
