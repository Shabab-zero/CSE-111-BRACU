# Task-3

user_input = input().split(', ')
dictionary = {}

for item in user_input:
    key, value = item.split(' : ')
    if value not in dictionary:
        dictionary.update({value: [key]})
    else:
        dictionary[value].append(key)

print(dictionary)