#Create student class that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print the average.
class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average(self):
        avg = (self.marks1 + self.marks2 + self.marks3) / 3
        print(f"Average marks of {self.name} is {avg}")
        return avg
class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average(self):
        avg = (self.marks1 + self.marks2 + self.marks3) / 3
        print(f"Average marks of {self.name} is {avg}")
        return avg

    # Static method to greet the user
    @staticmethod
    def hello():
        print("Hello, welcome to the Student Average Calculator!")

# Taking input from user
name = input("Enter student's name: ")
marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))

S1 =Student(name, marks1, marks2, marks3)
S1.average()
S1.hello()  # Call the hello method to greet the user














8