# Task-2

def div_sum(minimum, maximum, devisor):
    sum = 0

    for i in range(minimum, maximum):
        if i % devisor == 0:
            sum += i

    return sum

print(div_sum(0, 10, 2))
print(div_sum(3, 16, 3))