# Sample input:
# upgradData
# upGradScience

# Sample output:
# upgrad

string1 = (input("enter string1: ")).lower()
string2 = (input("enter string2: ")).lower()

l1 = len(string1)
l2 = len(string2)
l3 = min(l1, l2)
print(l3)
flag = 0
for i in range(l3):
    if string1[i] != string2[i]:
        break
    else:
        i = i + 1
if i == 0:
    print(-1)
else:
    print(string1[:i])
