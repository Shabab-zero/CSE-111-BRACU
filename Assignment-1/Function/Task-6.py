# Task-6

def capitalize(paragraph):
    words = paragraph.capitalize().replace(' i ', ' I ').split()
    #capitalize(): capitalizes 1st letter of a string.

    for i in range(1, len(words)):
        if words[i - 1][-1] in '.!?':
            words[i] = words[i].capitalize()
            
    return ' '.join(words)

user_input = input("Enter your paragraph: ")
print('Capitalized:', capitalize(user_input))