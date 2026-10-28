# TOPIC 1: Class and Object>>>>>>>>>>>>>>>

# class Student: # creating a class named student
#     subject="python"
#     college="abc"
#     year=4

# st1=Student() # creating an object of class student
# print(st1.subject,st1.college,st1.year)

##############

# class Student:
#     def __init__(self,name,cgpa): #__init__ it is a constructor and it is used to initialize the object and it is called automatically when we create an object of the class and it is used to assign the value to the variable name and cgpa
#         self.name=name
#         self.cgpa=cgpa

# stu1=Student("TASIR",3.33) #this object is created by using the constructor and we can pass the value in the constructor and it will assign to the variable name and cgpa
# print(f'name of the student is: {stu1.name} \n and cgpa of the student is: {stu1.cgpa}')
# stu2=Student("ALI",4.0)
# print(f'name of the student is: {stu2.name} \n and cgpa of the student is: {stu2.cgpa}')

##############

# class Student:
#     subject='python'
#     cgpa=3.33
#     college='abc'

# st1=Student()
# for studen in range(1,10):
#     print(st1.subject,st1.college,st1.cgpa)

###########################################################

# TOPIC 2: Constructor>>>>>>>>>>>>>>>>>>>>>>>>>>
# class Student:
#     def __init__(self,name,subject,cgpa,university):# this constuctor function which automatically called for every obj
#         self.name=name
#         self.subject=subject
#         self.university=university
#         self.cgpa=cgpa

#     def get_cgpa(self):
#         return self.cgpa #this is another constructor fnc


# st1=Student('Yasir','python',3.33,'peshawar')

# # print(f'name of the student is {st1.name} and subject is {st1.subject} and also university {st1.university} and cgpa {st1.cgpa}')

# print(st1.get_cgpa())

#####################################################################

## TOPIC 3: Class and Instance Attributes>>>>>>>>>>>>>>>>>>>>>

 # class attributes are those who belong to class and also it is common for all object
 # instance attributes are those who belong to object and it can be change of different object
 # why we use class attributes? 
 # bcz we know that class can only one time acoupy space in the memory and it is common for all object
 # while objects acoupy multiple space for multiple objects 


# class Employee:
#     office='ABC' # class attributes

#     def __init__(self,name,salary):
#         self.name=name # instance attributes
#         self.salary=salary # instance attributes

# emp1=Employee('tasir',30000) # first obj

# print(f'name of employee is {emp1.name} and salary {emp1.salary}')

# # print(Employee.office) # we can excess class atribute in this way 
# # print(emp1.office) # we can excess class atribute also in this way both work

##########################################################

# TopiC 4: Instance, Class and Static Method>>>>>>>>>>>>>>>>>>>>>

# < 1 INSTANCE METHOD >

# in this method first is passed a 'self' parameter which is getInfo(self) & also access the class and instance attributes 
# but if you think that we also passed self to __init__ method then is also a instance method?
# no this a constructor method which is comporsary not a instance method 

# class Laptop:
#     storage_type='ssd'
#     def __init__(self,RAM,storage):
#         self.RAM=RAM
#         self.storage=storage
#     def getInfo(self):       #this a instance method
#         print(f'laptop has RAM => {self.RAM} and storage => {self.storage} and storageType is => {self.storage_type}')

# laptop1=Laptop('16gb','512gb')
# laptop2=Laptop('8gb','300gb')

# laptop1.getInfo()

#####################################################

# <  2 Class METHOD >

# in class method first we passed a 'cls'parameter
#  cls can be change like 'abc' but conventially we use cls
# and we can access only class attributes and cannot access instance attribut
# and we write on top of class method called '"decorator" "@classmethod"' it basically take a fcn
#  which is get_storage_type() and change it behavior 
# mean 'they convert to this fcn into a class fcn'
# and also they take only class method 


# class Laptop:
#     storage_type='ssd' #class Attribut
#     def __init__(self,RAM,storage):
#         self.RAM=RAM # instance Attribut
#         self.storage=storage
    
    
#     def getInfo(self):  #this a instance method
#         print(f'laptop has RAM => {self.RAM} and storage => {self.storage} and storageType is => {self.storage_type}')
    
    
#     @classmethod
#     def get_storage_type(cls):  #this a class method
#         print(f'storage type is => {cls.storage_type}')

# l1=Laptop('16gb','512gb')

# l1.get_storage_type()

###########################################################

# <  3 Static  METHOD > 

# in this method no comporsery parameter required like cls,self and we can create it normal fcn
# and they can not access class and instance attributes
# we use a speciall "decorator" called '@staticmethod'
# it is tightly couple with class


# class Laptop:
#     storage_type='ssd'
#     def __init__(self,RAM,storage):
#         self.RAM=RAM
#         self.storage=storage

#     def getInfo(self):    #this a instance method
#         print(f'laptop has RAM => {self.RAM} and storage => {self.storage} and storageType is => {self.storage_type}')
    
    
#     @classmethod
#     def get_storage_type(cls):   #this a class method
#         print(f'storage type is => {cls.storage_type}')

#     @staticmethod
#     def cal_discount(price,discount):   # this a static method 
#         final=price-(discount*price/100)
#         print(f'this a final discount {final}')

# l1=Laptop('16gb','512gb')

# l1.cal_discount(40_000,10)

###################################################################

# TOPIC 5: PROBLEM 1 >>>>>>>>>>>>>>>>>>>>>

# 1 DESIGN AND CREATE AN ONLINE STORE FOR PRODUCT (NAME,PRICE)
# 2 tract total product which been created (mean find how much product are created inside store like 1,2,3,etc)
# 3 create a static method to calculate discount on each product base on % a parameter 

# class Product:
#     count=0
#     def __init__(self,name,price): 
#         self.name=name
#         self.price=price
#         Product.count +=1

#     def get_info(self):     # instance method
#         print(f'Price of {self.name} is Rs {self.price} ')
    
#     @classmethod
#     def get_count_product(cls):  # class method
#             print(f'total product in store are {cls.count}')

#     @staticmethod
#     def cal_discount(price,discount):
#          result=price-(price*discount/100)
#          print(f'after discount final price is {result} ')

# p1=Product('laptop',50_000)
# p2=Product('phone',10_000)
# p3=Product('pen',100)

# p1.get_info()
# p2.get_info()
# p3.get_info()

# Product.get_count_product()
# p1.cal_discount(p1.price,15)