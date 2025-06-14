
# Write a program that takes a string input and prints it in reverse.

# print("entera string")
# s=input()
# rev=s[::-1]
# print("The reverse of the string is:", rev) 

#Create a list of numbers and print the sum of all the elements.
# a=[1,2,3,4,5]
# b=sum(a)
# print("The sum of the list is:", b)

# Create a list of numbers and print the maximum and minimum elements.

# numbers = [10, 5, 25, 8, 99, 1]
# largest = max(numbers)
# smallest = min(numbers)
# print("The list is:", numbers)
# print("The largest number is:", largest)
# print("The smallest number is:", smallest)
numbers = []

for i in range(5):
    num =int(input(f"Enter number {i+1}: "))
    numbers.append(num)

numbers.sort()
print("Sorted list:", numbers)

