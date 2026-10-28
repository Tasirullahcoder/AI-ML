# TOPICS : 1:ENCAPSULATION 2:ABSTRACTION 3:INHERITANCE 4:POLYMORPHISM >>>>>>>>>>>>>>>

# TOPIC 1: ENCAPSULATION>>>>>>>>>>>>>>>

# wrapping data and function into single unit
# data hiding 
# we some types of attributes 
# 1 public that can access inside class and outside class & everywhere 
# 2 protected attribute that can access class + subclass
# 3 private attribute can access inside the class

# 1 protected & public attributes

# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name # public
#         self._balance=balance # protected => we use _balance which show protected 

# acc1=BankAccount('anwar',100_000)
# print(acc1.name,acc1._balance)  

###########################################################

# 2 private & public attributes

# to get or set the value of private attribute then use getter and setter function to acces val 

# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name # public
#         self.__balance=balance # private data mangling  we here __balance which show private

#     def get(self): # getter
#         # print(f'value of private attribute is {self.__balance}')
#         return self.__balance

#     def set(self,new_balance): #setter
#         self.__balance=new_balance

# acc1=BankAccount('anwar',100_000)

# acc1.set(200_000) # setter update the balance and then print final balance

# print(acc1.name,acc1.get())  
############################################################################

# TOPIC 2: INHERITANCE>>>>>>>>>>>>>>>

# reusing attributes and method from a parent (base) class

# class Employee: # parent class
#     startTime='10am'
#     endTime='6pm'
#     def change_time(self,new_time):
#         self.startTime=new_time

# class Teacher(Employee): # child class which inherites from employee
#     def __init__(self,subject):
#         self.subject=subject

# t1=Teacher('math')

# t1.change_time('9am')

# print(t1.subject,t1.startTime,t1.endTime)

############################################################################

# TOPIC 2: INHERITANCE TYPES >>>>>>>>>>>>>>>

# 1 we have single level inheritance which we define in above
# 2 multi level inheritance
# 3 multi inheritance

###################### 2 Multi Level Inheritance Below #########################

# class Employee: # parent class
#     startTime='10am'
#     endTime='6pm'

# class AdminStaff(Employee): 
#     def __init__(self,role):
#         self.role=role


# class Accountant(AdminStaff): 
#     def __init__(self,salary,role):
#         super().__init__(role) # with this i am calling  'adminstaff role' not a simple 
#         self.salary=salary

# acc1=Accountant(15_000,'CA')

# print(acc1.role,acc1.salary,acc1.startTime,acc1.endTime)


###################### 3 Multi Inheritance Below #########################

# class Teacher: 
#     def __init__(self,salary):
#             self.salary=salary

# class Student(): 
#     def __init__(self,gpa):
#         self.gpa=gpa


# class TA(Teacher,Student): 
#     def __init__(self,name,salary,gpa,):
#         super().__init__(salary)  
#         Student.__init__(self,gpa)
#         self.name=name

# Ta1=TA('khan',20_000,3.7)

# print(Ta1.name,Ta1.salary,Ta1.gpa)

#########################################################################

# TOPIC 3: ABSTRACTION >>>>>>>>>>>>>>>

# # Hiding internal detail and showing essencial features
# # abstract class is bluprint for other clases

# from abc import ABC ,abstractmethod
# class Animal :
#     @abstractmethod
#     def make_sound(self): # here we just initiolize fnc and define it in below.it is a bluprent
#         pass              # pass mean initilize the fnc but empty currently

# class Lion(Animal):
#     def make_sound(self):
#         print('Roar')


# class Cow(Animal):
#     def make_sound(self):
#         print('Moa')


# lion=Lion()
# cow=Cow()

# lion.make_sound()
# cow.make_sound()
#################################################################################

# TOPIC 4: POLYMORPHISM >>>>>>>>>>>>>>>

# POLY 'many' MORPHISM 'form' => mean multiple function but same name
# example operator overloading
#  like " + "" it can be add two number and can also to cancatinate two string

# print(1+2,'hellow'+'word')
#####################################################

# TOPIC 4: TWO TYPES FUNCTION OVERRIDING & DUCK TYPING  >>>>>>>>>>>>>>>

# # 1 FUNCTION OVERRIDING (inheritance) redefining parent class fnc in child class fnc below given eg

# class Employee:
#     def get_designation(self):
#         print('designation = employee')

# class Teacher(Employee) :
#     def get_designation(self):
#             print('designation = teacher')

# t1=Teacher()
# t1.get_designation()

# 2 DUCK TYPING ##################################

# # example of it .walk like a duck and quake like a duck .so both work
# #  like same so we can give function name same bcz work both same 


# class Teacher:
#     def get_designation(self):
#             print('designation = teacher')

# class Accountant:
#     def get_designation(self):
#         print('designation = accountant')


# t1=Teacher()
# acc1=Accountant()

# t1.get_designation()
# acc1.get_designation()
