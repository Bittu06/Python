"""Can you change the self-parameter inside a class to something else (say 
“harry”). Try changing self to “slf” or “harry” and see the effects"""




# Solution:
# Yes, we can change the self-parameter inside a class to something else.

class Train:
    def __init__(slf, name, fare, seats):
        slf.name = name
        slf.fare = fare
        slf.seats = seats

    def getStatus(bittu):
        print(f"The name of the train is {bittu.name}")
        print(f"The seats available in the train are {bittu.seats}")

    def fareInfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")

    def bookTicket(self):
        if self.seats > 0:
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full! Kindly try in tatkal")

intercity = Train("Intercity Express: 14015", 90, 10)
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()
intercity.bookTicket() 
intercity.getStatus()
intercity.fareInfo()