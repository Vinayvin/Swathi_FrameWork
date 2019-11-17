class Vehicle:
    def __init__(self,vehicle_type,mileage):
        self.vehicle_type=vehicle_type
        self.mileage=mileage

class Car(Vehicle):
    def __call__(self,vehicle_type,mileage):
        super().__init__(vehicle_type,mileage)
        print("Car")
class Bike(Vehicle):
    def __init__(self,vehicle_type,mileage):
        super().__init__(vehicle_type,mileage)
        print("Bike")

bike=Bike("2 wheeler",25)
car=Car("4 wheeler",18)
print(bike.vehicle_type)
print(car.vehicle_type)