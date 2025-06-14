a= input("enter your age: ")
if int(a) > 18:
    print("Eligible for voting")
elif int(a) == 18:
    print("Eligible for voting, but need to register first")
else:
    print("Not eligible for voting")