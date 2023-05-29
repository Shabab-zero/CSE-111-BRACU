# Task-9

class buttons:
    def __init__(self, word, spaces, border):
        print(f"{word} Button Specifications:")
        print("Button name:", word)
        border_char_top_bottom = 1 + spaces + len(word) + spaces + 1
        print("Number of the border characters for the top and the bottom:", border_char_top_bottom)
        print("Number of spaces between the left side border and the first character of the button name:", spaces)
        print("Number of spaces between the right side border and the last character of the button name:", spaces)
        print("Characters representing the borders:", border)
        print(border * border_char_top_bottom)
        print(border + ' ' * spaces + word + spaces * ' ' + border)
        print(border * border_char_top_bottom)


word = "CANCEL"
spaces = 10
border = 'x'
b1 = buttons(word, spaces, border)
print("=======================================================")
b2 = buttons("Notify",3, '!')
print("=======================================================")
b3 = buttons('SAVE PROGRESS', 5, '$')