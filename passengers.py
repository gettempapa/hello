class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
        
    def addPassenger(self, name):
        if not self.checkCapacity():
            return False
        self.passengers.append(name)
        return True
    
    def checkCapacity(self):
        return self.capacity - len(self.passengers)

flight1 = Flight(5)

customers = ["Steve", "Bill", "Deb", "Jenny", "Sally", "Dave", "Grant", "Petunia"]

for cust in customers:
    if flight1.addPassenger(cust) == True:
        print(f"{cust} was added to the flight")
    else:
        print(f"{cust} could not be added to the flight")

print(flight1.checkCapacity())