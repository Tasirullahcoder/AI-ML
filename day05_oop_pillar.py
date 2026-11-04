
# ============================================================
# DAY 05 (PART 2): ADVANCED OOP CONCEPTS
# ============================================================
# OOP has four important concepts:
#
# 1. Encapsulation
# 2. Inheritance
# 3. Abstraction
# 4. Polymorphism
# ============================================================


# ============================================================
# TOPIC 1: ENCAPSULATION
# ============================================================
# Encapsulation means wrapping data (attributes) and methods
# (functions) together inside a single class.
#
# It also helps control access to an object's data.
#
# Python has three common access conventions:
#
# 1. Public:
#    Can be accessed inside and outside the class.
#
# 2. Protected:
#    Written with a single underscore (_).
#    Intended for use inside the class and its subclasses.
#    This is a convention, not strict access restriction.
#
# 3. Private:
#    Written with double underscores (__).
#    Python uses name mangling to make direct access harder.
# ============================================================

def encapsulation():

    print("\n--- ENCAPSULATION ---")

    # --------------------------------------------------------
    # 1. PUBLIC AND PROTECTED ATTRIBUTES
    # --------------------------------------------------------

    class BankAccount:

        def __init__(self, name, balance):

            # Public attribute:
            # Can be accessed directly through the object.
            self.name = name

            # Protected attribute:
            # Single underscore indicates intended internal use.
            self._balance = balance

    # Creating an object of BankAccount.
    acc1 = BankAccount("Anwar", 100_000)

    # Accessing public and protected attributes.
    print("Name:", acc1.name)
    print("Balance:", acc1._balance)

    # --------------------------------------------------------
    # 2. PRIVATE AND PUBLIC ATTRIBUTES
    # --------------------------------------------------------

    class BankAccount:

        def __init__(self, name, balance):

            # Public attribute.
            self.name = name

            # Private attribute:
            # Double underscore triggers name mangling.
            self.__balance = balance

        # GETTER METHOD
        # Used to access the private attribute.
        def get(self):
            return self.__balance

        # SETTER METHOD
        # Used to update the private attribute.
        def set(self, new_balance):
            self.__balance = new_balance

    # Creating an object.
    acc1 = BankAccount("Anwar", 100_000)

    # Calling setter to update the private balance.
    acc1.set(200_000)

    # Calling getter to access the updated balance.
    print("\nName:", acc1.name)
    print("Updated Balance:", acc1.get())


# ============================================================
# TOPIC 2: INHERITANCE
# ============================================================
# Inheritance allows a child class to reuse attributes
# and methods from a parent (base) class.
#
# Benefits:
# 1. Code reusability.
# 2. Less code duplication.
# 3. Better code organization.
# ============================================================

def inheritance():

    print("\n--- INHERITANCE ---")

    # --------------------------------------------------------
    # 1. SINGLE-LEVEL INHERITANCE
    # --------------------------------------------------------

    class Employee:

        # Parent class attributes.
        startTime = "10am"
        endTime = "6pm"

        # Parent class instance method.
        def change_time(self, new_time):
            self.startTime = new_time

    # Teacher inherits from Employee.
    class Teacher(Employee):

        def __init__(self, subject):

            # Instance attribute of Teacher.
            self.subject = subject

    # Creating an object of the child class.
    t1 = Teacher("Math")

    # Calling the inherited method from Employee.
    t1.change_time("9am")

    # Accessing child and inherited parent attributes.
    print("\nSingle-Level Inheritance:")
    print(t1.subject, t1.startTime, t1.endTime)

    # --------------------------------------------------------
    # 2. MULTILEVEL INHERITANCE
    # --------------------------------------------------------
    # In multilevel inheritance:
    # A child class inherits from another child class.
    #
    # Employee -> AdminStaff -> Accountant
    #
    # Accountant inherits from AdminStaff.
    # AdminStaff inherits from Employee.

    class Employee:

        startTime = "10am"
        endTime = "6pm"

    class AdminStaff(Employee):

        def __init__(self, role):

            self.role = role

    class Accountant(AdminStaff):

        def __init__(self, salary, role):

            # super() calls the parent class initializer.
            # Here it calls AdminStaff.__init__().
            super().__init__(role)

            self.salary = salary

    # Creating an object of Accountant.
    acc1 = Accountant(15_000, "CA")

    # Accessing attributes from all three classes.
    print("\nMultilevel Inheritance:")
    print(
        acc1.role,
        acc1.salary,
        acc1.startTime,
        acc1.endTime
    )

    # --------------------------------------------------------
    # 3. MULTIPLE INHERITANCE
    # --------------------------------------------------------
    # Multiple inheritance means a child class
    # inherits from more than one parent class.
    #
    # TA inherits from both Teacher and Student.

    class Teacher:

        def __init__(self, salary):
            self.salary = salary

    class Student:

        def __init__(self, gpa):
            self.gpa = gpa

    class TA(Teacher, Student):

        def __init__(self, name, salary, gpa):

            # Initialize Teacher's attributes.
            super().__init__(salary)

            # Initialize Student's attributes.
            Student.__init__(self, gpa)

            self.name = name

    # Creating an object of TA.
    ta1 = TA("Khan", 20_000, 3.7)

    # Accessing attributes inherited from both parent classes.
    print("\nMultiple Inheritance:")
    print(ta1.name, ta1.salary, ta1.gpa)


