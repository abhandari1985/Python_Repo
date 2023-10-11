def swap(x, y):
    a = x + y - x
    b = x + y - y
    print(
        "Swapping successful !! ",
        "Value for first input is: ",
        a,
        " Value for second input is: ",
        b,
    )
    return (a, b)


input1 = int(input("enter first number to swap: "))
input2 = int(input("enter second number to swap: "))

swap(input1, input2)
