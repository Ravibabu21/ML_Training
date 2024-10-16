# Functions for basic arithmetic operations
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    # Handle divide by zero error
    if num2 == 0:
        return "Error! Division by zero."
    return num1 / num2
def expower(base, exponent):
    return base ** exponent

def squRoot(num1):
    return (num1**(1/2))
def factorial_num(num1):
    if num1 < 0:
        return "Factorial is not defined for negative numbers."
    if num1 == 0 or num1 == 1:
        return 1
    return num1 * factorial_num(num1 - 1)

def display_menu():
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponential")
    print("6. SquareRoot")
    print("7. Factorial")
    print("8. Exit")

def calculator():
    while True:
        display_menu()
        # Ask user to choose an operation
        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        # Exit condition
        if choice == '8':
            print("Exiting the calculator. Have a Great Day!👍")
            break

        # Ensure valid choice
        if choice in ['1', '2', '3', '4','5','6','7']:
            try:
                num1 = float(input("Enter first number: "))
                # For exponentiation and square root, num2 might not be needed
                if choice in ['5']:
                    num2 = float(input("Enter the exponent: "))
                elif choice in ['6']:
                    num2 = None  # Square root does not need a second number
                elif choice in ['7']:
                    num2 = None  # to find factorial, does not need a second number
                else:
                    num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            # Perform the chosen operation
            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            elif choice =='5':
                result= expower(num1,num2)
            elif choice=='6':
                result=squRoot(num1)
            elif choice=='7':
                result=factorial_num(num1)
            print(f"Result: {result}")
        else:
            print("Invalid choice! Please select a valid option.")

# Call the calculator function to start the program
calculator()
