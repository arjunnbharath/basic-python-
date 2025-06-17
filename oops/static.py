class Dog:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def bark_sound():
        return "Woof!"

print(Dog.bark_sound())  # Output: Woof!