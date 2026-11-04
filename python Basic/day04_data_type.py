# ============================================================
# PYTHON BASICS - DAY 04
# TOPIC: PYTHON BUILT-IN DATA TYPES
# ============================================================

# In this file, we will learn about four fundamental
# built-in data types in Python:
#
# 1. LIST
#    - Mutable: We can change, add, or remove elements.
#    - Uses square brackets: []
#    - Allows duplicate values.
#    - Ordered collection.
#    - Example: [10, 20, 30]
#
# 2. TUPLE
#    - Immutable: We cannot change its elements.
#    - Uses parentheses: ()
#    - Allows duplicate values.
#    - Ordered collection.
#    - Example: (10, 20, 30)
#
# 3. DICTIONARY
#    - Mutable: We can add, update, or remove items.
#    - Uses curly brackets: {}
#    - Stores data in key-value pairs.
#    - Keys must be unique.
#    - Example: {"name": "Tasir", "age": 22}
#
# 4. SET
#    - Mutable: We can add or remove elements.
#    - Uses curly brackets: {}
#    - Stores unique values (no duplicates).
#    - Unordered collection.
#    - Example: {10, 20, 30}
#
# IMPORTANT:
# - List and Tuple both store multiple values,
#   but List is mutable and Tuple is immutable.
#
# - Dictionary and Set both use curly brackets,
#   but Dictionary stores key-value pairs while
#   Set stores unique individual values.
#
# - An empty Dictionary is written as: {}
# - An empty Set is written as: set()
#
# ============================================================
# TOPICS COVERED IN THIS FILE
# ============================================================
#
# 1. List and List Methods
# 2. Tuple and Tuple Methods
# 3. Dictionary and Dictionary Methods
# 4. Set and Set Methods
# 5. Problem 1 - Find Unique Courses
# 6. Problem 2 - Find Students Taking English
# 7. Problem 3 - Group Courses by Student
#
# ============================================================


# DATA FOR PRACTICE PROBLEMS

info = [
    ("alice", "math"),
    ("bob", "science"),
    ("alice", "science"),
    ("charlie", "math"),
    ("bob", "math"),
    ("alice", "english"),
    ("charlie", "english")
]


# ============================================================
# TOPIC 1: LIST AND LIST METHODS
# ============================================================

def list_examples():

    # A List is a mutable and ordered collection.
    # It allows duplicate values and uses square brackets [].

    marks = [1, 2, 3, 4, 5, "tasir"]

    print("Original List:", marks)
    print("Data Type:", type(marks))

    # Accessing an element using its index
    print("Value at index 2:", marks[2])

    # Updating an element in a List
    marks[3] = 10
    print("After updating index 3:", marks)

    # Iterating through a List using a for loop
    print("\nLoop through List:")

    for x in marks:
        print(x)

    # ---------------- LIST METHODS ----------------

    val = [1, 3, 5, 6, 7]

    print("\nOriginal List:", val)

    # 1. append()
    # Adds an element at the end of the List.
    val.append(10)
    print("After append:", val)

    # 2. insert()
    # Inserts an element at a specific index.
    val.insert(1, 60)
    print("After insert:", val)

    # 3. sort()
    # Sorts the List in ascending order by default.
    val.sort()
    print("After sort:", val)

    # 4. reverse()
    # Reverses the order of elements in the List.
    val.reverse()
    print("After reverse:", val)

    # Finding a value using a for loop and break
    for x in val:
        if x == 10:
            print("Found value:", x)
            break


# ============================================================
# TOPIC 2: TUPLE AND TUPLE METHODS
# ============================================================

def tuple_examples():

    # A Tuple is an immutable and ordered collection.
    # It allows duplicate values and uses parentheses ().
    # Once created, its elements cannot be changed.

    tup = (1, 2, 3, 4, 5, "abc")

    print("Tuple:", tup)
    print("Data Type:", type(tup))

    # Creating a Tuple with a single element.
    # A comma is necessary to make it a Tuple.
    a = (1,)

    print("Single Value Tuple:", a)
    print("Data Type:", type(a))

    # ---------------- TUPLE METHODS ----------------

    b = (1, 2, 3, 2, 5, 2)

    # 1. index()
    # Returns the index of the first occurrence of a value.
    print("\nIndex of 5:", b.index(5))

    # 2. count()
    # Returns how many times a value appears.
    print("Count of 2:", b.count(2))


# ============================================================
# TOPIC 3: DICTIONARY AND DICTIONARY METHODS
# ============================================================

