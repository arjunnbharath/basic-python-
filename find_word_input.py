def check_for_line() :
    word ="learning"
    data =True
    lime_no = 1
    with open("test.txt", "r") as f:
        while data:
            data = f.readline()
          
            if word in data:
                print(f"The word '{word}' is found in line {lime_no + 1}.")
                print(f"Line {lime_no + 1}: {data.strip()}")
                lime_no += 1
                break
        else:
            print(f"The word '{word}' is not found in the file.")
# Uncomment the following lines to create a file named "test.txt" with some content
# with open("test.txt", "w") as f:
check_for_line()
