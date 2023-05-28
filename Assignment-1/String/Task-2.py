# Task-2

input_string = input("Enter a string: ")

contains_letters = False
contains_digits = False

for char in input_string:
    if char.isalpha():
        contains_letters = True
    elif char.isnumeric():
        contains_digits = True

if contains_letters and contains_digits:
    print('MIXED')
elif contains_digits:
    print('NUMBER')
else:
    print('WORD')