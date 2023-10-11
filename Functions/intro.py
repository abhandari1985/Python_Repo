# We will work on user defined functions
# order in which arguments are passed matters
# passing variable length arguments


# def var_func(*args):  # random no. of arguments can be passed
#     print(args)


# var_func(1, 3, 5, "abc")


# def var_func1(name, age=55, city="New York"):  # default arguments
#     print(name, age, city)


# var_func1("vikash")
# def func(x=1, y=2):
#     z = x * y + x + y
#     return z


# print(func(2, func(3)))
# L1 = [2, 7, 8, 10, 3]


# def func(y):
#     return y**2 - 2 * y - 2


# ans_list = [func(x) for x in L1]
# print(ans_list)

# lambda functions / anonymous functions as they do not have name

# # to check if a number is even / odd
# f = lambda x: "even" if x % 2 == 0 else "odd"
# print(f(10))

a = 3
b = 5

# Write your code here
greater = lambda x, y: x if x > y else y
print(greater(a, b))
