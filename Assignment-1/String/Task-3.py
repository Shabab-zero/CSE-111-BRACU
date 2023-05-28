# Task-3

input_string = input("Enter a string: ")
uppercase_index_1 = None
uppercase_index_2 = None

for i in range(len(input_string)):
    if input_string[i].isupper():
        uppercase_index_1 = i
        break
for i in range(uppercase_index_1 + 1, len(input_string)):
    if input_string[i].isupper():
        uppercase_index_2 = i

substring = input_string[uppercase_index_1 + 1: uppercase_index_2]

if len(substring) == 0:
    print('BLANK')
else:
    print(substring)