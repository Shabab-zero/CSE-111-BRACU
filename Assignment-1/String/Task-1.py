# Task-1

input_string = input("Enter a string: ")
uppercase_letters = 0
lowercase_letters = 0

for char in input_string:
    if char.isupper():
        uppercase_letters += 1
    elif char.islower():
        lowercase_letters += 1

if lowercase_letters >= uppercase_letters:
    print(input_string.lower())
else:
    print(input_string.upper())