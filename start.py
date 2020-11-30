import tkinter as tk
from tkinter.ttk import *
import datetime as dt
from functools import partial
# from PIL import Image
import os


class Guest:
    def __init__(self, f_name, l_name, phone, address, email, _id, _license):
        self.f_name = f_name
        self.l_name = l_name
        self.phone = phone
        self.address = address
        self.email = email
        self.id = _id
        self.license = _license

        self.room_num = 0


guests = [Guest("Johnny", "Johnson", "555-5555", "0000", "John@email.com", "CA, 1234", "YOOOOOO")]
roomData = [{'room':101, 'type':'K', 'status':'Available'},{'room':102, 'type':'DQK', 'status':'Unavailable/Occupied'},{'room':103, 'type':'DQ', 'status':'Unavailable/Dirty'},{'room':104, 'type':'S', 'status':'Available'}]
roomRates = {'S':10, 'K':20, 'DQK':30, 'DQ':25}
lst = [(101, 'K', 'Available'),
            (102, 'K', 'Available'),
            (103, 'DQ', 'Unavailable/Occupied'),
            (104, 'DQK', 'Unavailable/Dirty'),
            (105, 'S', 'Unavailable/Maintenance')]


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
        # find total number of rows and
        # columns in list
        rows = len(lst)
        cols = len(lst[0])
        gridLabels = []
        for r in range(rows):
            for c in range(cols):
                if lst[r][2] != 'Available':
                    gridLabels.append(Label(window, text=lst[r][c], borderwidth=1).grid(row=r+2, column=c))
                else:
                    if c == 2:
                        Button(window, text="Available", command=self.button_click6).grid(row=r+2, column=c)
                    else:
                        gridLabels.append(Label(window, text=lst[r][c], borderwidth=1).grid(row=r+2, column=c))
                currRows = r+2
        # Create labels, entries,buttons
        Button(window, text="Room List", command=self.button_click1).grid(row=currRows+1, column=0)
        Button(window, text="Weekly List", command=self.button_click2).grid(row=currRows+1, column=1)
        Button(window, text="Reservation", command=self.button_click3).grid(row=currRows+1, column=2)
        Button(window, text="Housekeeping", command=self.button_click4).grid(row=currRows+1, column=3)
        Button(window, text="Guest Profiles", command=self.button_click5).grid(row=currRows+1, column=4)
        # Button(window, text="Current Stay", command=self.button_click6).grid(row=currRows+1, column=5)
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
        Window5(new_master, -1)

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
        Window5(new_master, -1)

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
    def __init__(self, First="", Last="", DateMade="", CheckIn="", CheckOut="", RoomType="", Website="", Rate="",
                 TotalCharge=""):
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
    def __init__(self, master, lst=[Reservation()]):  # mutable default arg is intentional. Ignore warning!
        window = Frame(master)
        self.master = master
        master.title("RESERVATIONS")
        self.numberOfVariables = 8
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
        # take the mutable data
        self.lst = lst
        # button for add. Cannot pass arguments. self.button_add(<<arguments>>) will automatically
        # trigger the function for some reason. So I had to make lst a self.lst so all defs will have access
        # without needing it passed. A similar implementation can be seen in button_add's call to button_add_enter
        Button(window, text="Add", command=self.button_click_add).grid(row=0, column=7)

        # find total number of rows and columns in list
        rows = len(self.lst)
        cols = self.numberOfVariables  # number of variables in a reservation object
        currRows = 0
        gridLabels = []
        for r in range(rows):
            for c in range(cols):
                gridLabels.append(Label(window, text=self.lst[r].variableArray[c], borderwidth=1).grid(row=r+2, column=c))
                # button for delete
                self.delete_with_r = partial(self.button_click_delete, r)  # pairs the action with an argument for below
                Button(window, text="Delete", command=self.delete_with_r).grid(row=r + 2, column=8)
                # Edit button
                self.edit_with_r = partial(self.button_click_edit, r)  # pairs the action with an argument for below
                Button(window, text="Edit", command=self.edit_with_r).grid(row=r + 2, column=9)
                currRows = r+2

        # main buttons
        Button(window, text="Room List", command=self.button_click1).grid(row=currRows + 1, column=0)
        Button(window, text="Weekly List", command=self.button_click2).grid(row=currRows + 1, column=1)
        Button(window, text="Reservation", command=self.button_click3).grid(row=currRows + 1, column=2)
        Button(window, text="Housekeeping", command=self.button_click4).grid(row=currRows + 1, column=3)
        Button(window, text="Guest Profiles", command=self.button_click5).grid(row=currRows + 1, column=4)
        Button(window, text="Current Stay", command=self.button_click6).grid(row=currRows + 1, column=5)
        Button(window, text="Guest Search", command=self.button_click7).grid(row=currRows + 1, column=6)
        Button(window, text="Daily Report", command=self.button_click8).grid(row=currRows + 1, column=7)

        window.pack()

    def refresh(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window3(new_master, self.lst)

    def entry(self):
        self.sub_window = tk.Tk()

        self.entry_1 = Entry()
        self.entry_1.grid(row=0, column=0)

        self.entry_2 = Entry()
        self.entry_2.grid(row=1, column=0)

        self.entry_3 = Entry()
        self.entry_3.grid(row=2, column=0)

        self.entry_4 = Entry()
        self.entry_4.grid(row=3, column=0)

        self.entry_5 = Entry()
        self.entry_5.grid(row=4, column=0)

        self.entry_6 = Entry()
        self.entry_6.grid(row=5, column=0)

        self.entry_7 = Entry()
        self.entry_7.grid(row=6, column=0)

        self.entry_8 = Entry()
        self.entry_8.grid(row=7, column=0)

        self.temp_array = []

    def button_click_enter(self):
        self.temp_array.append(self.entry_1.get())
        self.temp_array.append(self.entry_2.get())
        self.temp_array.append(self.entry_3.get())
        self.temp_array.append(self.entry_4.get())
        self.temp_array.append(self.entry_5.get())
        self.temp_array.append(self.entry_6.get())
        self.temp_array.append(self.entry_7.get())
        self.temp_array.append(self.entry_8.get())

    def button_click_add(self):
        self.entry()
        Button(self.sub_window, text="Enter", command=self.button_add_enter).grid(row=0, column=1)

    def button_click_edit(self, r):
        self.entry()

        convert_to_check_in = partial(self.button_click_convert_to_check_in, r) # pairs the action with an argument for below
        Button(self.sub_window, text="Convert to Check-In", command=convert_to_check_in).grid(row=0, column=2)

        edit_with_r_temp = partial(self.button_edit_enter, r)
        Button(self.sub_window, text="Change", command=edit_with_r_temp).grid(row=0, column=1)

    def button_click_convert_to_check_in(self, r):
        self.button_edit_convert(r)

        # TODO
        # Next, pass self.list[r] to button_click6 when feature is implemented.
        # Right now, the call has no parameter to accept this.
        self.button_click6()

    def button_edit_enter(self, r):
        self.button_click_enter()
        self.lst[r] = Reservation(self.temp_array[0], self.temp_array[1], self.temp_array[2], self.temp_array[3],
                                  self.temp_array[4], self.temp_array[5], self.temp_array[6], self.temp_array[7])

        new_master = tk.Tk()
        self.master.destroy()
        self.sub_window.destroy()
        Window3(new_master, self.lst)

    def button_edit_convert(self, r):
        self.button_click_enter()
        self.lst[r] = Reservation(self.temp_array[0], self.temp_array[1], self.temp_array[2], self.temp_array[3],
                                  self.temp_array[4], self.temp_array[5], self.temp_array[6], self.temp_array[7])

    def button_add_enter(self):
        self.button_click_enter()
        self.lst.append(Reservation(self.temp_array[0], self.temp_array[1], self.temp_array[2], self.temp_array[3],
                                    self.temp_array[4], self.temp_array[5], self.temp_array[6], self.temp_array[7]))

        new_master = tk.Tk()
        self.master.destroy()
        self.sub_window.destroy()
        Window3(new_master, self.lst)

    def button_click_delete(self, r):
        del self.lst[r]
        self.refresh()

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
        Window5(new_master, -1)

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


class Checklist:
    def __init__(self, server="", room_num=0, room_type="", status=False, bathroom=False, towels=False, sheets=False,
                 vacuum=False, dusting=False, electronics=False):
        self.server = server
        self.room_num = room_num
        self.room_type = room_type
        self.status = status
        self.bathroom = bathroom
        self.towels = towels
        self.sheets = sheets
        self.vacuum = vacuum
        self.dusting = dusting
        self.electronics = electronics
        self.variableArray = [self.server, self.room_num, self.room_type, self.status, self.bathroom, self.towels,
                              self.sheets, self.vacuum, self.dusting, self.electronics]


class Window4:  # This window is for HOUSEKEEPING!
    def __init__(self, master, lst=[Checklist()]):  # mutable default arg is intentional. Ignore warning!
        window = Frame(master)
        self.master = master
        master.title("HOUSEKEEPING")
        self.numberOfVariables = 10
        # Label(window, text="Rooms", background="pink", anchor='w').grid(row=0, column=0)
        Label(window, text="Server", background="pink").grid(row=0, column=0)
        Label(window, text="Room #", background="pink").grid(row=0, column=1)
        Label(window, text="Room Type", background="pink").grid(row=0, column=2)
        Label(window, text="Status", background="pink").grid(row=0, column=3)
        Label(window, text="Bathroom", background="pink").grid(row=0, column=4)
        Label(window, text="Towels", background="pink").grid(row=0, column=5)
        Label(window, text="Sheets", background="pink").grid(row=0, column=6)
        Label(window, text="Vacuum", background="pink").grid(row=0, column=7)
        Label(window, text="Dusting", background="pink").grid(row=0, column=8)
        Label(window, text="Electronics", background="pink").grid(row=0, column=9)
        # take the mutable data
        self.lst = lst
        # button for add. Cannot pass arguments. self.button_add(<<arguments>>) will automatically
        # trigger the function for some reason. So I had to make lst a self.lst so all defs will have access
        # without needing it passed. A similar implementation can be seen in button_add's call to button_add_enter
        Button(window, text="Add", command=self.button_click_add).grid(row=0, column=11)

        # find total number of rows and columns in list
        rows = len(self.lst)
        cols = self.numberOfVariables  # number of variables in a reservation object
        currRows = 0
        gridLabels = []
        for r in range(rows):
            for c in range(cols):
                gridLabels.append(Label(window, text=self.lst[r].variableArray[c], borderwidth=1).grid(row=r+2, column=c))
                if self.check_readiness(self.lst[r].variableArray):
                    Label(window, text="True", borderwidth=1).grid(row=r+2, column=13)
                else:
                    Label(window, text="False", borderwidth=1).grid(row=r + 2, column=13)
                # button for delete
                self.delete_with_r = partial(self.button_click_delete, r)  # pairs the action with an argument for below
                Button(window, text="Delete", command=self.delete_with_r).grid(row=r + 2, column=11)
                # Checklist button
                self.edit_with_r = partial(self.button_click_edit, r)  # pairs the action with an argument for below
                Button(window, text="Check", command=self.edit_with_r).grid(row=r + 2, column=12)
                currRows = r+2
        # main buttons
        Button(window, text="Room List", command=self.button_click1).grid(row=currRows + 1, column=0)
        Button(window, text="Weekly List", command=self.button_click2).grid(row=currRows + 1, column=1)
        Button(window, text="Reservation", command=self.button_click3).grid(row=currRows + 1, column=2)
        Button(window, text="Housekeeping", command=self.button_click4).grid(row=currRows + 1, column=3)
        Button(window, text="Guest Profiles", command=self.button_click5).grid(row=currRows + 1, column=4)
        Button(window, text="Current Stay", command=self.button_click6).grid(row=currRows + 1, column=5)
        Button(window, text="Guest Search", command=self.button_click7).grid(row=currRows + 1, column=6)
        Button(window, text="Daily Report", command=self.button_click8).grid(row=currRows + 1, column=7)

        window.pack()

    def check_readiness(self, reservation_array):
        for j in reservation_array:
            if not reservation_array[j]:
                return False
        return True

    def refresh(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window4(new_master, self.lst)

    def entry(self):
        self.sub_window = tk.Tk()

        self.entry_1 = Entry()
        self.entry_1.grid(row=0, column=0)

        self.entry_2 = Entry()
        self.entry_2.grid(row=1, column=0)

        self.entry_3 = Entry()
        self.entry_3.grid(row=2, column=0)

        self.entry_4 = Entry()
        self.entry_4.grid(row=3, column=0)

        self.entry_5 = Entry()
        self.entry_5.grid(row=4, column=0)

        self.entry_6 = Entry()
        self.entry_6.grid(row=5, column=0)

        self.entry_7 = Entry()
        self.entry_7.grid(row=6, column=0)

        self.entry_8 = Entry()
        self.entry_8.grid(row=7, column=0)

        self.entry_9 = Entry()
        self.entry_9.grid(row=8, column=0)

        self.entry_10 = Entry()
        self.entry_10.grid(row=9, column=0)

        self.temp_array = []

    def button_click_enter(self):
        self.temp_array.append(self.entry_1.get())
        self.temp_array.append(self.entry_2.get())
        self.temp_array.append(self.entry_3.get())
        self.temp_array.append(self.entry_4.get())
        self.temp_array.append(self.entry_5.get())
        self.temp_array.append(self.entry_6.get())
        self.temp_array.append(self.entry_7.get())
        self.temp_array.append(self.entry_8.get())
        self.temp_array.append(self.entry_9.get())
        self.temp_array.append(self.entry_10.get())

    def button_click_add(self):
        self.entry()
        Button(self.sub_window, text="Enter", command=self.button_add_enter).grid(row=0, column=1)

    def button_click_edit(self, r):
        self.entry()

        # convert_to_check_in = partial(self.button_click_convert_to_check_in, r) # pairs the action with an argument for below
        # Button(self.sub_window, text="Convert to Check-In", command=convert_to_check_in).grid(row=0, column=2)

        edit_with_r_temp = partial(self.button_edit_enter, r)
        Button(self.sub_window, text="Change", command=edit_with_r_temp).grid(row=0, column=1)
    '''
    def button_click_convert_to_check_in(self, r):
        self.button_edit_convert(r)

        # TODO
        # Next, pass self.list[r] to button_click6 when feature is implemented.
        # Right now, the call has no parameter to accept this.
        self.button_click6()'''

    def button_edit_enter(self, r):
        self.button_click_enter()
        self.lst[r] = Checklist(self.temp_array[0], self.temp_array[1], self.temp_array[2], self.temp_array[3],
                                self.temp_array[4], self.temp_array[5], self.temp_array[6], self.temp_array[7],
                                self.temp_array[8], self.temp_array[9])

        new_master = tk.Tk()
        self.master.destroy()
        self.sub_window.destroy()
        Window4(new_master, self.lst)

    def button_edit_convert(self, r):
        self.button_click_enter()
        self.lst[r] = Checklist(self.temp_array[0], self.temp_array[1], self.temp_array[2], self.temp_array[3],
                                self.temp_array[4], self.temp_array[5], self.temp_array[6], self.temp_array[7],
                                self.temp_array[8], self.temp_array[9])

    def button_add_enter(self):
        self.button_click_enter()
        self.lst.append(Checklist(self.temp_array[0], self.temp_array[1], self.temp_array[2], self.temp_array[3],
                                  self.temp_array[4], self.temp_array[5], self.temp_array[6], self.temp_array[7],
                                  self.temp_array[8], self.temp_array[9]))

        new_master = tk.Tk()
        self.master.destroy()
        self.sub_window.destroy()
        Window4(new_master, self.lst)

    def button_click_delete(self, r):
        del self.lst[r]
        self.refresh()

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
        Window5(new_master, -1)

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
    def __init__(self, master, guest_num):
        window = Frame(master)
        self.master = master
        self.guest_num = guest_num

        master.title("GUEST PROFILE")

        if guest_num >= 0:
            Label(window, text="Guest", background="pink",anchor='w').grid(row=0, column=0)
            lst = [('First Name', 'Last Name', 'Phone', 'Address', 'E-mail',  'ID Info (State, ID#)', 'Vehicle License Plate')]
            # find total number of rows and
            # columns in list
            rows = len(lst)
            cols = len(lst[0])
            for r in range(rows):
                for c in range(cols):
                    Label(window, text=lst[r][c], borderwidth=1).grid(row=r+2, column=c)

            # Create entries
            self.efname = Entry(window)
            self.elname = Entry(window)
            self.ephone = Entry(window)
            self.eaddress = Entry(window)
            self.eemail = Entry(window)
            self.eid = Entry(window)
            self.elicense = Entry(window)

            # Place entries
            self.efname.grid(row=1, column=0)
            self.elname.grid(row=1, column=1)
            self.ephone.grid(row=1, column=2)
            self.eaddress.grid(row=1, column=3)
            self.eemail.grid(row=1, column=4)
            self.eid.grid(row=1, column=5)
            self.elicense.grid(row=1, column=6)

            # Insert pre-existing guest info to the entries
            self.efname.insert(0, guests[guest_num].f_name)
            self.elname.insert(0, guests[guest_num].l_name)
            self.ephone.insert(0, guests[guest_num].phone)
            self.eaddress.insert(0, guests[guest_num].address)
            self.eemail.insert(0, guests[guest_num].email)
            self.eid.insert(0, guests[guest_num].id)
            self.elicense.insert(0, guests[guest_num].license)

            # Button for accepting any changes to the entries
            Button(window, text="Accept Changes", command=self.button_click_edit).grid(row=2, column=0)

        # Create labels, entries,buttons
        Button(window, text="Room List", command=self.button_click1).grid(row=3, column=0)
        Button(window, text="Weekly List", command=self.button_click2).grid(row=3, column=1)
        Button(window, text="Reservation", command=self.button_click3).grid(row=3, column=2)
        Button(window, text="Housekeeping", command=self.button_click4).grid(row=3, column=3)
        Button(window, text="Guest Profiles", command=self.button_click5).grid(row=3, column=4)
        Button(window, text="Current Stay", command=self.button_click6).grid(row=3, column=5)
        Button(window, text="Guest Search", command=self.button_click7).grid(row=3, column=6)
        Button(window, text="Daily Report", command=self.button_click8).grid(row=3, column=7)

        window.pack()

    def button_click_edit(self):
        guests[self.guest_num].f_name = self.efname.get()
        guests[self.guest_num].l_name = self.elname.get()
        guests[self.guest_num].phone = self.ephone.get()
        guests[self.guest_num].address = self.eaddress.get()
        guests[self.guest_num].email = self.eemail.get()
        guests[self.guest_num].id = self.eid.get()
        guests[self.guest_num].license = self.elicense.get()

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
        Window5(new_master, -1)

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
                'Room Rate ($/Day)', 'Total Charge', 'Payments Made', 'Balance')]
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
        name = Entry(window).grid(row=currRows+1, column=0)
        checkindt = Label(window, text=dt.datetime.today).grid(row=currRows+1, column=1)
        checkoutdt = Entry(window).grid(row=currRows+1, column=2)
        Label(window, text="RoomType Placeholder").grid(row=currRows+1, column=3)
        Label(window, text="Room# Placeholder").grid(row=currRows+1, column=4)
        Label(window, text="RoomRate Placeholder").grid(row=currRows+1, column=5)
        TotalCharge = Label(window, text=1337).grid(row=currRows+1, column=6)
        PaymentsMade = Entry(window, text=0).grid(row=currRows+1, column=7)
        Label(window, text='test').grid(row=currRows+1, column=8)
        currRows = currRows+1
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
        Window5(new_master, -1)

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
        Window5(new_master, -1)

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
        Window5(new_master, -1)

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


class CurrentStayWindow:
    def __init__(self, master, guests, guest, checked_in, has_reservation):
        self.master = master
        window = Frame(master)
        self.guest = guest
        self.has_reservation = has_reservation
        self.room_num = 0

        master.title("CURRENT STAY")

        if checked_in:
            '''
            print guest and room info
            '''
            Button(window, text="Check-out", command=self.button_check_out).grid(row=3, column=0)
        else:
            '''
            if has_reservation:
                display guest info
                display the reserved room
            else:
                display empty guest info entries
                display list of available rooms
                display entry for desired room number
            '''
            Button(window, text="Check-in", command=self.button_check_in).grid(row=3, column=0)
        Button(window, text="Return to Room List", command=self.button_room_list).grid(row=3, column=1)
        window.pack()

    def button_check_out(self):
        """
        check RoomData for corresponding room number
        change room status to Unavailable/Dirty
        """
        return

    def button_check_in(self):
        """
        if !has_reservation:
            set self.room_num
            add guest info to guests
            add room_num to that guest
        change room status to Unavailable/Occupied
        """
        return

    def button_room_list(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window1(new_master)


def main():  # run mainloop

    root = tk.Tk()
    app = Window1(root)
    root.mainloop()


if __name__ == '__main__':
    main()
