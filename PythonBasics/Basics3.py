# # If you need to print string in a single line
# # Iterating through string
# string = "New Delhi"
# for ch in string:
#     print(ch, end=";")

# string = "New Delhi"
# for ch in string:
#     print(ch, end="")

# # Iterating through list of integers
# roll = [3, 4, 56, 62, 12]
# for serial in roll:
#     print(serial)

# # Points to note
# # roll, which represents a sequence; it can be a list, a tuple or a string.
# # To put it in a simple way it can be any iterable object.

# # The in operator, which, as you may recall, is a membership operator that
# # helps to check for the presence of an element in a sequence.

# # Iterating over dictionaries
# students_data = {1: ["Sam", 24], 2: ["Rob", 25]}
# print(students_data)

# for key, val in students_data.items():
#     print(key, val)

# # generate range of values
# print(range(1, 5))
# l = list(range(1, 5))
# print(l)
# for i in range(1, 5):
#     print(i, end=" ")

# print(list(range(1, 101, 2)))  # gives numbers 1 to 100 with step count of 2
# print(list(range(100, 0, -1)))


# L1 = [10, 20, 30, 24, 18]
# L2 = [8, 14, 15, 20, 10]
# L3 = []
# for i in range(len(L2)):
#     L3.append(L2[i] - L1[i])
# print(L3)
# Program to get each word in string with capital letter, using title method

# input_list = ["VARMA", "raj", "Gupta", "SaNdeeP"]
# for i in range(len(input_list)):
#     input_list[i] = input_list[i].lower()
# for i in range(len(input_list)):
#     input_list[i] = input_list[i].title()
# print(input_list)

# Program to write prime numbers between 1 to 20

# for n in range(1, 30):
#     flag = True
#     for i in range(2, n):  # i=2,3,4,5,6,7
#         if n % i == 0:
#             # n is not a prime number and we exit inner loop
#             print(n, "is not prime. It is factor of ", i)
#             flag = False
#             break
#     if flag == True:
#         #        print(n, end=" ")
#         print(n)

# l = []
# for i in range(-100, 0):
#     if i % 2 == 0:
#         l.append(i)
# print(l)

# print(list(range(-100, -1, 2)))

# print(sorted(set(range(-2, -101, -2))))

d = {0: "Fish", 1: "Bird", 2: "Mammal"}
for i in d:
    print(i)
