"""
Python Basics - Assignment 1
Each question is written as a separate function.
Run this file and select the question you want to practice.
"""

def question_1():
    """Take a user's name and age and display them."""
    print("\n--- Q1: Name and Age ---")
    user_name = input("Enter your name: ")
    user_age = input("Enter your age: ")

    print(f"Hello, {user_name}! You are {user_age} years old.")


def question_2():
    """Calculate sum, product, quotient, and positive difference."""
    print("\n--- Q2: Operations on Two Numbers ---")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Sum:", num1 + num2)
    print("Product:", num1 * num2)

    if num2 != 0:
        print("Quotient:", num1 / num2)
    else:
        print("Quotient: cannot divide by zero.")

    print("Difference:", abs(num1 - num2))


def question_3():
    """Calculate the average of three numbers."""
    print("\n--- Q3: Average of Three Numbers ---")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    average = (num1 + num2 + num3) / 3
    print("Average:", average)


def question_4():
    """Show the types returned by input and type conversions."""
    print("\n--- Q4: Type Checking and Conversion ---")
    value = input("Enter a number: ")

    print("Original value type:", type(value))
    print("Integer type:", type(int(value)))
    print("Float type:", type(float(value)))
    print("String type:", type(str(value)))


def question_5():
    """Demonstrate operator precedence."""
    print("\n--- Q5: Operator Precedence ---")
    result = 10 + 3 * 2 ** 2

    print("Expression: 10 + 3 * 2 ** 2")
    print("Result:", result)
    print("Exponentiation is evaluated before multiplication,")
    print("and multiplication is evaluated before addition.")


def question_6():
    """Swap the values of two variables using a temporary variable."""
    print("\n--- Q6: Swap Two Variables ---")
    num1 = input("Enter the first value: ")
    num2 = input("Enter the second value: ")

    print("Before swapping:", num1, num2)

    temp = num1
    num1 = num2
    num2 = temp

    print("After swapping:", num1, num2)


def question_7():
    """Convert Celsius temperature to Fahrenheit."""
    print("\n--- Q7: Celsius to Fahrenheit ---")
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32

    print("Temperature in Fahrenheit:", fahrenheit)


def question_8():
    """Calculate the area of a circle."""
    print("\n--- Q8: Area of a Circle ---")
    radius = float(input("Enter the radius: "))
    pi = 3.14
    area = pi * radius ** 2

    print("Area of the circle:", area)


def question_9():
    """Calculate simple interest."""
    print("\n--- Q9: Simple Interest ---")
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate (%): "))
    time = float(input("Enter the time in years: "))

    simple_interest = (principal * rate * time) / 100
    print("Simple interest:", simple_interest)


def question_10():
    """Display the integer part and two decimal digits of a number."""
    print("\n--- Q10: Integer and Decimal Parts ---")
    value = float(input("Enter a decimal number: "))

    # Format to two decimal places to avoid floating-point display surprises.
    formatted_value = f"{value:.2f}"
    integer_part, decimal_part = formatted_value.split(".")

    print("Integer part:", integer_part)
    print("Decimal part (two digits):", decimal_part)


QUESTIONS = {
    "1": question_1,
    "2": question_2,
    "3": question_3,
    "4": question_4,
    "5": question_5,
    "6": question_6,
    "7": question_7,
    "8": question_8,
    "9": question_9,
    "10": question_10,
}


def main():
    while True:
        print("\n========== PYTHON BASICS: ASSIGNMENT 1 ==========")
        for number in QUESTIONS:
            print(f"{number}. Question {number}")
        print("0. Exit")

        choice = input("Choose a question (0-10): ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        selected_question = QUESTIONS.get(choice)
        if selected_question is None:
            print("Invalid choice. Please select a question from 1 to 10.")
        else:
            selected_question()


if __name__ == "__main__":
    main()
