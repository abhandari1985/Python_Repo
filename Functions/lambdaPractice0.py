# Syntax of the map function looks as below
# map(function,iterable object)
# The function here can be a lambda function or a function object.
# The iterable object can be a string, list, tuple, set or dictionary.

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Use lambda functions when an anonymous function is required for a short period of time.

# Write a lambda function to check if a number is even or odd
inp = int(input("Enter number: "))
f = lambda x: print("even") if x % 2 == 0 else print("odd")
f(inp)
