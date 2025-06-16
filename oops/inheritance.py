class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

class Car(Vehicle):
    def __init__(self, brand):
        Vehicle.__init__(self, brand, 4)  # Direct call to base class

    def honk(self):
        print(f"{self.brand} goes Beep Beep!")

car = Car("Honda")
print(car.brand)       # Output: Honda
print(car.wheels)      # Output: 4
car.honk()             # Output: Honda goes Beep Beep!
