while True:
    n = input("Enter a number: ")
    
    if n.isdigit():
        n = int(n)
        if n % 2 == 0:
            print("The number is even")
        else:
            print("The number is odd")
        break
    else:
        print("Invalid input. Please enter digits only.")
