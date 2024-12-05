def calculator():
    print("welcome to gthe calculator!")
    print("Choose an operation:")
    print("1. Addition:")
    print("2.Subtration")
    print("3.Multiplication")
    print("4.Division")
try:
    choice = input("Enter your choice(1/2/3/4):")
    num1 = float(input("enter the first number:"))
    num2 = float(input("Enter the second number:"))

    if choice == "1":
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
    elif choice == "2":
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}")
    elif choice == "3":
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}")
    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1}/{num2} is {result}")
        else:
            print("Error: Division by Zero is not allowed!")
except ValueError:
    print("Invalid Input! Please enter numeric number")

calculator()