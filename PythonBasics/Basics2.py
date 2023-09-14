#String operations
#string can be declared with single or double codes. 

#indexing can also be in reverse. Negative indexing - for last element indexing will be -1

#strings are immutable you cannot change characters of a string - So, to update assign new string to the same variable
# name='vishwajeet singh'
# name[5]='v' 
# print(name)

#string concatenation
#type casting using str() function
age=30
print("I am "+str(age)+" years old.")
#slicing - by specifying start and end index >> string[start:end:step]
statement="I love Python programming"
print(statement[7:13])
print(statement[-18:-12])
print(statement[:20])
print(statement[20:])
#Membership - To check if a particular string or set of characters are present in the string
print("data" in statement)
print("scientist" not in statement)
#Repetition of string using * 
print(statement*5)
#String methods
print(statement.upper())
print(statement.lower())
print(statement.rstrip())
#rstrips end with white spaces from the string
print(statement.rstrip('.'))
#rstrips end with . from the string
print(statement.lstrip())
#rstrips white spaces from the beginning of the string
print(statement.strip())
#rstrips white spaces from the beginning and end of the string
#Chaining
text='############Employer Name is MS. What is employee name?!!!!!!!!!!'
print(text.lstrip('#').rstrip('!'))
x = 'len'
print(x[len(x*2)- 5])
#count method - to get the count of number of times a sequence is present in the string
print(text.count('e'))
print(text.count('e',30))
#placing integer in a string. format method takes care of type conversion
print("I am {0} years old".format(age))
#dynamic string formatting
A='data'
B='analysis'
C='panda'
print("{0} {1} using {2}".format(A,B,C))
#to get help related to any string method
help(str)