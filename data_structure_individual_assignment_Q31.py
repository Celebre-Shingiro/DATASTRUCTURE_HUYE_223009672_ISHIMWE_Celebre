from collections import deque

# Flight Booking System
flight_schedules = []
issued_tickets = deque()
cancelled_tickets = []
def addFlightSchedule(flight):
    flight_schedules.append(flight)
    print(f"Flight {flight} added to the schedule.")
def removeFlightSchedule(flight):
    if flight in flight_schedules:
        flight_schedules.remove(flight)
        print(f"Flight {flight} removed from the schedule.")
    else:
        print("Flight not found!")
def issueTicket(flight):
    if flight in flight_schedules:
        issued_tickets.append(flight)
        print(f"Ticket for flight {flight} booked!")
        return "Y"
    else:
        print(f"Flight {flight} not available in the schedule. Here is the flight schedule we have: {flight_schedules}")
        return "N"

def processTicket():
    if issued_tickets:
        flight = issued_tickets.popleft()
        print(f"Ticket for flight {flight} processed.")
    else:
        print("Empty tickets to process!")

def undoTicket():
    if issued_tickets:
        flight = issued_tickets.pop()
        cancelled_tickets.append(flight)
        print(f"Ticket for flight {flight} cancelled.")
    else:
        print("No tickets to undo!")

numberOfFlights = int(input("Enter the number of flights to add to the schedule: "))
for i in range(numberOfFlights):
    flight = input(f"Enter Flight {i+1}: ")
    addFlightSchedule(flight)
    if i == numberOfFlights - 1:
        print("Flights added successfully! \n ----------------------")

removalNumber = int(input("Enter number of flights to remove from the schedule, if you want to: "))
for i in range(removalNumber):
    flight = input(f"Enter Flight {i+1} to remove from schedule: ")
    removeFlightSchedule(flight)
    if i == removalNumber - 1:
        print("Flights removed successfully! \n ----------------------")

ticketNumber = int(input("Enter number of flight tickets to book: "))
i = 1
while i <= ticketNumber:
    flight = input(f"Enter flight ticket to book {i}: ")
    if flight == "S" or flight == "s":
        i += 1
    else:
        ticket_status = issueTicket(flight)
        if ticket_status == "N":
            i = i
        else:
            i += 1
    if i == ticketNumber + 1:
        print("Your tickets are booked. You are getting closer to the end! \n ----------------------")

undoNumber = int(input("Enter number of tickets to undo, if any: "))
for i in range(undoNumber):
    undoTicket()
    if i == undoNumber - 1:
        print("Tickets undone. you are near to the end of process! \n ----------------------")

processingNumber = int(input("Enter number of tickets to process: "))
for i in range(processingNumber):
    processTicket()
    if i == processingNumber - 1:
        print("Tickets processed. You are at the end! \n ----------------------")

print(f"Here is the flight schedule: {flight_schedules}")
print(f"Here are the booked tickets: {list(issued_tickets)}")
print(f"Here are the cancelled tickets: {cancelled_tickets}")
