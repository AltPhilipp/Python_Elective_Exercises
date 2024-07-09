import sympy

number = int(input("Enter a number: "))

while number != -1:
    if sympy.isprime(number):
        print(number, "is a prime number")
    else:
        print(number, "is not a prime number")
    number = int(input("Enter a number: "))
    