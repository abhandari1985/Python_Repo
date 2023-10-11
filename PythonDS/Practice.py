# Import required libraries:
# import random

# Print a random integer in the given range:
# print(random.randint(100,135))

# Create a list according to the given condition:
# Question 2: Create a list consisting of first 10 even numbers.

# start = input("Enter starting range of list: ")
# end = input("Enter ending range of list: ")
# from random import randint

# value = random.randint(int(start), int(end), 2)
# print(value)

processed_orders = [
    1152,
    1154,
    1155,
    1156,
    1157,
    1160,
    1161,
    1162,
    1166,
    1169,
    1170,
    1172,
    1176,
    1050,
    1178,
    1051,
    1052,
    1054,
    1058,
    1060,
    1061,
    1062,
    1065,
    1066,
    1067,
    1068,
    1069,
    1076,
    1077,
    1080,
    1081,
    1083,
    1091,
    1085,
    1088,
    1089,
    1131,
    1092,
    1094,
    1095,
    1099,
    1102,
    1103,
    1104,
    1106,
    1107,
    1108,
    1109,
    1111,
    1117,
    1119,
    1121,
    1150,
    1128,
    1129,
    1136,
    1137,
    1139,
    1140,
    1141,
    1144,
    1148,
    1124,
]
# List of order ID’s which are returned
returned_orders = [
    1153,
    1158,
    1159,
    1163,
    1164,
    1165,
    1167,
    1168,
    1171,
    1173,
    1174,
    1175,
    1177,
    1053,
    1055,
    1056,
    1057,
    1059,
    1063,
    1064,
    1070,
    1071,
    1072,
    1073,
    1074,
    1075,
    1078,
    1079,
    1082,
    1084,
    1086,
    1087,
    1090,
    1093,
    1096,
    1097,
    1098,
    1100,
    1101,
    1105,
    1110,
    1112,
    1113,
    1114,
    1115,
    1116,
    1118,
    1120,
    1122,
    1123,
    1125,
    1126,
    1127,
    1130,
    1132,
    1133,
    1134,
    1135,
    1138,
    1142,
    1143,
    1145,
    1146,
    1147,
    1149,
    1151,
]

# processed_orders = [1152, 1161]
# returned_orders = [1153, 1158, 1159, 1170]
print(len(processed_orders) + len(returned_orders))
newlist = []
newlist1 = processed_orders + returned_orders
newlist1.sort()

print(newlist1)
print()
print(sorted(processed_orders))
print()
print(newlist1[49])
if newlist1[49] in processed_orders:
    print("Yes")
else:
    print("No")
# print(newlist1.sort)
# polen = len(processed_orders)
# rolen = len(returned_orders)
# tolen = polen + rolen
# print(tolen)
# i = 0
# j = 0
# for x in range(tolen):
#     print(x)
#     if x % 2 == 0:
#         if i < polen:
#             newlist.append(processed_orders[i])
#             print(processed_orders[i])
#             i = i + 1
#             print("procesed order i: ")
#             print(i)
#         else:
#             break
#     else:
#         if j < rolen:
#             newlist.append(returned_orders[j])
#             print(returned_orders[j])
#             j = j + 1
#             print("returned order j: ")
#             print(j)
#         else:
#             break
#     print(x)
# print(newlist)
# print(newlist[49])
