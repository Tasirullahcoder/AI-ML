
# ==========================================================
# DAY 05: OBJECT-ORIENTED PROGRAMMING (OOP)
# ==========================================================
# OOP is a programming approach based on Classes and Objects.
# It helps us organize code and represent real-world entities.
#
# Topics:
# 1. Class and Object
# 2. Constructor and Instance Method
# 3. Class and Instance Attributes
# 4. Instance, Class and Static Methods
# 5. Online Store Problem


# ==========================================================
# TOPIC 1: CLASS AND OBJECT
# ==========================================================
# A CLASS is a blueprint used to create objects.
# An OBJECT is an instance of a class.
#
# We create an object by calling the class name.
# We can access class attributes using an object.


def class_and_object():

    print("\n--- CLASS AND OBJECT ---")

    # Creating a class named Student
    class Student:
        subject = "Python"
        college = "ABC"
        year = 4

    # Creating an object of Student class
    st1 = Student()

    # Accessing class attributes through an object
    print("Subject:", st1.subject)
    print("College:", st1.college)
    print("Year:", st1.year)

    print("\n--- MULTIPLE OBJECTS ---")

    # Creating another class with common attributes
    class StudentInfo:
        subject = "Python"
        cgpa = 3.33
        college = "ABC"

    # Creating an object
    student = StudentInfo()

    # Using a loop to print the same object's information
    # range(1, 10) generates numbers from 1 to 9.
    for number in range(1, 10):
        print(student.subject, student.college, student.cgpa)


# ==========================================================
# TOPIC 2: CONSTRUCTOR AND INSTANCE METHOD
# ==========================================================
# A constructor is commonly used to initialize an object.
# In Python, __init__() is the initializer method.
#
# It is automatically called when we create an object.
# self refers to the current object.
#
# An INSTANCE METHOD is a method that works with an object.
# It receives self as its first parameter.


def constructor_and_instance_method():

    print("\n--- CONSTRUCTOR AND INSTANCE METHOD ---")

    class Student:

        def __init__(self, name, subject, cgpa, university):
            # Initializing instance attributes
            self.name = name
            self.subject = subject
            self.university = university
            self.cgpa = cgpa

        # Instance method to return student's CGPA
        def get_cgpa(self):
            return self.cgpa

        # Instance method to display student information
        def get_info(self):
            print(f"Name: {self.name}")
            print(f"Subject: {self.subject}")
            print(f"University: {self.university}")
            print(f"CGPA: {self.cgpa}")

    # Creating an object and passing values to constructor
    st1 = Student("Yasir", "Python", 3.33, "Peshawar")

    # Calling instance methods
    st1.get_info()

    # Calling get_cgpa() to return CGPA
    print("Returned CGPA:", st1.get_cgpa())


# ==========================================================
# TOPIC 3: CLASS AND INSTANCE ATTRIBUTES
# ==========================================================
# CLASS ATTRIBUTES:
# - Belong to the class.
# - Shared by all objects unless overridden.
# - Defined directly inside the class.
#
# INSTANCE ATTRIBUTES:
# - Belong to individual objects.
# - Usually defined using self inside __init__().
# - Each object can have different values.


def class_and_instance_attributes():

    print("\n--- CLASS AND INSTANCE ATTRIBUTES ---")

    class Employee:

        # Class attribute: common for all employees
        office = "ABC"

        def __init__(self, name, salary):
            # Instance attributes: different for each employee
            self.name = name
            self.salary = salary

    # Creating first employee object
    emp1 = Employee("Tasir", 30000)

    # Creating second employee object
    emp2 = Employee("Ali", 40000)

    # Accessing instance attributes
    print(f"Employee: {emp1.name}, Salary: {emp1.salary}")
    print(f"Employee: {emp2.name}, Salary: {emp2.salary}")

    # Accessing class attribute through class
    print("Office:", Employee.office)

    # Class attribute can also be accessed through objects
    print("Office:", emp1.office)
    print("Office:", emp2.office)


# ==========================================================
# TOPIC 4: INSTANCE, CLASS AND STATIC METHODS
# ==========================================================
# Python provides three commonly used method types:
#
# 1. INSTANCE METHOD:
#    - Receives self as its first parameter.
#    - Can access instance and class attributes.
#
# 2. CLASS METHOD:
#    - Uses @classmethod decorator.
#    - Receives cls as its first parameter.
#    - Can access and modify class attributes.
#
# 3. STATIC METHOD:
#    - Uses @staticmethod decorator.
#    - Does not require self or cls.
#    - Does not automatically access instance or class attributes.
#    - Used for utility operations related to the class.


