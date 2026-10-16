# TO CHECK ODD OR EVEN NUMBER 

# input_number=int(input('Enter a number to check were is ODD or EVEN'))
# if input_number%2==0:
#     print('even number')
# else:
#     print('odd number')

# NESTING IF ELSE

# user_Name=input('Enter a User name')
# user_Password=input('Enter a User password')

# if user_Name == "admin" and user_Password == "pass":
#     print("you are succesfully login")
# else:
#     if user_Name=="admin" and user_Password != "pass":
#         print('your password is wrong')
#     else:
#         if user_Password == "pass" and user_Name != "admin":
#             print('your user name is wrong')
#         else:
#             print('you enter wrong usename and password ')

# MATCH CASE

# color=input('enter a color value')
# match color:
#     case 'Green':
#         print('GO')
#     case 'Red':
#         print('STOP')
#     case 'Yellow':
#         print('LOOK')
#     case _:
#         print('Wrong color')

# WHILE LOOP
# count=1
# while count<=5:
#     print('hellow',count)
#     count+=1
# print('HI Tasir ypu out from loop')

# i=5
# while i>=1:
#     print(i)
#     i-=1
# print('HI Tasir ypu out from loop')

# print a Multiplication Table

# number=int(input('Enter any number for table multiplication  '))
# j=1
# while j<=10:
#     print(j*number)
#     j+=1

# BREAK and continue KEYWORD IN LOOP////////////////////////////////

# i=1
# while i<=5:
#     print(i)
#     if(i==3):
#         break
#     i+=1 # updation step

# k=0
# while k<=10:
#     k+=1
#     if(k%3==0):
#         continue
#     print(k)

# FOR LOOP       //////////////////////////////////////////////////////

# string='HELLOW'
# for var in string:
#     print(var)

# string='INTERNSHIP'
# if('E' in string):
#     print('YES E is exest in the string')

# string='INTERNSHIP'
# for i in range(5):
#     print(i)

# word='artificial intelligence'
# ans=0
# for str in word:
#     if(str=='i'):
#         ans+=1
#         print(ans,'=>',str)

#/////////////////////////////////////////////////////////////////////

# 9 RANGE

#  range(1,10) here 1 is start value and 10 stop value
# for a in range(1,10):
#     print(a) 

##### 

#   #     1 is start value and 10 is stop value while 2 is step mean it will increase 2 time a value 
# for b in range(1,10,2):
#     print(b) 

# ////////////////////////////////////////////////////////////////////////

# FUNCTION

# def hellow():# fntn definition
#     print('tasirkhan')
# hellow() #fntn calling

# def hellow(a,b): # (a,b) funx parameter
#     sum=a+b
#     return sum

# print(hellow(2,5)) # (2,5) passing arguments
# /////////
# # 2 LAMBDA FUNCTION
# sum=lambda a,b:a+b
# print(sum(2,3))
# 1*2*3*4*5=120
def calFactorial(n):
    fact=1
    for i in range(1,n+1):
        fact *=i
    return fact

n=int(input('enter a number'))
print(calFactorial(n))