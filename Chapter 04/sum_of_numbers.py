
sum = 0.0
number = 1.0

number = int(input("Enter number(s) and -1 to calculate sum: "))

while number != -1:
    if number >= 0:
        sum = sum + number
        number = int(input("Enter number(s) and -1 to calculate sum: "))
    else:
        print("Invalid input")
        break
print(f"The sum of all numbers is {sum:.2f}")
