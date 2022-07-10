class ParkingGarage():
    def __init__(self):
        self.parkingSpaces = [1, 2, 3, 4, 5]
        self.tickets = [1, 2, 3, 4, 5]
        self.currentTicket = {}
    def takeTicket(self):
        if self.parkingSpaces==[]:
            print("There are no spaces available in the garage.")
        else:
            ticket = self.tickets.pop(0)
            self.parkingSpaces.pop(0)
            self.currentTicket[ticket]="unpaid"
            print(f"Your ticket number is {self.currentTicket}")
            print(f"Spaces left: {self.parkingSpaces}.")
    def payForParking(self):
        ticket = int(input("Enter your ticket number: "))
        if self.currentTicket[ticket] == 'paid':
            print("Thank you for your payment. You have 15 minutes to leave the garage.")
        else:
            print("Please pay the amount due.")
            pay = input("Please pay for parking!(Enter a number greater than 0)")
            if pay >= '0':
                print("Thank you for your payment! You have 15 minutes to leave the garage.")
                self.currentTicket[ticket]="paid"
                self.parkingSpaces.append(ticket)
    def leaveGarage(self):
        ticket = int(input("Enter your ticket number: "))
        if self.currentTicket[ticket] == 'paid':
            print("Thank you for parking with us! Have a great day!")
        else:
            print("Please pay the amount due before leaving the garage.")
            self.payForParking()
class UI():
    def __init__(self, ParkingGarage):
        self.ParkingGarage = ParkingGarage
    def runGarage(self):
        while True:
            print("----- Welcome to the Parking Garage! -----")
            response = input("What would you like to do? Park, pay, leave, or quit? ").lower()
            if response.lower() == 'park':
                self.ParkingGarage.takeTicket()
            elif response.lower() == 'pay':
                self.ParkingGarage.payForParking()
            elif response.lower() == 'leave':
                self.ParkingGarage.leaveGarage()
            elif response.lower() == 'quit':
                break
            else:
                print("Please select an option: pay, park, or leave.")
ui = UI(ParkingGarage())
ui.runGarage()

