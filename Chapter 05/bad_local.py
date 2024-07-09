# Definition of the main function.
name = ""


def main():
    get_name()
    print(f'Hello {name}.')  # This causes an error if not global name defined!


# Definition of the get_name function.
def get_name():
    global name  #This variable is valid globally
    name = input('Enter your name: ')


# Call the main function.
main()
