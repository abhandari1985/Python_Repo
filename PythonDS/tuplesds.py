# https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
# Tuples are almost similar to Lists with one difference lists are mutable and tuples are not
# Ordered sequence of mix data types
# Written as comma-separated elements within paranthesis
t = ("disco", 12, 4.5)
print(t)
print(type(t))

# tuple can be defined without paranthesis
t1 = "footbal", "messi", 100, 100
print(t1)

# define single value tuple
t2 = (3,)
print(t2)

t3 = (1,)
print(t3)

# Indexing slicing and concatenation are almost similar to what we have seen in strings and lists

# tuple = (2, 3.2, 4, 5)
# t4 = ((1, 2, 3), 4, 5)
# t5 = (hello, "2", "3")
# t6 = "2"
# t = (
#     1,
#     2,
# )
# print(t4)
# print(t5)
# print(tuple[1:-4])
# print(sum(tuple))
# print(min(tuple))
# print(max(tuple))

# t = ("disco", 12, 4.5)
# print(t[0][2])

# Add Items
# Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
# Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
# Example: Convert the tuple into a list, add "Python", and convert it back into a tuple

input_tuple = ("Monty Python", "British", 1969)
tuple_2 = list(input_tuple)
tuple_2.append("Python")
thistuple = tuple(tuple_2)

# Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s),
# and add it to the existing tuple:
y = ("orange",)

input_tuple += y
print(input_tuple)
print(y)

# Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple
fruits = ("apple", "banana", "cherry")  # packing a tuple

# in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# If the number of variables is less than the number of values, you can add an * to the variable name and the
# values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

(green, *yellow, red) = fruits
print(green)
print(yellow)
print(red)
