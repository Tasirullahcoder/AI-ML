
# ============================================================
# DAY 04: PYTHON STRINGS
# ============================================================

# A string is a sequence of characters enclosed in quotes.
# We can use single quotes (' '), double quotes (" "),
# or triple quotes (''' ''' / """ """) to create strings.
#
# Strings are immutable in Python.
# Immutable means that once a string is created,
# its individual characters cannot be changed directly.


# ============================================================
# TOPIC 1: STRING BASICS
# ============================================================

def string_basics():

    print("\n--- STRING BASICS ---")

    # Creating two string variables.
    word = "python"
    word2 = "I Love"

    # --------------------------------------------------------
    # 1. LENGTH OF A STRING
    # --------------------------------------------------------

    # len() is a built-in Python function.
    # It returns the total number of characters in a string.
    # Spaces are also counted as characters.

    print("Length of word:", len(word))

    # Output: 6

    # --------------------------------------------------------
    # 2. STRING CONCATENATION
    # --------------------------------------------------------

    # Concatenation means joining two or more strings.
    # The + operator is used to join strings.
    # We add " " to place a space between the two strings.

    print("Concatenation:", word2 + " " + word)

    # Output: I Love python

    # --------------------------------------------------------
    # 3. STRING INDEXING
    # --------------------------------------------------------

    # Indexing is used to access an individual character.
    # Python indexing starts from 0.
    #
    # p  y  t  h  o  n
    # 0  1  2  3  4  5

    # word[2] accesses the character at index 2.
    print("Value at index 2:", word[2])

    # Output: t

    # --------------------------------------------------------
    # 4. STRINGS ARE IMMUTABLE
    # --------------------------------------------------------

    # Immutable means we cannot change an existing string
    # by assigning a new character to one of its indexes.
    #
    # The following statement raises a TypeError:
    #
    # word[0] = "P"
    #
    # If we want a modified string, we can create a new string:
    # word = "P" + word[1:]
    #
    # This creates a new string; it does not modify
    # the original string in place.


# ============================================================
# TOPIC 2: STRING SLICING
# ============================================================

def string_slicing():

    print("\n--- STRING SLICING ---")

    # Creating a string.
    text = "python"

    # --------------------------------------------------------
    # 1. SLICING WITH START AND END INDEX
    # --------------------------------------------------------

    # Syntax: string[start:end]
    #
    # start is included, but end is excluded.
    #
    # p  y  t  h  o  n
    # 0  1  2  3  4  5
    #
    # text[2:4] means:
    # Start from index 2 and stop before index 4.
    # Therefore, the result is "th".

    store = text[2:4]

    print("text[2:4]:", store)

    # Output: th

    # --------------------------------------------------------
    # 2. SLICING FROM A START INDEX TO THE END
    # --------------------------------------------------------

    # If we do not provide an end index,
    # Python selects characters from the start index
    # all the way to the end of the string.

    store = text[2:]

    print("text[2:]:", store)

    # Output: thon


# ============================================================
# TOPIC 3: F-STRING
# ============================================================

def f_string():

    print("\n--- F-STRING ---")

    # Creating two integer variables.
    a = 5
    b = 10

    # Performing addition and storing the result.
    total = a + b

    # --------------------------------------------------------
    # F-STRING
    # --------------------------------------------------------

    # An f-string allows us to insert variables
    # and expressions directly inside a string.
    #
    # Write the letter f before the opening quote.
    # Use curly braces {} to insert variables or expressions.
    #
    # Python automatically replaces the variables
    # with their actual values.

    print(f"Sum of {a} and {b} is {total}")

    # Output: Sum of 5 and 10 is 15


# ============================================================
# MAIN FUNCTION: MENU-DRIVEN PROGRAM
# ============================================================

def main():

    # The while loop keeps displaying the menu
    # until the user chooses the Exit option.

    while True:

        print("\n========== DAY 04 MENU ==========")

        print("1. String Basics")
        print("2. String Slicing")
        print("3. F-String")
        print("0. Exit")

        # Taking the user's choice.
        # input() always returns the entered value as a string.

        choice = input("Enter your choice: ")

        # Calling the relevant function according to user choice.

        if choice == "1":

            string_basics()

        elif choice == "2":

            string_slicing()

        elif choice == "3":

            f_string()

        elif choice == "0":

            print("Exiting Day 04. Goodbye!")

            # break terminates the while loop.
            break

        else:

            # This block executes if the user enters
            # an option other than 0, 1, 2 or 3.

            print("Invalid choice! Please select 0, 1, 2 or 3.")


# This condition checks whether the file is being executed directly.
# If it is, the main() function will run.
if __name__ == "__main__":

    main()
