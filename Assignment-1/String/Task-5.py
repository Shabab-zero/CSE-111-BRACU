# Task-5

while True:
    password = input("Set your password: ")
    contains_lowercaseLetter = False
    contains_uppercaseLetter = False
    contains_digit = False
    contains_specialCharacter = False
    warning_messages = ''

    for char in password:
        if char.islower():
            contains_lowercaseLetter = True
        elif char.isupper():
            contains_uppercaseLetter = True
        elif char.isnumeric():
            contains_digit = True
        elif char in '_$#@':
            contains_specialCharacter = True

    if not contains_lowercaseLetter:
        warning_messages += 'Lowercase character missing, '
    if not contains_uppercaseLetter:
        warning_messages += 'Uppercase character missing, '
    if not contains_digit:
        warning_messages += 'Digit missing, '
    if not contains_specialCharacter:
        warning_messages += 'Special character missing, '

    if len(warning_messages) == 0:
        print('OK')
        break
    else:
        print(warning_messages[0: -2])