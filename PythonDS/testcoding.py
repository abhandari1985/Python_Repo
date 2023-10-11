C = [
    7,
    8,
    9,
    18,
    20,
    21,
    25,
    26,
    27,
    31,
    32,
    34,
    35,
    36,
    40,
    43,
    45,
    47,
    53,
    58,
    62,
    67,
    68,
    71,
    72,
    74,
    75,
    76,
    80,
    81,
    82,
    90,
    93,
    95,
    97,
    99,
]
F = [
    1,
    7,
    10,
    13,
    16,
    22,
    24,
    29,
    30,
    32,
    34,
    39,
    40,
    43,
    44,
    48,
    56,
    60,
    65,
    68,
    69,
    73,
    77,
    78,
    90,
    93,
    94,
    95,
    96,
]
H = [
    5,
    12,
    14,
    17,
    20,
    21,
    22,
    25,
    28,
    30,
    37,
    38,
    39,
    40,
    42,
    44,
    57,
    59,
    61,
    62,
    67,
    71,
    75,
    76,
    77,
    82,
    83,
    86,
    87,
    92,
    94,
    95,
]

# # E = ((set(C) & set(H)) | (set(C) & set(F)) | (set(H) & set(F))) - (
# #     set(C) & set(H) & set(F)
# # )
# # print(E, len(E))

# # Set of all students
# all_students = set(C) | set(H) | set(F)
# print(all_students, len(all_students))
# common = (set(C)) | (set(H)) | (set(F))
# print(common, len(common))
# # Find students who do not play any sport
# students_not_playing_any_sport = all_students - common

# # Convert the result to a list
# students_list = list(students_not_playing_any_sport)

# # Print the list of students not playing any sport
# print(students_list)


# C = [
#     7,
#     8,
#     9,
#     18,
#     20,
#     21,
#     25,
#     26,
#     27,
#     31,
#     32,
#     34,
#     35,
#     36,
#     40,
#     43,
#     45,
#     47,
#     53,
#     58,
#     62,
#     67,
#     68,
#     71,
#     72,
#     74,
#     75,
#     76,
#     80,
#     81,
#     82,
#     90,
#     93,
#     95,
#     97,
#     99,
# ]
# F = [
#     1,
#     7,
#     10,
#     13,
#     16,
#     22,
#     24,
#     29,
#     30,
#     32,
#     34,
#     39,
#     40,
#     43,
#     44,
#     48,
#     56,
#     60,
#     65,
#     68,
#     69,
#     73,
#     77,
#     78,
#     90,
#     93,
#     94,
#     95,
#     96,
# ]
# H = [
#     5,
#     12,
#     14,
#     17,
#     20,
#     21,
#     22,
#     25,
#     28,
#     30,
#     37,
#     38,
#     39,
#     40,
#     42,
#     44,
#     57,
#     59,
#     61,
#     62,
#     67,
#     71,
#     75,
#     76,
#     77,
#     82,
#     83,
#     86,
#     87,
#     92,
#     94,
#     95,
# ]

# Create sets from the given lists
C_set = set(C)
F_set = set(F)
H_set = set(H)

# Find the set of all students
all_students_set = set(
    range(1, 101)
)  # Assuming the students are numbered from 1 to 100
print(all_students_set)
# Find students who don't play any of the three sports
students_not_playing_any_sport = all_students_set - (C_set | F_set | H_set)

# Convert the result to a sorted list
students_list = sorted(list(students_not_playing_any_sport))

# Print the list of students who don't play any sport
print(students_list, len(students_list))
