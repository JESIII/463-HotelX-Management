import tkinter as tk
from tkinter.ttk import *
import datetime as dt
from datetime import timedelta
from datetime import date
from functools import partial
import time
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


class Room: # Please update this class with the info it needs
    def __init__(self, num, _type, status):
        self.num = num
        self.status = status
        self.type = _type


guests = [Guest("Johnny", "Johnson", "555-5555", "0000", "John@email.com", "CA, 1234", "YOOOOOO")]
rooms = [Room(101, 'K', 'Available'), Room(103, 'DQ', 'Unavailable/Occupied'), Room(104, 'DQK', 'Unavailable/Dirty'), Room(105, 'S', 'Unavailable/Maintenance'),Room(106, 'S', 'Unavailable/Occupied')]
roomRates = {'S':10, 'K':20, 'DQK':30, 'DQ':25}

class Window1:  # This window is for all the HOTEL ROOMS
    def __init__(self, master):
        self.master = master
        ListFrame = Frame(master)
        master.title("HOTEL ROOMS")
        label = Label(ListFrame, text="Room List").grid(row=0, column=0, sticky = 'W', pady = 2)
        Label(ListFrame, text="Room #").grid(row=1, column=0, sticky = 'W', pady = 2)
        Label(ListFrame, text="Type   ").grid(row=1, column=1, sticky = 'W', pady = 2)
        Label(ListFrame, text="Status").grid(row=1, column=2, sticky = 'W', pady = 2)
        Label(ListFrame, text="Edit").grid(row=1, column=3, sticky = 'W', pady = 2)
        currRow = 2
        for r in range(len(rooms)):
            if rooms[r].status != 'Available':
                self.clickRoomBtn = partial(self.clickRoom, rooms[r])
                Button(ListFrame, text=rooms[r].num, command=self.clickRoomBtn).grid(row=currRow, column=0, sticky = 'W', pady = 2)
                #Label(ListFrame, text=rooms[r].num, borderwidth=1).grid(row=currRow, column=0, sticky = 'W', pady = 2)
                Label(ListFrame, text=rooms[r].type, borderwidth=1).grid(row=currRow, column=1, sticky = 'W', pady = 2)
                Label(ListFrame, text=rooms[r].status, borderwidth=1).grid(row=currRow, column=2, sticky = 'W', pady = 2)
                if(rooms[r].status != 'Unavailable/Occupied'):
                    self.makeAvailableBtn = partial(self.makeAvailable, rooms[r])  # pairs the action with an argument for below
                    Button(ListFrame, text="Make Available", command=self.makeAvailableBtn).grid(row=currRow, column=3, sticky = 'W', pady = 2)
            else:
                self.clickRoomBtn = partial(self.clickRoom, rooms[r])
                Button(ListFrame, text=rooms[r].num, command=self.clickRoomBtn).grid(row=currRow, column=0, sticky = 'W', pady = 2)
                #Label(ListFrame, text=rooms[r].num, borderwidth=1).grid(row=currRow, column=0, sticky = 'W', pady = 2)
                Label(ListFrame, text=rooms[r].type, borderwidth=1).grid(row=currRow, column=1, sticky = 'W', pady = 2)
                self.makeRes = partial(self.availableButton, rooms[r])  # pairs the action with an argument for below
                Button(ListFrame, text="Available", command=self.makeRes).grid(row=currRow, column=2, sticky = 'W', pady = 2)
            currRow = currRow + 1
        # Create labels, entries,buttons
        ListFrame.pack()
        NavFrame = Frame(master)
        Button(NavFrame, text="Room List", command=self.button_click1).grid(row=currRow, column=0, sticky = 'W', pady = 2)
        Button(NavFrame, text="Weekly List", command=self.button_click2).grid(row=currRow, column=1, sticky = 'W', pady = 2)
        Button(NavFrame, text="Reservation", command=self.button_click3).grid(row=currRow, column=2, sticky = 'W', pady = 2)
        Button(NavFrame, text="Housekeeping", command=self.button_click4).grid(row=currRow, column=3, sticky = 'W', pady = 2)
        Button(NavFrame, text="Guest Search", command=self.button_click7).grid(row=currRow, column=6, sticky = 'W', pady = 2)
        Button(NavFrame, text="Daily Report", command=self.button_click8).grid(row=currRow, column=7, sticky = 'W', pady = 2)
        NavFrame.pack()

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
        Window3(new_master, reservations)

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

    def clickRoom(self, room):
        for index, r in enumerate(reservations):
            #if str(r.room_num) == str(room.num): #not needed
            if dt.date.today() < dt.datetime.strptime(r.CheckOut, '%Y-%m-%d').date() and dt.date.today() > dt.datetime.strptime(r.CheckIn, '%Y-%m-%d').date():
                new_master = tk.Tk()
                self.master.destroy()
                Window6(new_master, index) #passes reservation to window 6 for the current occupant
                print('here1')
            elif dt.date.today() < dt.datetime.strptime(r.CheckIn, '%Y-%m-%d'):
                new_master = tk.Tk()
                self.master.destroy()
                Window6(new_master, index) #passes reservation to window 6 for the reservation
                print('here2')
            else:
                new_master = tk.Tk()
                self.master.destroy()
                reservations.append(Reservation())
                Window6(new_master, index+1) #passes empty reservation to window 6
                print('here3')

    def button_click7(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window7(new_master)

    def button_click8(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window8(new_master)
    def confirmAvailability(self, room):
        for r in rooms:
            if room.num == r.num:
                r.status = 'Available'
        new_master = tk.Tk()
        self.master.destroy()
        self.sub_window.destroy()
        Window1(new_master)
    def declineAvailability(self):
        new_master = tk.Tk()
        self.master.destroy()
        self.sub_window.destroy()
        Window1(new_master)
    def makeAvailable(self, room):
        self.sub_window = tk.Tk()
        self.sub_window.title('Are you sure?')
        Label(self.sub_window, text="This room is " + room.status.split('/')[1]).grid(row=0, column=0, sticky = 'W', pady = 2)
        Label(self.sub_window, text='Are you sure you want to make it available?').grid(row=1, column=0, sticky = 'W', pady = 2)
        self.confirmAvailabilityBtn = partial(self.confirmAvailability, room)  # pairs the action with an argument for below
        Button(self.sub_window, text="Yes", command=self.confirmAvailabilityBtn).grid(row=2, column=0, sticky = 'W', pady = 2)
        self.declineAvailabilityBtn = partial(self.declineAvailability)  # pairs the action with an argument for below
        Button(self.sub_window, text="No", command=self.declineAvailabilityBtn).grid(row=2, column=1, sticky = 'W', pady = 2)
    def confirmEntry(self):
        total = (dt.datetime.strptime(self.checkout.get(), '%Y-%m-%d') - dt.datetime.strptime(self.checkin.get(), '%Y-%m-%d')).days * self.roomRate['text']
        reservation = Reservation(self.fname.get(), self.lname.get(), self.today['text'], self.checkin.get(), self.checkout.get(), self.roomType['text'], self.website.get(), self.roomRate['text'], total, self.roomNum['text'], self.payments.get(), self.balance.get(), self.numGuests.get())
        reservations.append(reservation)
        for x in range(len(rooms)):
            if str(rooms[x].num) == reservation.room_num:
                rooms[x].status = 'Unavailable/Occupied'
        new_master = tk.Tk()
        self.master.destroy()
        self.sub_window.destroy()
        Window1(new_master)

    def availableButton(self, room):
        self.sub_window = tk.Tk()
        self.sub_window.title('Make Reservation')
        Label(self.sub_window, text='First Name').grid(row=0, column=0)
        Label(self.sub_window, text='Last Name').grid(row=1, column=0)
        Label(self.sub_window, text='Date Made').grid(row=2, column=0)
        Label(self.sub_window, text='Checkin').grid(row=3, column=0)
        Label(self.sub_window, text='Checkout').grid(row=4, column=0)
        Label(self.sub_window, text='Room Type').grid(row=5, column=0)
        Label(self.sub_window, text='Website').grid(row=6, column=0)
        Label(self.sub_window, text='Rate').grid(row=7, column=0)
        Label(self.sub_window, text='Total Charge').grid(row=8, column=0)
        Label(self.sub_window, text='Room Num').grid(row=9, column=0)
        Label(self.sub_window, text='Payments').grid(row=10, column=0)
        Label(self.sub_window, text='Balance').grid(row=11, column=0)
        Label(self.sub_window, text='Number of Guests').grid(row=12, column=0)
        self.fname = Entry(self.sub_window)
        self.fname.grid(row=0, column=1)
        self.lname = Entry(self.sub_window)
        self.lname.grid(row=1, column=1)
        self.today = Label(self.sub_window, text=str(dt.date.today()))
        self.today.grid(row=2, column=1)
        self.checkin = Entry(self.sub_window)
        self.checkin.grid(row=3, column=1)
        self.checkout = Entry(self.sub_window)
        self.checkout.grid(row=4, column=1)
        self.roomType = Label(self.sub_window, text=str(room.type))
        self.roomType.grid(row=5, column=1)
        self.website = Entry(self.sub_window)
        self.website.grid(row=6, column=1)
        self.roomRate = Label(self.sub_window, text=roomRates.get(room.type))
        self.roomRate.grid(row=7, column=1)
        self.totalCharge = Label(self.sub_window, text=0)
        self.totalCharge.grid(row=8, column=1)
        self.roomNum = Label(self.sub_window, text=str(room.num))
        self.roomNum.grid(row=9, column=1)
        self.payments = Entry(self.sub_window)
        self.payments.grid(row=10, column=1)
        self.balance = Entry(self.sub_window)
        self.balance.grid(row=11, column=1)
        self.numGuests = Entry(self.sub_window)
        self.numGuests.grid(row=12, column=1)
        self.confirmRes = partial(self.confirmEntry)  # pairs the action with an argument for below
        Button(self.sub_window, text="Confirm", command=self.confirmRes).grid(row=13, column=1)
    
        # If button is clicked, run this method and open window 2


class Window2:  # This window is for the 7-DAY LIST!
    def __init__(self, master):
        window = Frame(master)
        self.master = master
        master.title("7-DAY LIST")
        label = Label(window, text="Rooms", background="pink", anchor='w').grid(row=0, column=0)
        Label(window, text="--Occupant--", background="pink").grid(row=0, column=4)
        Label(window, text="Room #", background="pink").grid(row=1, column=0)
        currRows = 2

        #Generate Title Names
        dayIndex = [] #so i can think less lol. to be reused in the name insertion.
        for x in range(7):
            #for the numbers 0-6, if today + the number is 0, 
            if (dt.date.today() + dt.timedelta(days=x)).weekday() == 0:
                Label(window, text="Monday", background="pink").grid(row=1, column=x+1)
            elif (dt.date.today() + dt.timedelta(days=x)).weekday() == 1:
                Label(window, text="Tuesday", background="pink").grid(row=1, column=x+1)
            elif (dt.date.today() + dt.timedelta(days=x)).weekday() == 2:
                Label(window, text="Wednesday", background="pink").grid(row=1, column=x+1)
            elif (dt.date.today() + dt.timedelta(days=x)).weekday() == 3:
                Label(window, text="Thursday", background="pink").grid(row=1, column=x+1)
            elif (dt.date.today() + dt.timedelta(days=x)).weekday() == 4:
                Label(window, text="Friday", background="pink").grid(row=1, column=x+1)
            elif (dt.date.today() + dt.timedelta(days=x)).weekday() == 5:
                Label(window, text="Saturday", background="pink").grid(row=1, column=x+1)
            elif (dt.date.today() + dt.timedelta(days=x)).weekday() == 6:
                Label(window, text="Sunday", background="pink").grid(row=1, column=x+1)
            dayIndex.append(x+1)
        #Insert Room List Vertically in Column 0
        for n in range(len(rooms)):
            self.clickRoom = partial(self.button_click6, rooms[n]) 
            Button(window, text=rooms[n].num, command=self.clickRoom).grid(row=currRows+n, column=0)
            for r in reservations:
                #Get # of days Between Checkin and Checkout
                sdate = dt.datetime.strptime(r.CheckIn, '%Y-%m-%d')
                edate = dt.datetime.strptime(r.CheckOut, '%Y-%m-%d')
                delta = edate - sdate
                #For each date between the check in and check out
                for j in range(delta.days + 1): #Remove +1 if we aren't including checkout day
                    day = sdate + timedelta(days=j)
                    #if the room for the current reservation is the room we are currently filling the row for
                    if(str(rooms[n].num) == r.room_num):
                        #then put the guest name that corresponds that room vertically and the weekday # horizontally
                        Label(window, text=(r.First + " " + r.Last)).grid(row=currRows+n, column=dayIndex[j])
                        #print(day.weekday()+1)
            #Label(window, text='test', borderwidth=1).grid(row=currRows, column=0)
            currRows = currRows+len(rooms)
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

    def button_click6(self, room):
        for index, r in enumerate(reservations):
            #if str(r.room_num) == str(room.num): #not needed
            if dt.date.today() < dt.datetime.strptime(r.CheckOut, '%Y-%m-%d').date() and dt.date.today() > dt.datetime.strptime(r.CheckIn, '%Y-%m-%d').date():
                new_master = tk.Tk()
                self.master.destroy()
                Window6(new_master, index) #passes reservation to window 6 for the current occupant
                print('here1')
            elif dt.date.today() < dt.datetime.strptime(r.CheckIn, '%Y-%m-%d'):
                new_master = tk.Tk()
                self.master.destroy()
                Window6(new_master, index) #passes reservation to window 6 for the reservation
                print('here2')
            else:
                new_master = tk.Tk()
                self.master.destroy()
                reservations.append(Reservation())
                Window6(new_master, index+1) #passes empty reservation to window 6
                print('here3')

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
    def __init__(self, First="", Last="", DateMade="", CheckIn="", CheckOut="", RoomType="", Website="",
                 Rate="", TotalCharge="", room_num="", payments="", balance="", guest_num=-1):
        self.First = First
        self.Last = Last
        self.DateMade = DateMade
        self.CheckIn = CheckIn
        self.CheckOut = CheckOut
        self.RoomType = RoomType
        self.room_num = room_num
        self.Website = Website
        self.Rate = Rate
        self.TotalCharge = TotalCharge
        self.payments = payments
        self.balance = balance
        self.guest_num = guest_num
        self.variableArray = [self.First, self.Last, self.DateMade, self.CheckIn, self.CheckOut, self.RoomType,
                              self.Website, self.Rate, self.TotalCharge]
        self.cur_stay = [self.First, self.Last, self.CheckIn, self.CheckOut, self.RoomType, self.room_num, self.Rate,
                         self.TotalCharge, self.payments, self.balance]

reservations = []
reservations.append(Reservation('John','Scales','2020-12-03','2020-12-03','2020-12-06', 'K', 'idk.com', '10', '400', '106', '0', '0', 1))
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
                    Label(window, text="Available", borderwidth=1).grid(row=r+2, column=13)
                else:
                    Label(window, text="Unavailable", borderwidth=1).grid(row=r + 2, column=13)
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
            if not j:
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

        self.check_box_unoccupied = tk.IntVar()
        Checkbutton(self.sub_window, text="Unoccupied", variable=self.check_box_unoccupied).grid(row=3, column=0, sticky='W')

        self.check_box_bathroom = tk.IntVar()
        Checkbutton(self.sub_window, text="Bathroom", variable=self.check_box_bathroom).grid(row=4, column=0, sticky='W')

        self.check_box_towels = tk.IntVar()
        Checkbutton(self.sub_window, text="Towels", variable=self.check_box_towels).grid(row=5, column=0, sticky='W')

        self.check_box_sheets = tk.IntVar()
        Checkbutton(self.sub_window, text="Sheets", variable=self.check_box_sheets).grid(row=6, column=0, sticky='W')

        self.check_box_vacuum = tk.IntVar()
        Checkbutton(self.sub_window, text="Vacuum", variable=self.check_box_vacuum).grid(row=7, column=0, sticky='W')

        self.check_box_dusting = tk.IntVar()
        Checkbutton(self.sub_window, text="Dusting", variable=self.check_box_dusting).grid(row=8, column=0, sticky='W')

        self.check_box_electronics = tk.IntVar()
        Checkbutton(self.sub_window, text="Electronics", variable=self.check_box_electronics).grid(row=9, column=0, sticky='W')

        self.temp_array = []

    def button_click_enter(self):
        self.temp_array.append(self.entry_1.get())
        self.temp_array.append(self.entry_2.get())
        self.temp_array.append(self.entry_3.get())
        self.temp_array.append(self.check_box_unoccupied.get())
        self.temp_array.append(self.check_box_bathroom.get())
        self.temp_array.append(self.check_box_towels.get())
        self.temp_array.append(self.check_box_sheets.get())
        self.temp_array.append(self.check_box_vacuum.get())
        self.temp_array.append(self.check_box_dusting.get())
        self.temp_array.append(self.check_box_electronics.get())

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
    def __init__(self, master, res_num=-1):
        window = Frame(master)
        self.master = master
        self.res_num = res_num

        master.title("GUEST'S CURRENT STAY INFO")

        currRows = 0
        if res_num >= 0 and res_num < len(reservations):
            Label(window, text="Guests", background="pink",anchor='w').grid(row=0, column=0)
            lst = [('Guest First Name', 'Guest Last Name', 'Check In Date and Time', 'Expected Check Out Date and Time',
                    'Room Type', 'Room Number', 'Room Rate ($/Day)', 'Total Charge', 'Payments Made', 'Balance')]
            # find total number of rows and
            # columns in list
            rows = len(lst)
            cols = len(lst[0])
            for r in range(rows):
                for c in range(cols):
                    Label(window, text=lst[r][c], borderwidth=1).grid(row=r+1, column=c)
                    currRows = r+1

            self.entries = []
            self.has_name = True
            # Button for guest name
            if reservations[res_num].guest_num == -1:
                self.has_name = False
                self.entries.append(Entry(window))
                self.entries.append(Entry(window))
                self.entries[0].grid(row=2, column=0)
                self.entries[0].grid(row=2, column=1)
            else:
                guest_full_name = guests[reservations[res_num].guest_num].f_name + " " + guests[reservations[res_num].guest_num].l_name
                Button(window, text=guest_full_name, command=self.button_guest_info).grid(row=2, column=0)

            # Create entries
            for i in range(8):
                self.entries.append(Entry(window))
                # Place entries
                if self.has_name:
                    self.entries[i].grid(row=2, column=i+2)
                    # Populate entries with all available reservation information
                    self.entries[i].insert(0, reservations[res_num].cur_stay[i])
                else:
                    self.entries[i+2].grid(row=2, column=i + 2)
                    # Populate entries with all available reservation information
                    self.entries[i+2].insert(0, reservations[res_num].cur_stay[i])
            # Button to update reservation information
            Button(window, text="Update Reservation info", command=self.button_update_reservation).grid(row=3, column=0)
            # Check-in and check-out buttons
            Button(window, text="Check-in", command=self.button_check_in).grid(row=3, column=1)
            Button(window, text="Check-out", command=self.button_check_out).grid(row=3, column=2)

        Button(window, text="Room List", command=self.button_click1).grid(row=4, column=0)
        Button(window, text="Weekly List", command=self.button_click2).grid(row=4, column=1)
        Button(window, text="Reservation", command=self.button_click3).grid(row=4, column=2)
        Button(window, text="Housekeeping", command=self.button_click4).grid(row=4, column=3)
        Button(window, text="Guest Profiles", command=self.button_click5).grid(row=4, column=4)
        Button(window, text="Current Stay", command=self.button_click6).grid(row=4, column=5)
        Button(window, text="Guest Search", command=self.button_click7).grid(row=4, column=6)
        Button(window, text="Daily Report", command=self.button_click8).grid(row=4, column=7)
        window.pack()

    def button_check_in(self):
        for r in rooms:
            if r.num is reservations[self.res_num].room_num:
                r.status = "Unavailable/Occupied"
        guests.append(Guest(self.entries[0].get(), self.entries[1].get(), "", "", "", "", ""))

    def button_check_out(self):
        for r in rooms:
            if r.num is reservations[self.res_num].room_num:
                r.status = "Unavailable/Dirty"

    def button_guest_info(self):
        new_master = tk.Tk()
        self.master.destroy()
        Window5(new_master, reservations[self.res_num].guest_num)

    def button_update_reservation(self):
        if self.has_name:
            reservations[self.res_num].First = self.entries[0].get()
            reservations[self.res_num].variableArray[0] = self.entries[0].get()
            reservations[self.res_num].Last = self.entries[1].get()
            reservations[self.res_num].variableArray[1] = self.entries[1].get()
            reservations[self.res_num].CheckIn = self.entries[2].get()
            reservations[self.res_num].variableArray[3] = self.entries[2].get()
            reservations[self.res_num].CheckOut = self.entries[3].get()
            reservations[self.res_num].variableArray[4] = self.entries[3].get()
            reservations[self.res_num].RoomType = self.entries[4].get()
            reservations[self.res_num].variableArray[5] = self.entries[4].get()
            reservations[self.res_num].room_num = self.entries[5].get()
            reservations[self.res_num].Rate = self.entries[6].get()
            reservations[self.res_num].variableArray[7] = self.entries[6].get()
            reservations[self.res_num].TotalCharge = self.entries[7].get()
            reservations[self.res_num].variableArray[8] = self.entries[7].get()
            reservations[self.res_num].payments = self.entries[8].get()
            reservations[self.res_num].balance = self.entries[9].get()
            for i in range(10):
                reservations[self.res_num].cur_stay[i] = self.entries[i].get()
        else:
            reservations[self.res_num].CheckIn = self.entries[0].get()
            reservations[self.res_num].variableArray[3] = self.entries[0].get()
            reservations[self.res_num].CheckOut = self.entries[1].get()
            reservations[self.res_num].variableArray[4] = self.entries[1].get()
            reservations[self.res_num].RoomType = self.entries[2].get()
            reservations[self.res_num].variableArray[5] = self.entries[2].get()
            reservations[self.res_num].room_num = self.entries[3].get()
            reservations[self.res_num].Rate = self.entries[4].get()
            reservations[self.res_num].variableArray[7] = self.entries[4].get()
            reservations[self.res_num].TotalCharge = self.entries[5].get()
            reservations[self.res_num].variableArray[8] = self.entries[5].get()
            reservations[self.res_num].payments = self.entries[6].get()
            reservations[self.res_num].balance = self.entries[7].get()
            for i in range(8):
                reservations[self.res_num].cur_stay[i + 2] = self.entries[i].get()

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


def main():  # run mainloop

    root = tk.Tk()
    app = Window1(root)
    root.mainloop()


if __name__ == '__main__':
    main()