# ============================================================
# TOPIC 3: ABSTRACTION
# ============================================================
# Abstraction means hiding internal implementation details
# and showing only the essential features.
#
# An abstract class acts as a blueprint for other classes.
#
# We use the abc module:
# ABC          -> To create an abstract base class.
# abstractmethod -> To define a method that child classes
#                   must implement.
# ============================================================

def abstraction():

    print("\n--- ABSTRACTION ---")

    # Importing ABC and abstractmethod.
    from abc import ABC, abstractmethod

    # Abstract base class.
    class Animal(ABC):

        # Abstract method.
        # We declare the method here but do not implement it.
        @abstractmethod
        def make_sound(self):
            pass

    # Lion inherits from Animal.
    class Lion(Animal):

        # Implementing the abstract method.
        def make_sound(self):
            print("Lion says: Roar")

    # Cow inherits from Animal.
    class Cow(Animal):

        # Implementing the abstract method.
        def make_sound(self):
            print("Cow says: Moo")

    # Creating objects of child classes.
    lion = Lion()
    cow = Cow()

    # Calling their implemented methods.
    lion.make_sound()
    cow.make_sound()

    # IMPORTANT:
    # We cannot directly create an object of Animal
    # because it contains an unimplemented abstract method.
    #
    # animal = Animal()  # This raises TypeError.


# ============================================================
# TOPIC 4: POLYMORPHISM
# ============================================================
# POLY means MANY.
# MORPHISM means FORMS.
#
# Polymorphism means the same interface or method name
# can behave differently in different situations.
#
# Examples:
# 1. Operator Overloading.
# 2. Method Overriding.
# 3. Duck Typing.
# ============================================================

def polymorphism():

    print("\n--- POLYMORPHISM ---")

    # --------------------------------------------------------
    # 1. OPERATOR OVERLOADING
    # --------------------------------------------------------
    # Operator overloading means the same operator
    # performs different operations depending on data types.
    #
    # Example:
    # + adds two numbers.
    # + joins two strings.

    print("\nOperator Overloading:")

    print(1 + 2)
    print("Hello " + "World")

    # --------------------------------------------------------
    # 2. METHOD OVERRIDING
    # --------------------------------------------------------
    # Method overriding happens when a child class
    # defines a method with the same name as its parent class.
    #
    # The child class implementation is used when called
    # through the child object's method.

    class Employee:

        def get_designation(self):
            print("Designation = Employee")

    class Teacher(Employee):

        # Overriding the parent class method.
        def get_designation(self):
            print("Designation = Teacher")

    # Creating an object of Teacher.
    t1 = Teacher()

    # Calls the overridden method from Teacher.
    print("\nMethod Overriding:")
    t1.get_designation()

    # --------------------------------------------------------
    # 3. DUCK TYPING
    # --------------------------------------------------------
    # Duck typing means an object's suitability depends
    # on the methods and behavior it provides,
    # rather than its actual class or type.
    #
    # Example:
    # If two different classes have the same method name,
    # we can call that method on objects of both classes.

    class Teacher:

        def get_designation(self):
            print("Designation = Teacher")

    class Accountant:

        def get_designation(self):
            print("Designation = Accountant")

    # Creating objects of different classes.
    t1 = Teacher()
    acc1 = Accountant()

    # Both objects have the same method name.
    # Each object executes its own implementation.

    print("\nDuck Typing:")
    t1.get_designation()
    acc1.get_designation()


# ============================================================
# MAIN FUNCTION: MENU-DRIVEN PROGRAM
# ============================================================

def main():

    # while True keeps displaying the menu
    # until the user chooses Exit.
    while True:

        print("\n========== DAY 05 OOP PART 2 MENU ==========")

        print("1. Encapsulation")
        print("2. Inheritance")
        print("3. Abstraction")
        print("4. Polymorphism")
        print("0. Exit")

        # Taking input from the user.
        choice = input("\nSelect an option: ")

        # Calling the relevant function.
        if choice == "1":
            encapsulation()

        elif choice == "2":
            inheritance()

        elif choice == "3":
            abstraction()

        elif choice == "4":
            polymorphism()

        elif choice == "0":
            print("Exiting Day 05 OOP Part 2. Goodbye!")
            break

        else:
            print("Invalid choice! Please select 0 to 4.")


# This condition checks whether the file is being
# executed directly.
#
# If it is, main() will run.
if __name__ == "__main__":
    main()
