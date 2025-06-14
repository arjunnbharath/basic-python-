print("Enter a string:")
s = input()
print("Enter the meaning of the string:")
meaning = input()
dictionary = {}
dictionary.update({s: meaning})

print("The dictionary is:", dictionary)
print("The meaning of the word", s, "is:", dictionary.get(s))


