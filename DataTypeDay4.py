# 4 fundimental and building data type in python "1 LIST,2 TUPLE,3 DICTIONARY,4 SETS"



# LIST =       mutable   []
# TUPLE =      immutable ()
# DICTIONARY = mutable   {}
# SETS      =  immutable {}




# 1 LIST
# LIST is a sequance of values with square bracket [] , and also it is mutable ,mean we can change its value
# while string is a immutable value mean we cannot change its value 

# marks=[1,2,3,4,5,'tasir']
#print(marks)
# print(type(marks))
# # print(marks[2])
# marks[3]=10
# # print(marks[3])
# for x in marks:
#     print(x)

# 2  LIST METHOD 
#append method used to add a value at the end of the list
# val=[1,3,5,6,7]
# print(val) # before adding value output

# val.append(10)
# print(val) # after adding value output

# #insert method used to add a value at the based of index in the list
# val.insert(1,60) # 1 is index and 600 is a value
# print(val)

# # sort method used to sort a value in the list
# val.sort()
# print(val)

# # reverse method used to sort a value in reverse in the list
# val.reverse()
# print(val)

# for x in val:
#     if(x==10):
#         print(x)
#         break


# 2 TUPLE:

# TUPLE is a sequance of values with PARENTHSIS() , and also it is immutable ,mean we cannot change its value
# while string is also immutable value mean we cannot change its value as well
# and also if we write a=(1) and check the data type then it will consider int datatype not tuple
# while if we write like this a=(1,)then it will consider a tuple

# tup=(1,2,3,4,5,'abc')
# print(tup)
# print(type(tup))

# a=(1,)
# print(type(a))

# 2 TUPLE METHOD
# b=(1,2,3,2,5)
# print(b.index(5)) # it actually show you which value hold on which index like you put 5 and output 4 ,mean 5 exest on 4 index

# b=(1,2,3,2,5,2)
# print(b.count(2)) # count show you which value how much repeated inside the tuple

# 3 DICTIONARY:
# KEY VALUE PAIR and also it is mutable datatype
# dic={
#     "name":"tasir",
#     "sub":["science,maths ,chemistry"],
#     "score":250,
#     "cgpa":3.33
# }
# # print(type(dic))
# print(dic["cgpa"])
# # after update the key then the result of 
# dic["cgpa"]=3.9
# print(dic["cgpa"])

# 2 METHOD OF DICTIONARY AS well but search in chatgpt but some is "dic.key(),dic.values(),dic.items(),dic.get(val),dic.update(new item)" 
# dic={
#     'name':'tasir',
#     'sub':['computer','math','networking'],
#     'score':9,
#     'hobies':('cricket',2020)
# }
# dic["score"]=12
# print(dic.keys())
# print(dic.values())
# print(dic.items())
# dic.update({'city':'peshawar'})
# print('after update the values are now you can see below')
# print(dic.items())

# 4 sets curly bracket{}
# collection of unique elements .and it is immutable datatype 

# set={1,2,3,4,5,5,2,1,10,8} #it not dublicate the value it just set the single value and unique
# # print(type(set))
# print(set)

# 2 SETS METHOD
 
# a={1,2,3,3}
# print(a)

# a.add(4)
# print(a)

# a.remove(4)
# print(a)

# a.clear()
# print(a)

# a={1,2,3,4,5}
# b={4,5,8,9}
# print(a.union(b))

# print(a.intersection(b))

######################################### PROBLEM 1
# info=[("alice","math"),
#       ("bob","science"),
#       ("alice","science"),
#       ("charlie","math"),
#       ("bob","math"),
#       ("alice","english"),
#       ("charlie","english")
# ]
# set_course=set() # it is a empty set

# for name,course in info:
#       set_course.add(course)
      
      
# print(set_course)
# ####################################PROBLEM 2
# for name,course in info:
#       if course=="english":
#             print(name,course)
# ###########################################PROBLEM 3
# dic={}
# for name,course in info:
#       if dic.get(name)==None:
#             dic.update({name:set()})
#             dic[name].add(course)
#       else:
#             dic[name].add(course)

# print(dic)
            