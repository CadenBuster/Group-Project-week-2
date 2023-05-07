# Start Your Code here

class ParkingGarage(): 
   
    def __init__(self):
        self.tickets = [100]
        self.parkingspaces = [100]
        self.currentticket= {'paid':False}

    def take_ticket(self):
        for x in range(len(self.tickets)):
            self.tickets[x] -= 1
            for x in self.tickets:
                print(f'There are {x} tickets available')
        for s in range(len(self.parkingspaces)):
            self.parkingspaces[s] -= 1
            for s in self.parkingspaces:
                print(f'There are {s} parking spots available')
        
    
    def pay_parking(self):
        while True:
            fare =  int(input('Please Enter Amount   '))
            if fare > 0:
                self.currentticket['paid'] = True
                print('Paid, You have 15 minutes to leave')
                print('Thank you. Have a nice day')
                self.take_ticket()
                self.leave_gargage()
                break
            else:
                print('Invalid input')
                continue
            

    def leave_gargage(self):
        if self.currentticket['paid'] == True:
            print('Thank you have a nice day')
            for x in range(len(self.tickets)):
                self.tickets[x] += 1
                for x in self.tickets:
                    print(f'There are {x} tickets available')
            for s in range(len(self.parkingspaces)):
                self.parkingspaces[s] += 1
                for s in self.parkingspaces:
                    print(f'There are {s} parking spots available')

my_garage = ParkingGarage()
my_garage.pay_parking()

    
    
    # # def leave_garage():
    #      if paid 
    # #    if not paid fare = input('Please pay your fare')
    #     #parkingspaces += 1
    #   d  # ticket += 1 

