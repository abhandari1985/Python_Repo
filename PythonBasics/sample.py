# # # # # # # # # # # # # # # L = [1, 2, 3, 4]
# # # # # # # # # # # # # # # print(L)
# # # # # # # # # # # # # # # print(type(L))

# # # # # # # # # # # # # # # L = [i for i in range(1, 5)]
# # # # # # # # # # # # # # # print(L)
# # # # # # # # # # # # # # # print(type(L))

# # # # # # # # # # # # # # # # L = [for i in range(1, 5): i]
# # # # # # # # # # # # # # # # print(L)
# # # # # # # # # # # # # # # # print(type(L))

# # # # # # # # # # # # # # # # L = [for i in range(1, 5) i]
# # # # # # # # # # # # # # # # print(L)
# # # # # # # # # # # # # # # # print(type(L))

# # # # # # # # # # # # # # L = [2, 3, 4, 2, 1, 2, 3]
# # # # # # # # # # # # # # print(
# # # # # # # # # # # # # #     L.index(2)
# # # # # # # # # # # # # # )  # L.index(k) will return the index of the first occurrence of the element k in L


# # # # # # # # # # # # # L = [2, 1, 2, 4, 5, 3, 6]
# # # # # # # # # # # # # K = 4 in L

# # # # # # # # # # # # # print(K)

# # # # # # # # # # # # L = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# # # # # # # # # # # # print(L[1:-1:2])

# # # # # # # # # # # A = [10, 20, 30]
# # # # # # # # # # # B = [45, 35, 25]
# # # # # # # # # # # B.extend(A)
# # # # # # # # # # # print(B)

# # # # # # # # # # L = [10, 20, 30, 40, 50, 5, 70, 80, 90, 100]

# # # # # # # # # # small = L[0]
# # # # # # # # # # for item in L:
# # # # # # # # # #     if item < small:
# # # # # # # # # #         small = item
# # # # # # # # # #         print(small)
# # # # # # # # # # print("smallest number: ", small)


# # # # # # # # # # Take input here
# # # # # # # # # # we will take input using ast sys
# # # # # # # # # import ast

# # # # # # # # # input_str = input()
# # # # # # # # # input_list = ast.literal_eval(input_str)

# # # # # # # # # # Remember how we took input in the Alarm clock Question in previous Session?
# # # # # # # # # # Lets see if you can finish taking input on your own

# # # # # # # # # data = input_list[0]
# # # # # # # # # check = input_list[1]

# # # # # # # # # # start writing your code to find if check is above average of data
# # # # # # # # # data = input_list[0]
# # # # # # # # # check = input_list[1]

# # # # # # # # # # start writing your code to find if check is above average of data
# # # # # # # # # sum = 0
# # # # # # # # # for item in data:
# # # # # # # # #     sum = sum + item
# # # # # # # # # avg = sum / len(data)
# # # # # # # # # print(check, avg)
# # # # # # # # # if check > avg:
# # # # # # # # #     print("True")
# # # # # # # # # else:
# # # # # # # # #     print("False")

# # # # # # # # print(((500 // 7) % 5) ** 3)
# # # # # # # # T = (3, 5, 7, 11)
# # # # # # # # print(T.append(9))


# # # # # # # L1 = ["Vikas", "Akshay", "Sanskar", "Mahima"]
# # # # # # # print(L1[1][-1])

# # # # # # l = [32, 34, 12, 27, 33]
# # # # # # l.append([14, 19])
# # # # # # print(l)
# # # # # # print(len(l))

# # # # # D = {1: ["Raj", 22], 2: ["Simran", 21], 3: ["Rahul", 40]}
# # # # # for val in D:
# # # # #     print(val)

# # # # for sentence in paragraph:
# # # #     for word in sentence.split():
# # # #         single_word_list.append(word)

# # # # print(list(range(10, 1, -1)))
# # # print(ord(123))

# # # strin = "anand"

