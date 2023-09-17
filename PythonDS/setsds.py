# Sets are unordered, don't maintain an order in which element are inserted.
# This makes sets unfit for indexing and slicing.
# What is their use then ? They can eliminate duplicates
# sets are enclosed with in curly brackets

# Here is an example where students are graded and we need to get distinct value from the grades.
# Set will remove all the duplicates
# Grades = [
#     "A",
#     "A",
#     "B",
#     "C",
#     "D",
#     "B",
#     "B",
#     "C",
#     "D",
#     "E",
#     "C",
#     "C",
#     "A",
#     "B",
#     "F",
#     "D",
#     "C",
#     "B",
#     "C",
#     "A",
#     "B",
#     "F",
#     "B",
#     "A",
#     "E",
#     "B",
#     "B",
#     "C",
#     "D",
# ]
# l = [1, 2, 3, 4, 5, 6, 7, 5, 6]
# m = set(Grades)
# print(m)

# print(type(l))
# print(type(m))
# print(len(m))

# a = {1, 2, 3, 4, 5}
# a.add("India")
# print(a)

# a.remove("India")
# print(a)

# # SET OPERATIONS
# A = {0, 2, 4, 6, 8}
# B = {1, 2, 3, 4, 5}
# print(A, B)
# print(A | B)  # Union - Syntax#1
# print(A.union(B))  # Union - Syntax#2
# print(A & B)  # Intersection - Syntax1
# print(A.intersection(B))  # Intersection - Syntax2
# print(A - B)  # Difference - Syntax1
# print(A.difference(B))  # Difference - Syntax2
# print(A ^ B)  # Symmetric difference - Will remove numbers in common and get remaing

# SETS Practice
C = [5, 5, 5, 5, 5, 5, 6, 3]
D = [3, 3, 5, 5, 1, 7, 2]
E = set(D) & set(C)
mylist = list(E)  # Convert set to list using list function
print(mylist)

nums = set([1, 1, 2, 3, 3, 3, 4])
print(nums)
print(len(nums))
