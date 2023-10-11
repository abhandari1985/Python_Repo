# String operations
# string can be declared with single or double codes.

# indexing can also be in reverse. Negative indexing - for last element indexing will be -1

# strings are immutable you cannot change characters of a string - So, to update assign new string to the same variable
# name='vishwajeet singh'
# name[5]='v'
# print(name)

# string concatenation
# type casting using str() function
import random

age = 30
print("I am " + str(age) + " years old.")
# slicing - by specifying start and end index >> string[start:end:step]
statement = "I love Python programming"
print(statement[7:13])
print(statement[-18:-12])
print(statement[:20])
print(statement[20:])
# Membership - To check if a particular string or set of characters are present in the string
print("data" in statement)
print("scientist" not in statement)
# Repetition of string using *
print(statement * 5)
# String methods
print(statement.upper())
print(statement.lower())
print(statement.rstrip())
# rstrips end with white spaces from the string
print(statement.rstrip("."))
# rstrips end with . from the string
print(statement.lstrip())
# rstrips white spaces from the beginning of the string
print(statement.strip())
# rstrips white spaces from the beginning and end of the string
# Chaining
text = "############Employer Name is MS. What is employee name?!!!!!!!!!!"
print(text.lstrip("#").rstrip("!"))
x = "len"
print(x[len(x * 2) - 5])
# count method - to get the count of number of times a sequence is present in the string
print(text.count("e"))
print(text.count("e", 30))
# placing integer in a string. format method takes care of type conversion
print("I am {0} years old".format(age))
# dynamic string formatting
A = "data"
B = "analysis"
C = "panda"
print("{0} {1} using {2}".format(A, B, C))
print(f"{A} {B}{C}")
# to get help related to any string method
# help(str)

print(random.randrange(0, 181, 2))

random_list = []
# Set a length of the list to 10
for i in range(0, 30):
    # any random numbers from 0 to 1000
    random_list.append(random.randint(25, 30))
print(random_list)

# Capitalize
# Title
# Strings are immutable in nature. Content cannot be changed
# But we can use replace to update the string
# use id function to get the memory address. Python garbage collector will clean unused memory stores time to time


# 8 to 8.5 >> 20-50         |   35-40 | 30-35   | 45-50
# 8.5 to 9 >> 50-150        |   30-35 | 25-30   | 40-45
# 9 to 9.5 >> 150-260       |   25-30 | 20-25   | 35-40
# 9.5 to 10 >> 250-350      |   20-25 | 15-20   | 35-40
# 10 to 10.5 >> 275-360     |   10-20 | 5-15    | 30-35
# 10.5 to 11.0 >> 200-250   |   25-30 | 20-25   | 25-30
