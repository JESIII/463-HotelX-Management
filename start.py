import tkinter as tk
from tkinter.ttk import *
import datetime as dt
#from PIL import Image
import os


class Window1:  # This window is for all the HOTEL ROOMS
    def __init__(self, master):
        window = Frame(master)
        self.master = master
        master.title("HOTEL ROOMS")
        currRows = 0
        label = Label(window, text="Rooms",anchor='w').grid(row=0, column=0)
        Label(window, text="Room #").grid(row=1, column=0)
        Label(window, text="Type").grid(row=1, column=1)
        Label(window, text="Status").grid(row=1, column=2)
        # take the data
        lst = [(101, 'K', 'Available'),
            (102, 'K', 'Available'),
            (103, 'DQ', 'Unavailable/Occupied'),
            (104, 'DQK', 'Unavailable/Dirty'),
            (105, 'S', 'Unavailable/Maintenance')]
        # find total number of rows and
        # columns in list
        rows = len(lst)
        cols = len(lst[0])
        gridLabels = []
        for r in range(rows):
            for c in range(cols):
                gridLabels.append(Label(window, text=lst[r][c], borderwidth=1).grid(row=r+2, column=c))
                currRows = r+2
        # Create labels, entries,buttons
        Button(window, text="Room List", command=self.button_click1).grid(row=currRows+1, column=0)
        Button(window, text="Weekly List", command=self.button_click2).grid(row=currRows+1, column=1)
        Button(window, text="Reservation", command=self.button_click3).grid(row=currRows+1, column=2)
        Button(window, text="Housekeeping", command=self.button_click4).grid(row=currRows+1, column=3)
        Button(window, text="Guest Profiles", command=self.button_click5).grid(row=currRows+1, column=4)
        Button(window, text="Current Stay", command=self.button_click6).grid(row=currRows+1, column=5)
        Button(window, text="Guest Search", command=self.button_click7).grid(row=currRows+1, column=6)
        Button(window, text="Daily Report", command=self.button_click8).grid(row=currRows+1, column=7)
        window.pack()

    def button_click1(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window1(new_master)

    def button_click2(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window2(new_master)

    def button_click3(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window3(new_master)

    def button_click4(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window4(new_master)

    def button_click5(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window5(new_master)

    def button_click6(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window6(new_master)

    def button_click7(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window7(new_master)

    def button_click8(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window8(new_master)
        # If button is clicked, run this method and open window 2


class Window2:  # This window is for the 7-DAY LIST!
    def __init__(self, master):
        window = Frame(master)
        self.master = master
        master.title("7-DAY LIST")
        currRows = 0
        label = Label(window, text="Rooms", background="pink", anchor='w').grid(row=0, column=0)
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
                currRows = r+2
        # Create labels, entries,buttons
        Button(window, text="Room List", command=self.button_click1).grid(row=currRows+1, column=0)
        Button(window, text="Weekly List", command=self.button_click2).grid(row=currRows+1, column=1)
        Button(window, text="Reservation", command=self.button_click3).grid(row=currRows+1, column=2)
        Button(window, text="Housekeeping", command=self.button_click4).grid(row=currRows+1, column=3)
        Button(window, text="Guest Profiles", command=self.button_click5).grid(row=currRows+1, column=4)
        Button(window, text="Current Stay", command=self.button_click6).grid(row=currRows+1, column=5)
        Button(window, text="Guest Search", command=self.button_click7).grid(row=currRows+1, column=6)
        Button(window, text="Daily Report", command=self.button_click8).grid(row=currRows+1, column=7)
        window.pack()

    def button_click1(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window1(new_master)

    def button_click2(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window2(new_master)

    def button_click3(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window3(new_master)

    def button_click4(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window4(new_master)

    def button_click5(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window5(new_master)

    def button_click6(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window6(new_master)

    def button_click7(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window7(new_master)

    def button_click8(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window8(new_master)
        # If button is clicked, run this method and open window 2


class Reservation:  # reservation object for window3, the RESERVATIONS
    def __init__(self, First, Last, DateMade, CheckIn, CheckOut, RoomType, Website, Rate, TotalCharge):
        self.First = First
        self.Last = Last
        self.DateMade = DateMade
        self.CheckIn = CheckIn
        self.CheckOut = CheckOut
        self.RoomType = RoomType
        self.Website = Website
        self.Rate = Rate
        self.TotalCharge = TotalCharge
        self.variableArray = [self.First, self.Last, self.DateMade, self.CheckIn, self.CheckOut, self.RoomType,
                              self.Website, self.Rate, self.TotalCharge]


class Window3:  # This window is for RESERVATION!
    def __init__(self, master):
        window = Frame(master)
        self.master = master
        master.title("RESERVATIONS")
        Label(window, text="Reservations", background="pink", anchor='w').grid(row=0, column=0)
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
        lst = [Reservation("Timmothy", "Leary", dt.date(2020, 10, 5), dt.date(2020, 10, 10), dt.date(2020, 10, 15),
                           'S', 'booking.com', '$7', 5*7),
               Reservation("Charles", "Manson", dt.date(2020, 10, 5), dt.date(2020, 10, 10), dt.date(2020, 10, 15),
                           'S', 'booking.com', '$7', 5*7),
               Reservation("Sharon", "Tate", dt.date(2020, 10, 5), dt.date(2020, 10, 10), dt.date(2020, 10, 15),
                           'S', 'booking.com', '$7', 5*7)]
        # find total number of rows and columns in list
        rows = len(lst)
        cols = 8  # number of variables in a reservation object
        currRows = 0
        gridLabels = []
        for r in range(rows):
            for c in range(cols):
                gridLabels.append(Label(window, text=lst[r].variableArray[c], borderwidth=1).grid(row=r+2, column=c))
                currRows = r+2

        Button(window, text="Room List", command=self.button_click1).grid(row=currRows+1, column=0)
        Button(window, text="Weekly List", command=self.button_click2).grid(row=currRows+1, column=1)
        Button(window, text="Reservation", command=self.button_click3).grid(row=currRows+1, column=2)
        Button(window, text="Housekeeping", command=self.button_click4).grid(row=currRows+1, column=3)
        Button(window, text="Guest Profiles", command=self.button_click5).grid(row=currRows+1, column=4)
        Button(window, text="Current Stay", command=self.button_click6).grid(row=currRows+1, column=5)
        Button(window, text="Guest Search", command=self.button_click7).grid(row=currRows+1, column=6)
        Button(window, text="Daily Report", command=self.button_click8).grid(row=currRows+1, column=7)
        window.pack()

    def button_click1(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window1(new_master)

    def button_click2(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window2(new_master)

    def button_click3(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window3(new_master)

    def button_click4(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window4(new_master)

    def button_click5(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window5(new_master)

    def button_click6(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window6(new_master)

    def button_click7(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window7(new_master)

    def button_click8(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window8(new_master)
        # Create labels, entries,buttons


class Window4:  # This window is for HOUSEKEEPING!
    def __init__(self, master):
        window = Frame(master)
        self.master = master
        master.title("HOUSEKEEPING")
        label = Label(window, text="Rooms", background="pink",anchor='w').grid(row=0, column=0)
        currRows = 0
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
                currRows = r+1
        Button(window, text="Room List", command=self.button_click1).grid(row=currRows+1, column=0)
        Button(window, text="Weekly List", command=self.button_click2).grid(row=currRows+1, column=1)
        Button(window, text="Reservation", command=self.button_click3).grid(row=currRows+1, column=2)
        Button(window, text="Housekeeping", command=self.button_click4).grid(row=currRows+1, column=3)
        Button(window, text="Guest Profiles", command=self.button_click5).grid(row=currRows+1, column=4)
        Button(window, text="Current Stay", command=self.button_click6).grid(row=currRows+1, column=5)
        Button(window, text="Guest Search", command=self.button_click7).grid(row=currRows+1, column=6)
        Button(window, text="Daily Report", command=self.button_click8).grid(row=currRows+1, column=7)
        window.pack()
        # Create labels, entries,buttons
        window.pack()

    def button_click1(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window1(new_master)

    def button_click2(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window2(new_master)

    def button_click3(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window3(new_master)

    def button_click4(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window4(new_master)

    def button_click5(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window5(new_master)

    def button_click6(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window6(new_master)

    def button_click7(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window7(new_master)

    def button_click8(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window8(new_master)
        # Create labels, entries,buttons


class Window5:  # This window is for GUEST PROFILE!
    def __init__(self, master):
        window = Frame(master)
        self.master = master
        master.title("GUEST PROFILE")
        label = Label(window, text="Guest", background="pink",anchor='w').grid(row=0, column=0)
        lst = [('First Name', 'Last Name', 'Phone', 'Address', 'E-mail',  'ID Info (State, ID#)', 'Vehicle License Plate'),
            ('', '', '', '', '', '', '')]
        currRows = 0
        # find total number of rows and
        # columns in list
        rows = len(lst)
        cols = len(lst[0])
        gridLabels = []
        for r in range(rows):
            for c in range(cols):
                gridLabels.append(Label(window, text=lst[r][c], borderwidth=1).grid(row=r+2, column=c))
                currRows = r+2
        window.pack()
        # Create labels, entries,buttons
        Button(window, text="Room List", command=self.button_click1).grid(row=currRows+1, column=0)
        Button(window, text="Weekly List", command=self.button_click2).grid(row=currRows+1, column=1)
        Button(window, text="Reservation", command=self.button_click3).grid(row=currRows+1, column=2)
        Button(window, text="Housekeeping", command=self.button_click4).grid(row=currRows+1, column=3)
        Button(window, text="Guest Profiles", command=self.button_click5).grid(row=currRows+1, column=4)
        Button(window, text="Current Stay", command=self.button_click6).grid(row=currRows+1, column=5)
        Button(window, text="Guest Search", command=self.button_click7).grid(row=currRows+1, column=6)
        Button(window, text="Daily Report", command=self.button_click8).grid(row=currRows+1, column=7)
        window.pack()

    def button_click1(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window1(new_master)

    def button_click2(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window2(new_master)

    def button_click3(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window3(new_master)

    def button_click4(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window4(new_master)

    def button_click5(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window5(new_master)

    def button_click6(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window6(new_master)

    def button_click7(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window7(new_master)

    def button_click8(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window8(new_master)


class Window6:  # This window is for GUEST'S CURRENT STAY INFO!
    def __init__(self, master):
        window = Frame(master)
        self.master = master
        master.title("GUEST'S CURRENT STAY INFO")
        label = Label(window, text="Guests", background="pink",anchor='w').grid(row=0, column=0)
        # take the data
        lst = [('Guest Name', 'Check In Date and Time', 'Expected Check Out Date and Time',  'Room Type', 'Room Number',
                'Room Rate ($/Day)', 'Total Charge', 'Payments Made', 'Balance'),
            ('', '', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', '', '')]
        currRows = 0
        # find total number of rows and
        # columns in list
        rows = len(lst)
        cols = len(lst[0])
        gridLabels = []
        for r in range(rows):
            for c in range(cols):
                gridLabels.append(Label(window, text=lst[r][c], borderwidth=1).grid(row=r+1, column=c))
                currRows = r+1
        window.pack()
        Button(window, text="Room List", command=self.button_click1).grid(row=currRows+1, column=0)
        Button(window, text="Weekly List", command=self.button_click2).grid(row=currRows+1, column=1)
        Button(window, text="Reservation", command=self.button_click3).grid(row=currRows+1, column=2)
        Button(window, text="Housekeeping", command=self.button_click4).grid(row=currRows+1, column=3)
        Button(window, text="Guest Profiles", command=self.button_click5).grid(row=currRows+1, column=4)
        Button(window, text="Current Stay", command=self.button_click6).grid(row=currRows+1, column=5)
        Button(window, text="Guest Search", command=self.button_click7).grid(row=currRows+1, column=6)
        Button(window, text="Daily Report", command=self.button_click8).grid(row=currRows+1, column=7)
        # Create labels, entries,buttons

    def button_click1(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window1(new_master)

    def button_click2(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window2(new_master)

    def button_click3(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window3(new_master)

    def button_click4(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window4(new_master)

    def button_click5(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window5(new_master)

    def button_click6(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window6(new_master)

    def button_click7(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window7(new_master)

    def button_click8(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window8(new_master)


class Window7:  # This window is for GUEST SEARCH!
    def __init__(self, master):
        window = Frame(master)
        self.master = master
        master.title("GUEST SEARCH")
        currRows = 0 
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
                currRows = r+1
        Button(window, text="Room List", command=self.button_click1).grid(row=currRows+1, column=0)
        Button(window, text="Weekly List", command=self.button_click2).grid(row=currRows+1, column=1)
        Button(window, text="Reservation", command=self.button_click3).grid(row=currRows+1, column=2)
        Button(window, text="Housekeeping", command=self.button_click4).grid(row=currRows+1, column=3)
        Button(window, text="Guest Profiles", command=self.button_click5).grid(row=currRows+1, column=4)
        Button(window, text="Current Stay", command=self.button_click6).grid(row=currRows+1, column=5)
        Button(window, text="Guest Search", command=self.button_click7).grid(row=currRows+1, column=6)
        Button(window, text="Daily Report", command=self.button_click8).grid(row=currRows+1, column=7)
        window.pack()
        # Create labels, entries,buttons

    def button_click1(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window1(new_master)

    def button_click2(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window2(new_master)

    def button_click3(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window3(new_master)

    def button_click4(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window4(new_master)

    def button_click5(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window5(new_master)

    def button_click6(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window6(new_master)

    def button_click7(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window7(new_master)

    def button_click8(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window8(new_master)


class Window8:  # This window is for DAILY REPORT!
    def __init__(self, master):
        window = Frame(master)
        self.master = master
        master.title("DAILY REPORT")
        currRows = 0
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
                currRows = r+1
        Button(window, text="Room List", command=self.button_click1).grid(row=currRows+1, column=0)
        Button(window, text="Weekly List", command=self.button_click2).grid(row=currRows+1, column=1)
        Button(window, text="Reservation", command=self.button_click3).grid(row=currRows+1, column=2)
        Button(window, text="Housekeeping", command=self.button_click4).grid(row=currRows+1, column=3)
        Button(window, text="Guest Profiles", command=self.button_click5).grid(row=currRows+1, column=4)
        Button(window, text="Current Stay", command=self.button_click6).grid(row=currRows+1, column=5)
        Button(window, text="Guest Search", command=self.button_click7).grid(row=currRows+1, column=6)
        Button(window, text="Daily Report", command=self.button_click8).grid(row=currRows+1, column=7)
        window.pack()
        # Create labels, entries,buttons
        # NEED TO GET A SUM OF THE CASH!

    def button_click1(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window1(new_master)

    def button_click2(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window2(new_master)

    def button_click3(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window3(new_master)

    def button_click4(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window4(new_master)

    def button_click5(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window5(new_master)

    def button_click6(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window6(new_master)

    def button_click7(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window7(new_master)

    def button_click8(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window8(new_master)
    


def main():  # run mainloop
    root = tk.Tk()
    app = Window1(root)
    root.mainloop()


if __name__ == '__main__':
    main()
