import tkinter as tk
from tkinter.ttk import *
import datetime as dt
from PIL import Image
import os
class Window1:  # This window is for all the HOTEL ROOMS
    def __init__(self, master):
        window = Frame(master)
        master.title("HOTEL ROOMS")
        label = Label(window, text="Rooms",anchor='W').grid(row=0, column=0)
        Label(window, text="Room #").grid(row=1, column=0)
        Label(window, text="Status").grid(row=1, column=1)
        # take the data
        lst = [(101, 'Available'),
            (102, 'K','Available'),
            (103, 'DQ','Unavailable/Occupied'),
            (104, 'DQK','Unavailable/Dirty'),
            (105, 'S','Unavailable/Maintenance')]
        # find total number of rows and
        # columns in list
        rows = len(lst)
        cols = len(lst[0])
        gridLabels = []
        for r in range(rows):
            for c in range(cols):
                gridLabels.append(Label(window, text=lst[r][c], borderwidth=1).grid(row=r+2, column=c))
        window.pack()
        # Create labels, entries,buttons

    def button_click(self):
        pass
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
        label = Label(window, text="Rooms", background="pink",anchor='W').grid(row=0, column=0)
        Label(window, text="--Occupant--", background="pink").grid(row=0, column=4)
        Label(window, text="Room #", background="pink").grid(row=1, column=0)
        Label(window, text="Monday", background="pink").grid(row=1, column=1)
        Label(window, text="Tuesday", background="pink").grid(row=1, column=2)
        Label(window, text="Wednesday", background="pink").grid(row=1, column=3)
        Label(window, text="Thursday", background="pink").grid(row=1, column=4)
        Label(window, text="Friday", background="pink").grid(row=1, column=5)
        Label(window, text="Saturday", background="pink").grid(row=1, column=6)
        Label(window, text="Sunday", background="pink").grid(row=1, column=7)
        # take the data
        lst = [(101, 'Raj', 'Mumbai', '', 'Marx.K', 'Marx.K', '', ''),
            (102, 'Aaryan', 'Pune', 'Bones.B', 'Bones.B', 'Bones.B', 'Bones.B', 'Bones.B'),
            (103, 'Vaishnavi', 'Mumbai', '', '', 'Lindberg.C', 'Lindberg.C', 'Lindberg.C'),
            (104, 'Rachna', 'Mumbai', '', '', '', 'Bamford.M', 'Bamford.M'),
            (105, 'Shubham', 'Delhi', '', '', '', '', 'Meyers.A')]
        # find total number of rows and
        # columns in list
        rows = len(lst)
        cols = len(lst[0])
        gridLabels = []
        for r in range(rows):
            for c in range(cols):
                gridLabels.append(Label(window, text=lst[r][c], borderwidth=1).grid(row=r+2, column=c))
        window.pack()
        # Create labels, entries,buttons

    def button_click(self):
        pass
        # If button is clicked, run this method and open window 2


class Window3:  # This window is for RESERVATION!
    def __init__(self, master):
        window = Frame(master)
        master.title("RESERVATIONS")
        Label(window, text="Reservations", background="pink",anchor='w').grid(row=0, column=0)
        Label(window, text="First", background="pink").grid(row=1, column=0)
        Label(window, text="Last", background="pink").grid(row=1, column=1)
        Label(window, text="Date Made", background="pink").grid(row=1, column=2)
        Label(window, text="Check-in", background="pink").grid(row=1, column=3)
        Label(window, text="Check-out", background="pink").grid(row=1, column=4)
        Label(window, text="Room Type", background="pink").grid(row=1, column=5)
        Label(window, text="Website", background="pink").grid(row=1, column=6)
        Label(window, text="Rate", background="pink").grid(row=1, column=7)
        Label(window, text="Total Charge", background="pink").grid(row=1, column=8)
        # take the data
        lst = [('Raj', 'Mumbai', dt.date(2020, 10, 5), dt.date(2020, 10, 10), dt.date(2020, 10, 15), 'S', 'booking.com', '$7', 5*7),
            ('Aaryan', 'Pune', dt.date(2020, 10, 5), dt.date(2020, 10, 10), dt.date(2020, 10, 15), 'S', 'booking.com', '$7', 5*7),
            ('Shubham', 'Delhi', dt.date(2020, 10, 5), dt.date(2020, 10, 10), dt.date(2020, 10, 15), 'S', 'booking.com', '$7', 5*7),]
        # find total number of rows and
        # columns in list
        rows = len(lst)
        cols = len(lst[0])
        gridLabels = []
        for r in range(rows):
            for c in range(cols):
                gridLabels.append(Label(window, text=lst[r][c], borderwidth=1).grid(row=r+2, column=c))
        window.pack()
        # Create labels, entries,buttons

    def button_click(self):
        pass
        # If button is clicked, run this method and open window 2


