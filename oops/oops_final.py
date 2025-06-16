#delete function in python
# The `del` statement in Python is used to delete objects, variables, or attributes.

# class student :
#     def __init__(self,name):
#         self.name= name

# s1= student("sahil")
# s2= student("sahil")

# print(s1.name)
# print(s2.name)

# del s1
# print(s1)  # This will raise an error because s1 has been deleted


#private like functions in python
# In Python, you can create private methods by prefixing the method name with a double underscore (`__`).

class Student:
    def __init__(self, name):
        self.name = name

    def __private_method(self):
        print(f"This is a private method for {self.name}")

    def public_method(self):
        print(f"This is a public method for {self.name}")
        self.__private_method()  # Calling the private method within the class  

# Example usage
s1 = Student("Sahil")           
s1.public_method()  # This will work and call the private method
# s1.__private_method()  # This will raise an AttributeError because __private_method is private
# s1.public_method()  # This will work and call the private method
# s1.__private_method()  # This will raise an AttributeError because __private_method is private