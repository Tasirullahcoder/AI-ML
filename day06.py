# TOPIC 1: OPERATION ON FILES  and method  READ(),OPEN(),CLOSE(), >>>>>>>>>>>>>>>

# f=open('sample_day06.txt','r') # r mean read file

# data=f.readline() # mean to read one line by line 

# data=f.read()       # mean read all lines

# print(data)

# f.close()        # after perform operation closed to it  must

######################################################################

# TOPIC 2: OPERATION ON FILES WRITE() >>>>>>>>>>>>>>>

# 1 if i want to overwrite the all text  then use this one 

# f=open('sample_day06.txt','w') # w mean write on file

# f.write('text to overrite \n the complete data')

# f.close()

######################################################

# TOPIC 3: OPERATION ON FILES WRITE() AND READ() >>>>>>>>>>>>>>>

# 2 if you want to write text at the end of old text then use this one

# f=open('sample_day06.txt','a')

# data=f.write('\n i want to test just \n is it work or not')

# print(data)

# f.close()

###############################################################
# TOPIC 3: OPERATION ON FILES WRITE() AND READ() >>>>>>>>>>>>>>>

# 3 if you want to write overrite  text then use this one

# f=open('sample_day06.txt','w+')

# data=f.write('\n i want to test just \n is it work or not')

# print(f.read())

# f.close()

##################################################################
# TOPIC 3: OPERATION ON FILES WRITE() AND READ() >>>>>>>>>>>>>>>

# 4 if you want to write text but this text will in start point are write

#  and also read old text then use this

# f=open('sample_day06.txt','r+')

# data=f.write('123')

# print(f.read())

# f.close()

##################################################################
# TOPIC 3: OPERATION ON FILES WRITE() AND READ() >>>>>>>>>>>>>>>

# 5 if you want to write text but this text will be in ending are write

# but this nothing will be read old text then use this

# f=open('sample_day06.txt','a+')

# data=f.write('123')

# print(f.read())

# f.close()

#############################################################################
# TOPIC 3: OPERATION ON FILES WRITE() AND READ() >>>>>>>>>>>>>>>

# 6 if you want to write text in other file then use this one

# f=open('sample_day06_2.txt','w+')

# data=f.write('1234567')

# print(f.read())

# f.close()
################################################################################