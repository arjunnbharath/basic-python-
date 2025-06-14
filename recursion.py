## Recursive function to print numbers from n to 1
# def sum(n):
#  def show(n):
#     if n == 0:
#         return 0
#     print(n)
#     show(n - 1)
#     print("AAA")
# show(5)    
#---------------------------------

 
# Recursive function to calculate the sum of numbers from 1 to n    
# def sum(n):
#     if (n==0) :
#      return 0
#     return n + sum(n - 1)

# print(sum(5)) 
# -----------------------------------


# write a recursive funtion to print all the elements in a list
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
def print_list(lst, index=0):
    if index == len(lst):
        return
    print(lst[index])
    print_list(lst, index + 1)

print_list(list)