# # s = "upGrad"

# # # s = upgrad

# # s = s[:2] + s[2].upper() + s[3:]


# # # "G".join(["up", "rad"])


# # # s = "aabupGradaab".strip("aab")


# # # s = "aabupGradaab".strip("a").strip("b").strip("a")
# # print("G".join(["up", "rad"]))

# # Write your code here
# input_tuple = ("Monty Python", "British", 1969)
# list1 = list(input_tuple)
# list1.append("Python")
# tuple_2 = tuple(list1)
# # Make sure to name the final tuple 'tuple_2'
# print(tuple_2)

# input_str = "Kumar_Ravi_003"
# name_code = input_str.split("_")
# first_name = name_code[0]  # write your answer here
# second_name = name_code[1]  # write your answer here
# customer_code = name_code[2]  # write your answer here
# print(first_name)
# print(second_name)
# print(customer_code)

# list_1 = [2, 33, 222, 14, 25]
# print(list_1[-5])
# word = ["1", "2", "3", "4"]
# word[:] = []
# print(word)
# L = ["one", "two", "three", "four", "five", "six"]
# print(L.sort())
# # print(L)
# input_list = ["SAS", "R", "PYTHON", "SPSS"]
# input_list.pop()
# input_list.append("SPARK")
# print(input_list)


# A = [5, 1, 3, 4, 4, 5, 6, 7]
# B = [3, 3, 5, 5, 1, 7, 2]
# commonlist = list(set(A) & set(B))
# print(sorted(commonlist))

# x = 3.5
# print(float(int(x)))

# name = "I love breaking bad"

# print(name.count("a"))

# import ast

# # Take input
# str_inpt = ast.literal_eval(input())
# # Write your code here
# if len(str_inpt) > 0 and len(str_inpt) < 12:
#     total = sum(str_inpt)
#     print(total)
# else:
#     print(-1)

# Take input here using ast sys
# input_list = ast.literal_eval(input())
# K = int(input())
# # K = 9
# count = 0
# # start writing your code here
# for string in str_inpt:
#     # print(string.isdigit())
#     if string.isdigit():
#         newstring = int(string) + K
#         print(newstring)
#         string = str(newstring)
#         str_inpt[count] = string
#     count += 1
# print(str_inpt)

# Sample Input :
# ['Python', '123', 'Data']
#   4
# Sample Output : ['Python', '127', 'Data']
# l = []
# l = input_list[K - 1 :]
# print(l)

# Take input here
# L = test_str.split(" ")
# newstr = ""
# print(L)


# for string in L:
#     for i in range(0, len(string)):
#         if string[i].isupper():
#             newstr = newstr + string[i]
#     print(newstr)
#     newstr = ""
# def find_max_run_of_uppercase(s):
#     max_run = 0  # To store the length of the maximum run
#     current_run = 0  # To store the length of the current run

#     for char in s:
#         if char.isupper():
#             current_run += 1
#         else:
#             current_run = 0  # Reset the current run if not uppercase

#         if current_run > max_run:
#             max_run = current_run  # Update max_run if current_run is greater

#     return max_run


# # Input string
# test_str = "MuMbaI is in MAHArashTRA"

# # Call the function and print the result
# result = find_max_run_of_uppercase(test_str)
# print(result)
# https://learnpython.com/blog/sort-tuples-in-python/
# sort a list of tuples based on the second element in reverse order
# input_str = [(55, 77), (34, 90), (67, 100), (90, 0)]
# input_str.sort(key=lambda i: i[1], reverse=True)
# print(input_str)
s = input()


def divisible(s):
    if s.find(","):
        num = s.split(",")
        number = ""
        for i in num:
            number = number + i
            s = number
    intnum = int(s)
    while intnum != 0:
        div = intnum % 10
        if intnum % div != 0:
            return 0
            break
        intnum = intnum // 10


if divisible(s) != 0:
    print("Happy Number")
else:
    print("Sad Number")
