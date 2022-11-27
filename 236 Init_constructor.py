class Vehicles():
    def __init__(self):
        print("Calling init")
        self.val=0
        self.cost=10000
        
    def incrementVehicle(self):
        self.val+=1
        
car=Vehicles()
print("First obj value:",car.val)

car.incrementVehicle()
car.incrementVehicle()

print("First obj value after incrementing",car.val)

bike=Vehicles()
print("Second obj value:",bike.val)