# https://docs.python.org/3/tutorial/introduction.html#lists #
# Lets build an application that records customer details and assign it unique userid generated randomly #
# name=input("Enter username: ")
# number=input("What is your number: ")
# print(name,number)

# Generating random number
# name = input("Enter username: ")
# number = input("What is your phone number: ")
# from random import seed
from random import randint

value = randint(100, 999)
# print(name, number, value)

# Lists are ordered sequence of mix data types, written as comma separated elements within square brackets
# List1 = [name, number, value]
# print(List1)

# Introduction
L = ["India", 23, 6, "Mumbai"]
# Nested List
L1 = ["Chemistry", "Biology", [1994, 2004], 4]
# Indexing
print(L1[1])
# Indexing for Nested list
print(L1[2][1])
# negative Indexing for Nested list
print(L1[-2][1])
# Slicing - get a subset from the defined list
print(L1[0:2])
print(L1[-3:-1])
# Membership in lists
L2 = [1, 2, 3, 4, 5]
print(1 in L2)
print(20 in L2)
# List concatenation
new_L = L2 + [100, 200]
print(new_L)
# List are mutable, we can replace content at a given index
L1[1] = "Physics"
print(L1)
# Extend the existing list. Added elements are added to new indexes
L1.extend([100, 99])
print(L1)
# Append the existing list. All Added elements are added only to the next available index
L1.append([49, 50])
print(L1)
L1.append([80])
print(L1)
# Delete command in list
del L1[0:2]
print(L1)
# pop command in list. Ipop(index): Remove and return the item at index (default last)
L3 = ["anand", "singh", "bhandari", "121126"]
print(L3)
L3.pop()
print(L3)
# remove command in list. remove(value): Remove the first occurrence of a value in the list
L3.remove("singh")
print(L3)
# sort function
L4 = [12, 45, 5, 90]
L4.sort()
print(L4)
L4.sort(reverse=True)
print(L4)
# sorted functions. sorted(): Assign the sorted elements to a new list and the original list is left as is.
L = ["one", "two", "three", "four", "five", "six"]
print(sorted(L))
print(L)

# word = ["1", "2", "3", "4"]
# word[:] = []
# print(word)

# Shadow Copying
A = ["apple", "mango", "guava"]
B = A
print(A, B)
A[0] = "strawberry"
print(A, B)
# shadow copying. If we need to make copy of a list but changing element on one should not change on the other
A = ["apple", "mango", "guava"]
B = A[:]
print(B, A)
A[0] = "pineapple"
print(A, B)
