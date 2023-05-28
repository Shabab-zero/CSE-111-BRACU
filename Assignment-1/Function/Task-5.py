# Task-5

def palindrome_check(given_string):
    if given_string == given_string[:: -1]:
        return 'Palindrome'
    else:
        return 'Not a palindrome'
    
user_input = input('Enter a string to check palindrome or not: ').replace(' ', '')
print(palindrome_check(user_input))