class Window4:  # This window is for HOUSEKEEPING!
    def __init__(self, master):
        window = Frame(master)
        master.title("HOUSEKEEPING")
        label = Label(window, text="Rooms", background="pink",anchor='w').grid(row=0, column=0)
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
                gridLabels.append(Label(window, text=lst[r][c], borderwidth=1).grid(row=r+1, column=c))
        window.pack()
        # Create labels, entries,buttons

    def button_click(self):
        pass
        # If button is clicked, run this method and open window 2


class Window5:  # This window is for GUEST PROFILE!
    def __init__(self, master):
        window = Frame(master)
        master.title("GUEST PROFILE")
        label = Label(window, text="Guest", background="pink",anchor='w').grid(row=0, column=0)
        lst = [('First Name', 'Last Name', 'Phone', 'Address', 'E-mail',  'ID Info (State, ID#)', 'Vehicle License Plate'),
            ('', '', '', '', '', '', '')]
        # find total number of rows and
        # columns in list
        rows = len(lst)
        cols = len(lst[0])
        gridLabels = []
        for r in range(rows):
            for c in range(cols):
                gridLabels.append(Label(window, text=lst[r][c], borderwidth=1).grid(row=r+2, column=c))
        window.pack()
        # Create labels, entries,buttons

    def button_click(self):
        pass
        # If button is clicked, run this method and open window 2


class Window6:  # This window is for GUEST'S CURRENT STAY INFO!
    def __init__(self, master):
        window = Frame(master)
        master.title("GUEST'S CURRENT STAY INFO")
        label = Label(window, text="Guests", background="pink",anchor='w').grid(row=0, column=0)
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
                gridLabels.append(Label(window, text=lst[r][c], borderwidth=1).grid(row=r+1, column=c))
        window.pack()
        # Create labels, entries,buttons

    def button_click(self):
        pass
        # If button is clicked, run this method and open window 2


class Window7:  # This window is for GUEST SEARCH!
    def __init__(self, master):
        window = Frame(master)
        master.title("GUEST SEARCH")
        label = Label(window, text="Search", background="pink",anchor='w').grid(row=0, column=0)
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
                gridLabels.append(Label(window, text=lst[r][c], borderwidth=1).grid(row=r+1, column=c))
        window.pack()
        # Create labels, entries,buttons

    def button_click(self):
        pass
        # If button is clicked, run this method and open window 2


class Window8:  # This window is for DAILY REPORT!
    def __init__(self, master):
        window = Frame(master)
        master.title("DAILY REPORT")
        label = Label(window, text="Rooms", background="pink",anchor='w').grid(row=0, column=0)
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
                gridLabels.append(Label(window, text=lst[r][c], borderwidth=1).grid(row=r+1, column=c))
        window.pack()
        # Create labels, entries,buttons
        # NEED TO GET A SUM OF THE CASH!

    def button_click(self):
        pass
        # If button is clicked, run this method and open window 2


def main():  # run mainloop
    root = tk.Tk()
    app = Window5(root)
    root.mainloop()


if __name__ == '__main__':
    main()
