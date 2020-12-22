VALID_COLORS = ['blue', 'yellow', 'red']
NOT_VALID = 'Not a valid color'


def print_colors():
    """In the while loop ask the user to enter a color,
       lowercase it and store it in a variable. Next check:
       - if 'quit' was entered for color, print 'bye' and break.
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""
    while True:
        color = input("enter a color: ").lower()
        if color == 'quit':
            print(f'bye\n')
            break
        elif color not in VALID_COLORS:
            print(NOT_VALID+'\n')
        else:
            print(f'{color}')


if __name__ == '__main__':
    result = print_colors()
