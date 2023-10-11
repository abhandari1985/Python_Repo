def reverse(n):
    reversednum = 0
    while n != 0:
        digit = n % 10
        reversednum = reversednum * 10 + digit
        n //= 10


number = int(input("enter number to reverse: "))
print(reverse(number))
