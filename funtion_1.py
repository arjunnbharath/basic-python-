# def s(a, b):
#     sum_val = a + b
#     mul = a * b
#     sub = a - b
#     div = a / b
#     return sum_val, mul, sub, div

# print("Enter two numbers")
# a = int(input("Enter first number: "))      
# b = int(input("Enter second number: "))
# result_sum, result_mul, result_sub, result_div = s(a, b)
# print("The sum of", a, "and", b, "is:", result_sum)
# print("The product is:", result_mul)
# print("The difference is:", result_sub)
# print("The division result is:", result_div)

# ques 1

# game = ["pubg", "cricket", "football", "hockey", "tennis"]
# animal = ["dog", "cat", "lion", "tiger", "elephant"]
# def plen(lst):
#     print("Length of the list is:", len(lst))
# plen(game)

# ques 2

# def animal_list(lst):
#     print("Animal list is:", lst)
#     for i in lst:
#         print(i, end=' ')
#    # Print a newline after the loop
# animal_list(animal)

# ques 3
# n=int(input("Enter a number: "))
# def is_factorial(a):
#     factorial = 1
#     for i in range(1, a + 1):
#         factorial *= i
#     print(factorial)  

# is_factorial(n)

# ques 4
s=input("Enter the $: ")

def dollar_to_rupee(dollar):
    rs= dollar * 82.5
    print(f"{dollar} dollars is equal to {rs} rupees.")
dollar_to_rupee(float(s))