def dictionary_examples():

    # A Dictionary is a mutable collection.
    # It stores data in key-value pairs.
    # It uses curly brackets {}.
    # Dictionary keys must be unique.

    dic = {
        "name": "tasir",
        "sub": ["science", "maths", "chemistry"],
        "score": 250,
        "cgpa": 3.33
    }

    print("Original Dictionary:", dic)
    print("CGPA:", dic["cgpa"])

    # Updating an existing value
    dic["cgpa"] = 3.9
    print("Updated CGPA:", dic["cgpa"])

    # Another Dictionary example
    student = {
        "name": "tasir",
        "sub": ["computer", "math", "networking"],
        "score": 9,
        "hobbies": ("cricket", 2020)
    }

    student["score"] = 12

    # ---------------- DICTIONARY METHODS ----------------

    # 1. keys()
    # Returns all keys of the Dictionary.
    print("\nDictionary Keys:", student.keys())

    # 2. values()
    # Returns all values of the Dictionary.
    print("Dictionary Values:", student.values())

    # 3. items()
    # Returns key-value pairs.
    print("Dictionary Items:", student.items())

    # 4. get()
    # Returns the value of a specified key.
    # If the key does not exist, it returns None
    # or the default value provided.
    print("Student Name:", student.get("name"))
    print("City:", student.get("city", "Not available"))

    # 5. update()
    # Adds new key-value pairs or updates existing ones.
    student.update({"city": "Peshawar"})

    print("\nAfter updating Dictionary:")
    print(student.items())


# ============================================================
# TOPIC 4: SET AND SET METHODS
# ============================================================

def set_examples():

    # A Set is a mutable and unordered collection.
    # It stores only unique values (no duplicates).
    # It uses curly brackets {}.
    # An empty Set is created using set(), not {}.

    set_data = {1, 2, 3, 4, 5, 5, 2, 1, 10, 8}

    print("Original Set:", set_data)
    print("Data Type:", type(set_data))

    # Duplicate values are automatically removed.

    # ---------------- SET METHODS ----------------

    a = {1, 2, 3, 3}

    print("\nOriginal Set:", a)

    # 1. add()
    # Adds a new element to the Set.
    a.add(4)
    print("After add:", a)

    # 2. remove()
    # Removes a specified element.
    # Raises KeyError if the element does not exist.
    a.remove(4)
    print("After remove:", a)

    # 3. clear()
    # Removes all elements from the Set.
    a.clear()
    print("After clear:", a)

    # ---------------- SET OPERATIONS ----------------

    a = {1, 2, 3, 4, 5}
    b = {4, 5, 8, 9}

    # 4. union()
    # Returns all unique elements from both Sets.
    print("\nUnion:", a.union(b))

    # 5. intersection()
    # Returns only the common elements.
    print("Intersection:", a.intersection(b))


# ============================================================
# TOPIC 5: PROBLEM 1 - FIND UNIQUE COURSES
# ============================================================

def problem_1():

    # We want to find all unique courses.
    # A Set is useful because it automatically removes duplicates.

    set_course = set()

    for name, course in info:
        set_course.add(course)

    print("Unique Courses:", set_course)


# ============================================================
# TOPIC 6: PROBLEM 2 - FIND STUDENTS TAKING ENGLISH
# ============================================================

def problem_2():

    # We want to find students whose course is English.
    # We use a for loop to check every record.
    # An if condition checks whether the course is English.

    for name, course in info:

        if course == "english":
            print(name, course)


# ============================================================
# TOPIC 7: PROBLEM 3 - GROUP COURSES BY STUDENT
# ============================================================

def problem_3():

    # We want to create a Dictionary where:
    # Key = Student name
    # Value = Set of courses taken by that student.
    #
    # We use a Set for courses because a student
    # should not have duplicate courses.

    dic = {}

    for name, course in info:

        # If the student does not exist in the Dictionary,
        # create a new key with an empty Set as its value.

        if dic.get(name) is None:
            dic.update({name: set()})

        # Add the course to that student's Set.
        dic[name].add(course)

    print("Courses grouped by students:")

    for name, courses in dic.items():
        print(name, ":", courses)


# ============================================================
# MAIN FUNCTION - MENU SYSTEM
# ============================================================

def main():

    while True:

        print("\n========== PYTHON BASICS: DAY 04 ==========")

        print("1. List and List Methods")
        print("2. Tuple and Tuple Methods")
        print("3. Dictionary and Dictionary Methods")
        print("4. Set and Set Methods")
        print("5. Problem 1 - Find Unique Courses")
        print("6. Problem 2 - Find English Students")
        print("7. Problem 3 - Group Courses by Student")
        print("0. Exit")

        choose = input("\nChoose an example (0-7): ").strip()

        if choose == "1":
            list_examples()

        elif choose == "2":
            tuple_examples()

        elif choose == "3":
            dictionary_examples()

        elif choose == "4":
            set_examples()

        elif choose == "5":
            problem_1()

        elif choose == "6":
            problem_2()

        elif choose == "7":
            problem_3()

        elif choose == "0":
            print("Goodbye! Keep practicing Python.")
            break

        else:
            print("Invalid choice. Please enter 0-7.")


# ============================================================
# PROGRAM EXECUTION
# ============================================================

if __name__ == "__main__":
    main()
