# Create a global variable.
number: int = 0


def main():
    global number
    number = int(input('Enter a number: '))
    show_number()


def show_number():
    print(f'The number you entered is {number}.')


# Call the main function.
main()
