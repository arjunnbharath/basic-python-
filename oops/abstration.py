#what is abstration?
# Abstraction is a fundamental concept in object-oriented programming (OOP) that allows you to hide the complex 
# implementation details of a system and expose only the necessary parts to the user. It helps in reducing complexity and 
# increasing efficiency by allowing the user to interact with an object without needing to understand its internal workings.

# In Python, abstraction can be achieved using abstract classes and interfaces. An abstract class is a class that cannot be
# instantiated and may contain abstract methods that must be implemented by any subclass. This allows you to define a common
# interface for a group of related classes while hiding the implementation details.

class car():
    def __init__(self):
        self.acc = False
        self.brake = False
        self.clutch = False

    def Start(self):
        self.acc = True
        self.clutch = True
        print("Car started")

car1 = car()
car1.Start()