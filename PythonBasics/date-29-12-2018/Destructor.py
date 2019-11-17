class Vehicle:
    def __init__(self,vehicle_type):
        self.vehicle_type=vehicle_type

    def __del__(self):
        print("Object destroyed")


v = Vehicle("2 wheeler")
#manually deleting the object
del v
print(v)
