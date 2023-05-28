# Task-1

print("Enter 'STOP' to stop")

numbers_list = []
unique_numbers = []

while True:
    input_number = input('Enter a number: ')
    if input_number == 'STOP':
        break
    numbers_list.append(input_number)

for i in numbers_list:
    if i not in unique_numbers:
        unique_numbers.append(i)

for i in unique_numbers:
    print(f"{i} - {numbers_list.count(i)} times")