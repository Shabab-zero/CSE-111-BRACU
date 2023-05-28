# Task-4

cellphone_t9 = {1: '.,?!:', 
                2: 'ABC', 
                3: 'DEF', 
                4: 'GHI', 
                5: 'JKL', 
                6: 'MNO', 
                7: 'PQRS', 
                8: 'TUV', 
                9: 'WXYZ', 
                0: ' '}

user_input = input('Enter a text: ').upper()
keystrokes = ''

for char in user_input:
    for key, value in cellphone_t9.items():
        if char in value:
            keystrokes += str(key) * (value.index(char) + 1)
            continue #For efficiency purposes. Will work without continue

print(keystrokes)