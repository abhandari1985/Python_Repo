# Write a program to count students age above 18
students_data = {
    1: ["Sam", 15],
    2: ["ROb", 18],
    3: ["Kyle", 16],
    4: ["COrner", 19],
    5: ["Trump", 20],
}

f = lambda x: print(x[1]) if x[1] > 18 else print("age is less than 18")
f(["COrner", 19])

len(list(filter(lambda x: x[1] > 18, students_data.values())))
