# Task-1

def BMI(height, weight):
    BMI = round(weight / (height / 100) ** 2, 1) #Round value to 1 decimal place
    if BMI < 18.5:
        comment = 'Underweight'
    elif BMI <= 24.9:
        comment = 'Normal'
    elif BMI <= 30:
        comment = 'Overweight'
    else:
        comment = 'Obese'
    print(f"Score is {BMI}. You are {comment}")

BMI(175, 96)
BMI(152, 48)