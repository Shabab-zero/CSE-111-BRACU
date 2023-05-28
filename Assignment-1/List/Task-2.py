# Task-2

N = int(input("Enter number of lists: "))
highest_sum = float('-inf')
highest_sum_list = None

for i in range(N):
    input_list = [int(j) for j in input(f"Enter list {i + 1}: ").split()]
    sum = 0
    for j in input_list:
        sum += j

    if sum > highest_sum:
        highest_sum = sum
        highest_sum_list = input_list

print("Highest sum:", highest_sum)
print("Highest sum list:", highest_sum_list)