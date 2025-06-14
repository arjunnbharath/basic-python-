print("DRIVING TEST")
print("Enter the age of the person: ")
age=int(input())
if( age >= 18):
    while True:   
      print("do yo have a driving license? (Y/N)")
      license=input()
      if(license== "Y" or license == "y"):
        print("You are eligible for driving test")
        break
      elif(license == "N" or license == "n"):
        print("not eligible for driving test, please apply for a license first")
        break
      else:
        print("enter y or n only")
else:
    print("You are not eligible for driving test")
print("Thank you for using the driving test program")