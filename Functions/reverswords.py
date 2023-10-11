# Sample input:
# I love coding in python

# Sample output:
# python in coding love I

s = input("enter string: ")
l = s.split(" ")
r = []
for i in range(len(l) - 1, -1, -1):
    r.append(l[i])
reversstr = " ".join(r)
print(reversstr)
