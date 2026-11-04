
# ==========================================================
# TOPIC 1: FILE OPERATIONS — OPEN(), READ(), READLINE(), CLOSE()
# ==========================================================

f = open('sample_day06.txt', 'r')  # r means read mode

data = f.readline()  # readline() reads one line at a time

f = open('sample_day06.txt', 'r')

data = f.read()  # read() reads all remaining content

print(data)

f.close()  # Close the file after performing the operation


# ==========================================================
# TOPIC 2: FILE OPERATION — WRITE()
# ==========================================================

# 1. WRITE MODE ('w')
# It overwrites the complete old content.
# If the file does not exist, Python creates it.

# f = open('sample_day06.txt', 'w')
# f.write('Text to overwrite the complete data')
# f.close()


# ==========================================================
# TOPIC 3: FILE OPERATIONS — APPEND ('a')
# ==========================================================

# 2. APPEND MODE ('a')
# It writes new text at the end of the existing content.

# f = open('sample_day06.txt', 'a')
# data = f.write('\nI want to test just\nIs it working or not?')
# print(data)  # Returns the number of characters written
# f.close()


# ==========================================================
# TOPIC 4: WRITE AND READ MODE ('w+')
# ==========================================================

# 3. w+ means write and read.
# It deletes the old content when the file is opened.
# Then it allows writing and reading.

# f = open('sample_day06.txt', 'w+')
# data = f.write('I want to test just\nIs it working or not?')
# f.seek(0)  # Move the cursor to the beginning
# print(f.read())
# f.close()


# ==========================================================
# TOPIC 5: READ AND WRITE MODE ('r+')
# ==========================================================

# 4. r+ means read and write.
# It does not delete the old content.
# The file must already exist.

# f = open('sample_day06.txt', 'r+')
# data = f.write('123')
# print(f.read())
# f.close()


# ==========================================================
# TOPIC 6: APPEND AND READ MODE ('a+')
# ==========================================================

# 5. a+ means append and read.
# It writes new content at the end of the file.
# It also allows reading.

# f = open('sample_day06.txt', 'a+')
# data = f.write('123')
# f.seek(0)  # Move the cursor to the beginning for reading
# print(f.read())
# f.close()


# ==========================================================
# TOPIC 7: CREATE AND WRITE IN ANOTHER FILE ('w+')
# ==========================================================

# 6. Open another file using w+.
# If the file does not exist, Python creates it.

# f = open('sample_day06_2.txt', 'w+')
# data = f.write('1234567')
# f.seek(0)
# print(f.read())
# f.close()