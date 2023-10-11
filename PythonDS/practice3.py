# world_cups = {
#     2019: ["England", "New Zealand"],
#     2015: ["Australia", "New Zealand"],
#     2011: ["India", "Sri Lanka"],
#     2007: ["Australia", "Sri Lanka"],
#     2003: ["Australia", "India"],
# }
# print("To check if New Zealad made it to finals in 20th century")
# year = int(input("Enter year: "))
# if year in world_cups:
#     if "New Zealand" in world_cups[year]:
#         print("team was present")
#     else:
#         print("team was not present")

# a = 10
# b = 16
# c = 20

# if a > b and a > c:
#     print("a")
# elif b > a and b > c:
#     print("b")
# else:
#     print("c")

# Given the code below, the output obtained in several runs is 'C' 'A' 'D' 'B'.
# 70, 91, 67, 88
# if score >= 90:
#    print('A')
# elif score >=80:
#    print('B')
# elif score >= 70:
#    print('C')
# elif score >= 60:
#    print('D')
# else:
#    print('F')

# if (10 < 0) and (0 < -10):
#     print("A")
# elif (10 > 0) or False:
#     print("B")
# else:
#     print("C")
if True or True:
    if False and True or False:
        print("A")
    elif False and False or True and True:
        print("B")
    else:
        print("C")
else:
    print("D")
