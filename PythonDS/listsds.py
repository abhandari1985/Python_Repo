# # # https://docs.python.org/3/tutorial/introduction.html#lists #
# # # Lets build an application that records customer details and assign it unique userid generated randomly #
# # # name=input("Enter username: ")
# # # number=input("What is your number: ")
# # # print(name,number)

# # # Generating random number
# # # name = input("Enter username: ")
# # # number = input("What is your phone number: ")
# # # from random import seed
# # start = int(input("Enter starting range of list: "))
# # end = int(input("Enter ending range of list: "))
# # from random import randint

# # value = randint(start, end)
# # print(value)

# # from random import randint

# # value = randint(100, 999)
# # # print(name, number, value)

# # # Lists are ordered sequence of mix data types, written as comma separated elements within square brackets
# # # List1 = [name, number, value]
# # # print(List1)

# # # Introduction
# # L = ["India", 23, 6, "Mumbai"]
# # # Nested List
# # L1 = ["Chemistry", "Biology", [1994, 2004], 4]
# # # Indexing
# # print(L1[1])
# # # Indexing for Nested list
# # print(L1[2][1])
# # # negative Indexing for Nested list
# # print(L1[-2][1])
# # # Slicing - get a subset from the defined list
# # print(L1[0:2])
# # print(L1[-3:-1])
# # # Membership in lists
# # L2 = [1, 2, 3, 4, 5]
# # print(1 in L2)
# # print(20 in L2)
# # # List concatenation
# # new_L = L2 + [100, 200]
# # print(new_L)
# # # List are mutable, we can replace content at a given index
# # L1[1] = "Physics"
# # print(L1)
# # # Extend the existing list. Added elements are added to new indexes
# # L1.extend([100, 99])
# # print(L1)
# # # Append the existing list. All Added elements are added only to the next available index
# # L1.append([49, 50])
# # print(L1)
# # L1.append([80])
# # print(L1)
# # # Delete command in list
# # del L1[0:2]
# # print(L1)
# # # pop command in list. Ipop(index): Remove and return the item at index (default last)
# # L3 = ["anand", "singh", "bhandari", "121126"]
# # print(L3)
# # L3.pop()
# # print(L3)
# # # remove command in list. remove(value): Remove the first occurrence of a value in the list
# # L3.remove("singh")
# # print(L3)
# # # sort function
# # L4 = [12, 45, 5, 90]
# # L4.sort()
# # print(L4)
# # L4.sort(reverse=True)
# # print(L4)
# # # sorted functions. sorted(): Assign the sorted elements to a new list and the original list is left as is.
# # L = ["one", "two", "three", "four", "five", "six"]
# # print(sorted(L))
# # print(L)

# # # word = ["1", "2", "3", "4"]
# # # word[:] = []
# # # print(word)

# # # shallow Copying
# # A = ["apple", "mango", "guava"]
# # B = A
# # print(A, B)
# # A[0] = "strawberry"
# # print(A, B)
# # # shallow copying. If we need to make copy of a list but changing element on one should not change on the other
# # A = ["apple", "mango", "guava"]
# # B = A[:]
# # print(B, A)
# # A[0] = "pineapple"
# # print(A, B)


# # L1 = ["8", "5.66", "6.5", "10", "10"]
# # L2 = ["7", " 10", "6", "7", "9"]
# # L3 = []

# # avgL1 = 0
# # avgL2 = 0
# # for i in range(5):
# #     L3.append((float(L1[i]) * 10 + float(L2[i])) / 11)
# # count = 0
# # for j in range(5):
# #     if float(L3[j]) >= float(L1[j]):
# #         count = count + 1
# # print(count)
# # print(L1)
# # print(L2)
# # print(L3)

# # if count > 2:
# #     print("Selected")
# # else:
# #     print("Rejected")

# L1 = ["automobiles", "Honda", "Benz", "Suzuki", "Morris Garages"]
# L2 = []
# for string in L1:
#     L2.append(len(string))
# print(L2)

# # Using Comprehensions
# L3 = [len(string) for string in L1]
# print(L3)

# # iterating over L1 and L2 simultaneously
# for i, j in zip(L1, L2):
#     print(i, " - ", j)

# # Dictionary Comprehension
# # create a dictionary consisting of element and length for elements in List L1
# L4 = {word: len(word) for word in L1}
# print(L4)

# # write a program which takes a word as an input and returns vowels from the word
# input_str = input("Enter String with vowels")
# vow = ""
# for char in input_str:
#     if char in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
#         vow = vow + char
# print(vow)

# # comprehension for set
# vowels = {char for char in input_str if char in "aeiouAEIOU"}
# print(vowels)

# n = int(input())
# L5 = []
# for i in range(1, n + 1):
#     L5.append(i * i)
# print(L5)
# L6 = [i * i for i in range(1, n + 1)]
# print(L6)

# input_list = ["wood", "old", "apple", "big", "item", "euphoria"]
# list_vowel1 = []
# for word in input_list:
#     if word[0] in ("aeiouAEIOU"):
#         list_vowel1.append(word)
# print(list_vowel1)

# list_vowel = [word for word in input_list if word[0] in ("aeiouAEIOU")]
# print(list_vowel)

# input_list = list(range(1, 100))
# output_dict = {val: val**3 for val in input_list if val % 3 == 0}
# print(output_dict)
# print([i + j for i in "abc" for j in "def"])
d = {x.upper(): x * 3 for x in "acbd"}
print(d)
