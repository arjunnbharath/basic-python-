d ={}
x=input("Enter a mark for physics: ")
d.update({"Physics": x})
y=input("Enter a mark for chemistry: ")
d.update({"Chemistry": y})
z=input("Enter a mark for maths: ")
d.update({"maths":z})
print("The dictionary is:", d)
print("The marks in physics is:", d.get("Physics"))
print("The marks in chemistry is:", d.get("Chemistry"))
print("The marks in maths is:", d.get("maths"))
