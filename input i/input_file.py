#for this u need to first create a file named demo.txt with some content
# and then read it using the code below
# f=open("demo.txt","r")
# data=f.read()
# print(data)
# f.close()

# f=open("demo.txt","w")

# f.write("This is a new line added to the file.\n")
# f.write("This is another line.\n")  
# f.close()
# # Now reading the file again to see the changes     
# f=open("demo.txt","r")
# data=f.read()

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
# Now writing to the file
with open("demo.txt", "w") as f:
    f.write("This is a new line added to the file.\n")
    f.write("This is anotherhhhhhhhhhhhhh line.\n")                          
# Now reading the file again to see the changes
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
# Now appending to the file
with open("input i/demo.txt", "a") as f:
    f.write("This is an appended line.\n")
# Now reading the file again to see the changes
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
# Now deleting the file
import os
if os.path.exists("demo.txt"):
    os.remove("input i/demo.txt")
    print("File deleted successfully")      
else:
    print("The file does not exist")                