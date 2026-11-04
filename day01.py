"""
Python Basics - Day 1
Topics: Operators, Type Conversion, Input, and Conditional Statements.

Run this file and choose an example from the menu.
"""

def arithmetic_operators():
    print("\n--- Arithmetic Operators ---")
    a = 10
    b = 5

    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
    print("Modulus (remainder):", a % b)
    print("Exponentiation:", a ** b)


def type_conversion():
    print("\n--- Type Conversion ---")

    # Implicit conversion: Python converts the integer to a float automatically.
    implicit_result = 5 + 10.0

    # Explicit conversion (type casting): the programmer converts the value.
    explicit_result = int(5 + 10.0)

    print("Implicit conversion:", implicit_result, type(implicit_result))
    print("Explicit conversion:", explicit_result, type(explicit_result))


def user_input():
    print("\n--- User Information ---")
    user_name = input("Enter your name: ")
    user_age = input("Enter your age: ")

    print(f"Your name is {user_name}. You are {user_age} years old.")


def average_of_two_numbers():
    print("\n--- Average of Two Numbers ---")
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

    average = (first_number + second_number) / 2
    print("Average:", average)


def traffic_light():
    print("\n--- Traffic Light ---")
    color = input("Enter a traffic light color (red, yellow, green): ").strip().lower()

    if color == "red":
        print("Stop the car.")
    elif color == "green":
        print("You can go.")
    elif color == "yellow":
        print("Look carefully and get ready to stop.")
    else:
        print("Invalid traffic light color.")


def main():
    while True:
        print("\n========== PYTHON BASICS: DAY 1 ==========")
        print("1. Arithmetic operators")
        print("2. Type conversion")
        print("3. User input")
        print("4. Average of two numbers")
        print("5. Conditional statements (traffic light)")
        print("0. Exit")

        choice = input("Choose an example (0-5): ").strip()

        if choice == "1":
            arithmetic_operators()
        elif choice == "2":
            type_conversion()
        elif choice == "3":
            user_input()
        elif choice == "4":
            average_of_two_numbers()
        elif choice == "5":
            traffic_light()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 0 to 5.")


if __name__ == "__main__":
    main()
