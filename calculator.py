#def read_number1():
#    number1 = float(input("Please Enter the First Number: "))

#def read_number2():
#    number2 = float(input("Please Enter the Second Number: "))

def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    return number1 / number2
print("----------------------------------")
print("Welcome to the Online Calculator")
print("----------------------------------")
print("Select operation: ")
print("1) Add")
print("2) Subtract")
print("3) Multiply")
print("4) Divide")

while True:
    operator = input("Enter operator option (Add/Subtract/Multiply/Divide): ")

    if operator in ("Add", "Subtract", "Multiply", "Divide"):
        number1 = float(input("Please Enter the First Number: "))
        number2 = float(input("Please Enter the Second Number: "))

        if operator == "Add":
            print(number1, "+", number2, "=", add(number1, number2))

        elif operator == "Subtract":
            print(number1, "-", number2, "=", subtract(number1, number2))

        elif operator == "Multiply":
            print(number1, "*", number2, "=", multiply(number1, number2))

        elif operator == "Divide":
            print(number1, "/", number2, "=", divide(number1, number2))

        next_calculation = input("Would you like to use the calculator? (yes/no): ")
        if next_calculation == "no":
            break
