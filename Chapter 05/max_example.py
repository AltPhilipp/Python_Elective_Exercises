# Determining max of two values

def main():
    # Defining local variables
    num1 = 0
    num2 = 0

    # Asking user to enter values
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = maximum(num1, num2)

    print(f"The maximum value of {num1} and {num2} is {result}")


def maximum(num1: int, num2: int) -> int:
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2


# Call method
main()
