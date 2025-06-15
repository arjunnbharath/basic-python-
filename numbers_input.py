def numbers():
    even_no = []
    odd_no = []
    
    with open("numbers.txt", "r") as f:
        data = f.read()
        print("Raw data:", data)
        
        num_list = data.split(",")  # Split the data by commas
        for num in num_list:
            num = num.strip()  # Remove whitespace
            if num.isdigit():  # Check if it's a valid number
                n = int(num)
                print(n)
                if n % 2 == 0:
                    even_no.append(n)
                else:
                    odd_no.append(n)

    # Calculate sums
    sum_even = sum(even_no)
    sum_odd = sum(odd_no)

    # Output results
    print("Even numbers:", even_no)
    print("Sum of even numbers:", sum_even)
    print("Odd numbers:", odd_no)
    print("Sum of odd numbers:", sum_odd)

# Call the function
numbers()
