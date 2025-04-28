def add(a, b):
    print(f"Addition result: {a + b}")

def subtract(a, b):
    print(f"Subtraction result: {a - b}")

def multiply(a, b):
    print(f"Multiplication result: {a * b}")

def division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("You can't divide by zero")
        result = a / b
        print(f"Division result: {result}")
    except ZeroDivisionError as e:
        print(e)

def main():
    try:
        a = float(input('Enter value for a: '))
        b = float(input('Enter value for b: '))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    operation = input("Enter the operation number: ")

    if operation == "1":
        add(a, b)
    elif operation == "2":
        subtract(a, b)
    elif operation == "3":
        multiply(a, b)
    elif operation == "4":
        division(a, b)
    else:
        print("Invalid operation! Please choose a valid option.")


main()