def instance_class_static_methods():

    print("\n--- INSTANCE, CLASS AND STATIC METHODS ---")

    class Laptop:

        # Class attribute
        storage_type = "SSD"

        def __init__(self, RAM, storage):
            # Instance attributes
            self.RAM = RAM
            self.storage = storage

        # 1. INSTANCE METHOD
        # Uses self to access object attributes.
        def get_info(self):
            print(
                f"Laptop RAM: {self.RAM}, "
                f"Storage: {self.storage}, "
                f"Storage Type: {self.storage_type}"
            )

        # 2. CLASS METHOD
        # Uses cls to access class attributes.
        @classmethod
        def get_storage_type(cls):
            print(f"Storage Type: {cls.storage_type}")

        # 3. STATIC METHOD
        # Does not require self or cls.
        # Calculates the final price after discount.
        @staticmethod
        def cal_discount(price, discount):
            final_price = price - (price * discount / 100)
            print(f"Final Price After Discount: Rs {final_price}")

    # Creating laptop objects
    laptop1 = Laptop("16GB", "512GB")
    laptop2 = Laptop("8GB", "300GB")

    # Calling instance method
    laptop1.get_info()
    laptop2.get_info()

    # Calling class method
    Laptop.get_storage_type()

    # Calling static method
    Laptop.cal_discount(40000, 10)


# ==========================================================
# TOPIC 5: PROBLEM 1 - ONLINE STORE
# ==========================================================
# Problem Requirements:
# 1. Create an online store for products (name and price).
# 2. Track the total number of products created.
# 3. Create a static method to calculate product discounts.
#
# Concepts used:
# - Class
# - Constructor
# - Instance Attributes
# - Class Attributes
# - Instance Method
# - Class Method
# - Static Method


def online_store_problem():

    print("\n--- ONLINE STORE ---")

    class Product:

        # Class attribute to track total products
        count = 0

        def __init__(self, name, price):

            # Instance attributes
            self.name = name
            self.price = price

            # Increase product count whenever an object is created
            Product.count += 1

        # Instance method to display product information
        def get_info(self):
            print(f"Product: {self.name}")
            print(f"Price: Rs {self.price}")

        # Class method to display total products
        @classmethod
        def get_count_product(cls):
            print(f"Total Products in Store: {cls.count}")

        # Static method to calculate discount
        @staticmethod
        def cal_discount(price, discount):

            # Calculate price after discount
            final_price = price - (price * discount / 100)

            print(f"Original Price: Rs {price}")
            print(f"Discount: {discount}%")
            print(f"Final Price: Rs {final_price}")

    # Creating product objects
    p1 = Product("Laptop", 50000)
    p2 = Product("Phone", 10000)
    p3 = Product("Pen", 100)

    # Displaying product information
    p1.get_info()
    print()

    p2.get_info()
    print()

    p3.get_info()
    print()

    # Displaying total number of products
    Product.get_count_product()

    print("\n--- PRODUCT DISCOUNT ---")

    # Calculating discount on laptop
    Product.cal_discount(p1.price, 15)


# ==========================================================
# MAIN MENU
# ==========================================================
# The main() function displays all available topics.
# The user selects an option to execute the desired function.
# The while loop keeps the menu running until user exits.


def main():

    while True:

        print("\n========================================")
        print("       DAY 05: OOP LEARNING MENU")
        print("========================================")

        print("1. Class and Object")
        print("2. Constructor and Instance Method")
        print("3. Class and Instance Attributes")
        print("4. Instance, Class and Static Methods")
        print("5. Online Store Problem")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            class_and_object()

        elif choice == "2":
            constructor_and_instance_method()

        elif choice == "3":
            class_and_instance_attributes()

        elif choice == "4":
            instance_class_static_methods()

        elif choice == "5":
            online_store_problem()

        elif choice == "0":
            print("\nThank you for learning Python OOP!")
            break

        else:
            print("\nInvalid choice! Please select 0 to 5.")


# Program execution starts here.
# This condition prevents main() from running automatically
# when this file is imported into another Python file.

if __name__ == "__main__":
    main()
