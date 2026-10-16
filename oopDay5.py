# what is aggrigation pipeline? and how they work? and why we use it ? can we work without it ?.understand me on aggegation pipeline deeply step by step

 #HOOP

# class Student: # creating a class named student
#     subject="python"
#     college="abc"
#     year=4

# st1=Student() # creating an object of class student
# print(st1.subject,st1.college,st1.year)

###################

# class Student:
#     def __init__(self,name,cgpa): #__init__ it is a constructor and it is used to initialize the object and it is called automatically when we create an object of the class and it is used to assign the value to the variable name and cgpa
#         self.name=name
#         self.cgpa=cgpa

# stu1=Student("TASIR",3.33) #this object is created by using the constructor and we can pass the value in the constructor and it will assign to the variable name and cgpa
# print(f'name of the student is: {stu1.name} \n and cgpa of the student is: {stu1.cgpa}')
# stu2=Student("ALI",4.0)
# print(f'name of the student is: {stu2.name} \n and cgpa of the student is: {stu2.cgpa}')
########################################################
# class Student:
#     subject='python'
#     cgpa=3.33
#     college='abc'

# st1=Student()
# for studen in range(1,10):
#     print(st1.subject,st1.college,st1.cgpa)
###########################################################
# class Student:
#     def __init__(self,name,subject,cgpa,university):# this constuctor function which automatically called for every obj
#         self.name=name
#         self.subject=subject
#         self.university=university
#         self.cgpa=cgpa

#     def get_cgpa(self):
#         return self.cgpa #this is another constructor fnc


# st1=Student('tasir','python',3.33,'agriculture')
# st2=Student('anwar','cybersecurity',3.5,'UET')


# # print(f'name of the student is {st1.name} and subject is {st1.subject} and also university {st1.university} and cgpa {st1.cgpa}')
# # print(f'name of the student is {st2.name} and subject is {st2.subject} and also university {st2.university} and cgpa {st2.cgpa}')

# print(st1.get_cgpa())# to called second constructor which getcgpa
# print(st2.get_cgpa())# to called second constructorwhich getcgpa
#####################################################################

## types of attributes
 # class attributes are those who belong to class and also it is common for all object
 # instance attributes are those who belong to object and it can be change of different object
 # why we use class attributes? 
 # bcz we know that class can only one time acoupy space in the memory and it is common for all object
 # while objects acoupy multiple space for multiple objects 
  
class Employee:
    office='ABC' # class attributes

    def __init__(self,name,salary):
        self.name=name # instance attributes
        self.salary=salary # instance attributes

emp1=Employee('tasir',30000) # first obj
emp2=Employee('anwar',20000) #second obj
print(f'name of employee is {emp1.name} and salary {emp1.salary}')
print(f'name of employee is {emp2.name} and salary {emp2.salary}')
# print(Employee.office) # we can excess class atribute in this way 
# print(emp1.office) # we can excess class atribute also in this way both work