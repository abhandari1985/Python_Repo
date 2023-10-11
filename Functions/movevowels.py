s = input("enter a string: ")
v = ""
c = ""
for char in s:
    if char in ("a", "e", "i", "o", "u"):
        v = v + char
    else:
        c = c + char
print(v + c)
