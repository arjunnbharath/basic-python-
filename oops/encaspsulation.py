#what is encapsulation in python
## Encapsulation is a fundamental concept in object-oriented programming (OOP) 
# that restricts direct access to an object's attributes and methods. It helps to 
# protect the internal state of an object and prevents unintended interference and misuse of its data.

class Car:
    def __init__(self):
        self.__acc = False  # Private attribute
        self.__brake = False  # Private attribute
        self.__clutch = False  # Private attribute

    def start(self):
        self.__acc = True
        self.__clutch = True
        print("Car started")

    def stop(self):
        self.__acc = False
        self.__clutch = False
        print("Car stopped")

    def get_acc_status(self):
        return self.__acc

    def get_brake_status(self):
        return self.__brake 
    def get_clutch_status(self):
        return self.__clutch
    def set_acc_status(self, status):
        if isinstance(status, bool):
            self.__acc = status
        else:
            print("Invalid value for acc status. It must be a boolean.")
    def set_brake_status(self, status):

        if isinstance(status, bool):
            self.__brake = status
        else:
            print("Invalid value for brake status. It must be a boolean.")

    def set_clutch_status(self, status):
        if isinstance(status, bool):
            self.__clutch = status
        else:
            print("Invalid value for clutch status. It must be a boolean.")
# Example usage
car1 = Car()
car1.start()        
car1.set_acc_status(True)
car1.set_brake_status(False)
car1.set_clutch_status(True)
print(f"Accelerator status: {car1.get_acc_status()}")
print(f"Brake status: {car1.get_brake_status()}")
print(f"Clutch status: {car1.get_clutch_status()}")
car1.stop()
# car1.__acc = True  # This will raise an AttributeError because __acc is private