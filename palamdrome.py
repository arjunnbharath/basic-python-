pal =[]
rev=[]
print("Enter a string:")
s = input()
pal= s
rev =s[::-1]

if pal == rev:
     print("The string is a palindrome")         
else:
    print("The string is not a palindrome")