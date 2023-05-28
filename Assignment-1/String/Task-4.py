# Task-4

string_1, string_2 = input("Enter two comma separated strings: ").split(', ')
common_characters = ''

for char in string_1:
    if char in string_2:
        common_characters += char
for char in string_2:
    if char in string_1:
        common_characters += char

if len(common_characters) == 0:
    print("Nothing in common.")
else:
    print(common_characters)