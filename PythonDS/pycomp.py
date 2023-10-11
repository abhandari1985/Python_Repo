# # # # # # Python comprehensions >> more pythonic way to write codes
# # # # # # Query >> From a list create another list having length of each word from existing list

# # # # # l1 = ["automobiles", "honda", "maruti", "suzuki", "hyundai"]
# # # # # l2 = []
# # # # # l3 = []
# # # # # for word in l1:
# # # # #     l2.append(len(word))
# # # # # print(l2)

# # # # # l3 = [len(word) for word in l1]
# # # # # print(l3)

# # # # # # iterating over 2 lists simultaneously

# # # # # for i, j in zip(l1, l3):
# # # # #     print(i, "-", j)

# # # # # # Example in Dictionary comprehension
# # # # # # Create a dictionary consisting of element and length of each element from above list
# # # # # d = {word: len(word) for word in l1}
# # # # # print(d)
# # # # # # Using list comprehensions is much more concise and elegant than explicit for loops.
# # # # # # An example of creating a list using a loop is as follows:

# # # # # L1 = [10, 20, 30, 24, 18]
# # # # # L2 = [8, 14, 15, 20, 10]
# # # # # L4 = []
# # # # # for i in range(len(L1)):
# # # # #     L4.append(L1[i] - L2[i])
# # # # # print(L4)

# # # # # # You know this code from our earlier discussions. The same code using a list comprehension is as follows:
# # # # # # using list comprehension
# # # # # L1 = [10, 20, 30, 24, 18]
# # # # # L2 = [8, 14, 15, 20, 10]
# # # # # L5 = [L1[i] - L2[i] for i in range(0, len(L1))]
# # # # # print(L5)


# # # # # # Write a program that takes word from the user and returns vowels from the word
# # # # # inputword = input("Enter a word ")
# # # # # vowels = set()
# # # # # for ch in inputword:
# # # # #     if ch in "aeiou":
# # # # #         vowels.add(ch)
# # # # # print(vowels)

# # # # # vowels1 = {ch for ch in inputword if ch in "aeiou"}

# # # # # n = int(input("enter number: "))
# # # # # L1 = []
# # # # # L1 = [i**2 for i in range(1, n + 1)]
# # # # # print(L1)

# # # # input_list = ["wood", "old", "apple", "big", "item", "euphoria"]
# # # # list_vowel = []
# # # # vowels1 = []
# # # # for word in input_list:
# # # #     if word[0] in "aeiou":
# # # #         list_vowel.append(word)
# # # # print(list_vowel)

# # # # vowels1 = [word for word in input_list if word[0] in "aeiou"]
# # # # print(vowels1)


# # # # # vowels1 = {ch for ch in input_list if ch in "aeiou"}

# # # input_list = list(range(1, 100))
# # # output_dict = {}

# # # for val in input_list:
# # #     if val % 3 == 0:
# # #         output_dict[val] = val**3
# # # print(output_dict)

# # # output_dict1= [val:val**3 for val in input_list if val%3=0]

# # # output_dict= {val : val**3 for val in input_list if val % 3 == 0}

# # # print([i + j for i in "abc" for j in "def"])

# # d = {x.upper(): x * 3 for x in "acbd"}
# # print(d)

# # p = 23 // 5
# # print(p)


# if 1:
#     print("True")

# if 1:
#     print(True)

# for i in range(3):
#     print(i)

print("11 12 13 \n14")

a = 11

b = 12

c = 13

d = 14

print(a, b, c)

print(d)

a = 11

b = 12

c = 13

d = 14

print("{0} {1} {2}".format(a, b, c))

print(d)

a = 11

b = 12

c = 13

d = 14

print("%d %d %d" % (a, b, c))

print(d)

a = 11

b = 12

c = 13

d = 14

print(f"{a}{b}{c}")

print(d)
