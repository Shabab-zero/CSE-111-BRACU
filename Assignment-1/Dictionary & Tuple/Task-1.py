# Task-1

user_input_1 = input().split(', ')
user_input_2 = input().split(', ')
combined_items = user_input_1 + user_input_2
combined_dict = {}
list_of_unique_values = []

for item in combined_items:
    key, value = item.split(':')
    if key not in combined_dict:
        combined_dict.update({key: int(value)})
    else:
        combined_dict[key] += int(value)

for value in combined_dict.values():
    if value not in list_of_unique_values:
        list_of_unique_values.append(value)

list_of_unique_values.sort()
tuple_of_unique_values = tuple(list_of_unique_values)

print(combined_dict)
print('Values:', tuple_of_unique_values)