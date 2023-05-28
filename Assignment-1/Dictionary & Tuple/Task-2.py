# Task-2

print("Enter 'STOP' to stop")
dictionary = {}

while True:
    user_input = input("Enter a number: ")
    if user_input == 'STOP':
        break

    if int(user_input) not in dictionary:
        dictionary.update({int(user_input): 1})
    else:
        dictionary[int(user_input)] += 1

for number, frequency in dictionary.items():
    print(f"{number} : {frequency} times")
