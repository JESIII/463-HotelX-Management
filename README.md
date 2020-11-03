# 463 HotelX Management

Case1:
Preconditions: User is on window1, which is default upon startup
Success Guarantee: Show all rooms and their status:
	Available, Unavailable/Occupied, Unavailable/Dirty, Unavailable/Maintenance
	and also:
	King (K), Double Queen (DQ), Double Queen with Kitchen (DQK), Suite (S)
Main Success Scenario: 1. The user starts the program and sees this screen
			2. The user may hit the next page to get to window2
Extensions: 2. User may close the program instead

Case2:
Preconditions:User is on window2
Success Guarantee: Show all rooms and who is staying in each one
	over the course of the next 7 days
Main Success Scenario: 1. The user may hit the next page to get to the next window
Extensions: 1a. User may close the program instead
	    1b. User may hit PREV to go to the previous page instead

Case3:
Preconditions:User is on window3
Success Guarantee: shows a list of all reservations currently in the system:
	Guest First Name, Guest Last Name, Date Made,  Date Checkin,  Date Checkout,  
	Room Type, Website Reservation Made, Rate ($/Day), Total Charge
Main Success Scenario: 1. The user may hit the next page to get to the next window
Extensions: 1a. User may close the program instead
	    1b. User may hit PREV to go to the previous page instead

Case4:
Preconditions:User is on window4
Success Guarantee: shows a list of all the dirty rooms, with their cleaning stats:
	Housekeep Name, Room number, Type, Status, Bathroom,  Towels, Bed Sheets, 
	Vacuum, Dusting, Electronics
Main Success Scenario: 1. The user may hit the next page to get to the next window
Extensions: 1a. User may close the program instead
	    1b. User may hit PREV to go to the previous page instead

Case5:
Preconditions:User is on window5
Success Guarantee: shows the guest profile information:
	First Name, Last Name, Phone, Address, E-mail,  ID Info (State, ID#), Vehicle License Plate
Main Success Scenario: 1. The user may hit the next page to get to the next window
Extensions: 1a. User may close the program instead
	    1b. User may hit PREV to go to the previous page instead

Case6:
Preconditions:User is on window6
Success Guarantee: shows the room/guest current stay information:
	Guest Name, Check In Date and Time, Expected Check Out Date and Time,  Room Type, 
	Room Number, Room Rate ($/Day), Total Charge, Payments Made, Balance
Main Success Scenario: 1. The user may hit the next page to get to the next window
Extensions: 1a. User may close the program instead
	    1b. User may hit PREV to go to the previous page instead

Case7:
Preconditions:User is on window7
Success Guarantee: the user can search for a guest using: 
	Guest First Name, Guest Last Name, Room Number, Phone Number, Street Address, 
	Check In Date, Checkout Date
Main Success Scenario:  1. The user enters a data appropriate to the fields and hits "search."
			3. The proper customer profile is fetched 
			4. The user may hit the next page to get to the next window
Extensions: 3a. If no customer matches parameters, return "N/A".
	    4a. User may close the program instead
	    4b. User may hit PREV to go to the previous page instead

Case8:
Preconditions:User is on window8
Success Guarantee: show a report of the day’s activity. 
	It will show a list of rooms that were rented that day and their stats.
	Room Number, Guest Name, Date In, Date Out (If Checked Out), Amount Paid for the room. 
	Below will be a total of dollars paid
Main Success Scenario: 1. The user may hit the next page to get to the next window
Extensions: 1a. User may close the program instead
	    1b. User may hit PREV to go to the previous page instead