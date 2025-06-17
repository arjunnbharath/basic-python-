class Dog:
    def __init__(self, name):
        self.name = name  # instance variable

    def speak(self):
        return f"{self.name} says Woof!"
        
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy says Woof!
