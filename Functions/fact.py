def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


number = int(input("enter integer "))
if number >= 0:
    result = factorial(number)
    print(result)
else:
    print(-1)
