# TOPIC 3: OPERATION ON FILES WRITE() AND READ() >>>>>>>>>>>>>>>

import os
import json

# 7 if you want to delete file then use this one

# os.remove('sample_day06_2.txt')

#######################################################
# TOPIC 3: OPERATION ON FILES WRITE() AND READ() >>>>>>>>>>>>>>>

# 8 if you want to open file  and not close menually

#  then use this one it will automatically read & then close .mean not need to write close()

# with open('sample_day06.txt') as f:

#     print(f.read())

##########################################################
# TOPIC 4: OPERATION ON FILES WRITE() AND READ() PROBLEM 1 >>>>>>>>>>>>>>>

# z=1
# x=True
# with open('sample_day06_2.txt','r') as f:
#     while x:
#         x = f.readline()
#         if 'python' in x:
#             print(f'found {x} at line no {z}')
#             break
#         print(x)
#         z+=1

##################################################################################
# TOPIC 5: EXCEPTION HANDLING (TRY,EXCEPT,ELSE,FINALLY) >>>>>>>>>>>>>>>

# # we actually want to handle error

# try: # here we define my logic
#     user_input=int(input('enter a number'))
#     ans=10/user_input

# except ZeroDivisionError: # this is a building error exception in python.in block if any error then block will be run
#     print('divide by 0 is not allowed')

# except ValueError: # this is also building error exception in python.it will run if put invalid value
#     print('Invalid Input')

# else: # this is a block when logic fine .no error then this block will be run
#     print(f'ans={ans}')

# finally: # this block run in both cases even if error occur or no error accur so this block must in both case
#     print('End of Program')

##################################################################################
# TOPIC 6: WORKING WITH JSON MODULE   >>>>>>>>>>>>>>>

# 1 when you have a string data in form of object & want to convert it in object dictionary use this one

# python_str='{"name":"anwar","age":20,"isTeacher":true}'
# print(type(python_str))

# python_obj=json.loads(python_str)
# print(type(python_obj))

###################################################################################

# 2 when you have a dictionary data  & want to convert it in string use this one

# data={
#     "name":"ali",
#     "fname":"khan",
#     "age":20,
#     "teacher":None
# }
# print(type(data))

# py_dic=json.dumps(data)
# print(type(py_dic))


###################################################################################

# 3 when you have a dictionary data in other json file & you want to import it  use this one


# with open('test_day06.json','r') as f:
#     data=json.load(f)
#     print(type(data))

###################################################################################

# 4 when you have a dictionary data here in this file & want 
#   to override this data in with other json file data  use this one


# g={"name":"jonas","age":60,"isTeacher":False}

# with open('test_day06.json','w') as f:
#     data=json.dump(g,f , indent=4)
#     print('Done')