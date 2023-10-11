# # A Dictionary stores element as key and value pairs. Key is like an index. Values can be mutable, immutable
# # Dict = {key1:value1, key2:value2, ... }
# d = {"India": "INR", "USA": "USD", "France": "EURO"}
# print(d)
# print(d["USA"], d["India"])

# # Replace value for key in dictionary
# d["USA"] = "$"
# print(d)

# # Insert new key: value pair
# d["Japan"] = "Yen"
# print(d)

# # Delete a new key: value pair
# del d["France"]

# # Sort a dictionary
# print(sorted(d))

# # Extract all values from dictionary
# print(d.values())

# # Extract all the keys from dictionary
# print(d.keys())

# # Use update instead of replace
# d.update({"India": "Rupee"})
# print(d)

# # {102:['Shiva', 24, 'Content Strategist'],104:['Udit',25,'Content Strategist'], 105:['Huzefa',32,'Project Manager' ]}
# di = {
#     102: ["Shiva", 24, "Content Strategist"],
#     104: ["Udit", 25, "Content Strategist"],
#     105: ["Huzefa", 32, "Project Manager"],
# }

# print(di[102][2])

# d = {}
# print(d)
# d = {"a": 1, "b": 2}
# print(d)
# d = dict(a=1, b=2)
# print(d)
# # d = ('a':1, 'b':2)
# print(d)

# dict_1 = {"Python": 40, "R": 45}
# del dict_1["R"]
# print(dict_1)

# d = {"Python": 40, "R": 45}
# print(list(d.keys()))

# d = {"Name": "Monty", "Profession": "Singer", "Label": "Instrument"}
# print(d.get("Label", "NA"))

# print(sorted(d.values()))

# Take input here
# we will take input using ast sys
# import ast

# reading the input dictionary
# input_dictionary = input()
# convert_dictionary = ast.literal_eval(input_dictionary)

# reading the input list
# input_list = input()
# convert_list = ast.literal_eval(input_list)

# sizeoflist = len(convert_list)
# for keys in convert_dictionary:
#     for i in range(0, sizeoflist):
#         if keys == convert_list[i][0]:
#             convert_dictionary[keys] = convert_list[i][1]
# print(convert_dictionary)


# import ast

# take input of two dictionaries
# reading the input dictionary
# input_dictionary1 = input()
# convert_dictionary1 = ast.literal_eval(input_dictionary1)
# input_dictionary2 = input()
# convert_dictionary2 = ast.literal_eval(input_dictionary2)
# print(convert_dictionary1, convert_dictionary2)
# d = {}
# # Write the code here
# print(convert_dictionary2.update(convert_dictionary1))
# print(convert_dictionary2)

# Iterating through a dictionary
# d = {"India": "INR", "USA": "USD", "France": "EURO"}
# for key, val in d.items():
#     print(key, val)

L1 = [10, 20, 30, 24, 18]
L2 = [8, 14, 15, 20, 10]
L3 = []
for i in range(len(L2)):
    L3.append(L2[i] - L1[i])
print(L3)
