# Task-3

print("Enter 'STOP' to stop")

while True:
    user_input = input("Enter a list: ")
    if user_input == 'STOP':
        break

    input_list = [int(i) for i in user_input.split()]
    check_list = [i for i in range(1, len(input_list))]
    
    for i in range(1, len(input_list)):
        absolute_difference = abs(input_list[i] - input_list[i - 1])
        if absolute_difference in check_list:
            check_list.remove(absolute_difference)

    if len(check_list) == 0:
        print("UB Jumper")
    else:
        print("Not UB Jumper")