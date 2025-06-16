class lab :
    print("welcome to the lab")
    print("we need your dertails")
    name =input("Enter your name: ")
    age = int(input("Enter your age: "))
    roll_no = int(input("Enter your roll number: "))

class Student:
    def __init__(self,ddd):
        self.name = ddd
        print("name is",ddd)