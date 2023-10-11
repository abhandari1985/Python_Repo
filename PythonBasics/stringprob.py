input_string = "Programming is 100% fun"
newstrn = ""
for i in input_string:
    if i not in ("[@_!#$%^&*()<>?/\|}{~:] "):
        if i not in ("0123456789"):
            newstrn = newstrn + i
print(newstrn.swapcase())
