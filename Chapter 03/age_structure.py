age: int = int(input('Enter your age: '))

# Determine the grade.
if 0 <= age <= 1:
    print('Your are an infant.')
elif 1 < age < 13:
    print('Your are a child.')
elif 13 <= age < 20:
    print('Your are a teenager.')
elif age >= 20:
    print('Your are an adult.')
else:
    print('Invalid age.')

"""
match age:
        case age if 0 <= age <= 1:
            print("123")
        case "Start":
            i = 0
            while i < 10:
                if i == 9:
                    print("Hello World #10")
                else:
                    print("Hello World")
                i += 1
        case _:
            print("Default Case")
"""