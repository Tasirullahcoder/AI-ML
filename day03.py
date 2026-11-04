
# ==========================================
# PYTHON BASICS - DAY 03
# Topics: Conditions, Loops, Functions
# ==========================================


# TOPIC 1: CHECK ODD OR EVEN NUMBER

def odd_or_even():
    number = int(input("Enter a number to check ODD or EVEN: "))

    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


# TOPIC 2: NESTED IF ELSE

def nested_if_else():
    user_name = input("Enter a username: ")
    user_password = input("Enter a password: ")

    if user_name == "admin" and user_password == "pass":
        print("You have successfully logged in.")
    else:
        if user_name == "admin" and user_password != "pass":
            print("Your password is wrong.")
        else:
            if user_password == "pass" and user_name != "admin":
                print("Your username is wrong.")
            else:
                print("You entered both wrong username and password.")


# TOPIC 3: MATCH CASE

def match_case():
    color = input("Enter a color: ").strip().capitalize()

    match color:
        case "Green":
            print("GO")
        case "Red":
            print("STOP")
        case "Yellow":
            print("LOOK")
        case _:
            print("Wrong color")


# TOPIC 4: WHILE LOOP

def while_loop():
    count = 1

    while count <= 5:
        print("Hello", count)
        count += 1

    print("You are out of the first loop.")

    i = 5

    while i >= 1:
        print(i)
        i -= 1

    print("You are out of the second loop.")


# TOPIC 5: MULTIPLICATION TABLE

def multiplication_table():
    number = int(input("Enter any number for multiplication table: "))

    j = 1

    while j <= 10:
        print(f"{number} x {j} = {number * j}")
        j += 1


# TOPIC 6: BREAK AND CONTINUE KEYWORDS

def break_continue():
    print("BREAK example:")

    i = 1

    while i <= 5:
        print(i)

        if i == 3:
            break

        i += 1

    print("CONTINUE example:")

    k = 0

    while k < 10:
        k += 1

        if k % 3 == 0:
            continue

        print(k)


# TOPIC 7: FOR LOOP

def for_loop():
    string = "HELLOW"

    for var in string:
        print(var)

    string = "INTERNSHIP"

    if "E" in string:
        print("YES, E exists in the string.")

    for i in range(5):
        print(i)

    word = "artificial intelligence"
    ans = 0

    for character in word:
        if character == "i":
            ans += 1
            print(ans, "=>", character)


# TOPIC 8: RANGE METHOD

def range_method():
    # range(start, stop)
    # Stop value is excluded.

    print("range(1, 10):")

    for a in range(1, 10):
        print(a)

    # range(start, stop, step)

    print("range(1, 10, 2):")

    for b in range(1, 10, 2):
        print(b)


# TOPIC 9: FUNCTIONS

def function_examples():

    # Function without parameters

    def hello():
        print("Tasirkhan")

    hello()

    # Function with parameters and return value

    def add(a, b):
        total = a + b
        return total

    print("Sum:", add(2, 5))


# TOPIC 10: LAMBDA FUNCTION AND FACTORIAL

def lambda_factorial():

    # Lambda function

    add = lambda a, b: a + b

    print("Lambda sum:", add(2, 3))

    # Factorial
    # 5! = 1 * 2 * 3 * 4 * 5 = 120

    def calculate_factorial(n):
        if n < 0:
            return None

        fact = 1

        for i in range(1, n + 1):
            fact *= i

        return fact

    number = int(input("Enter a number for factorial: "))

    result = calculate_factorial(number)

    if result is None:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"Factorial of {number} is: {result}")


# ==========================================
# MAIN FUNCTION
# ==========================================

def main():

    while True:

        print("\n========== PYTHON BASICS: DAY 03 ==========")
        print("1. Odd or Even Number")
        print("2. Nested If Else")
        print("3. Match Case")
        print("4. While Loop")
        print("5. Multiplication Table")
        print("6. Break and Continue")
        print("7. For Loop")
        print("8. Range Method")
        print("9. Functions")
        print("10. Lambda Function and Factorial")
        print("0. Exit")

        choose = input("Choose an example (0-10): ").strip()

        if choose == "1":
            odd_or_even()

        elif choose == "2":
            nested_if_else()

        elif choose == "3":
            match_case()

        elif choose == "4":
            while_loop()

        elif choose == "5":
            multiplication_table()

        elif choose == "6":
            break_continue()

        elif choose == "7":
            for_loop()

        elif choose == "8":
            range_method()

        elif choose == "9":
            function_examples()

        elif choose == "10":
            lambda_factorial()

        elif choose == "0":
            print("Goodbye! Keep practicing Python.")
            break

        else:
            print("Invalid choice. Please enter 0-10.")


# ==========================================
# PROGRAM EXECUTION
# ==========================================

if __name__ == "__main__":
    main()
