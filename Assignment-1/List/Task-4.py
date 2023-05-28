# Task-4

n, k = [int(i) for i in input().split()]
teams = [int(i) for i in input().split()]
eligible_programmers = []

for i in teams:
    if i + k <= 5:
        eligible_programmers.append(i)

number_of_teams = len(eligible_programmers) // 3
print(number_of_teams)