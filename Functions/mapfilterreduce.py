# Map is a function that works like list comprehensions and for loops. It is used when you need to map or
# implement functions on various elements at the same time.

# The syntax of the map function looks as shown below:
# map(function,iterable object)
# The function here can be a lambda function or a function object.
# The iterable object can be a string, list, tuple, set or dictionary.

# Example of map

list_numbers = (1, 2, 3, 4)
sample_map = map(lambda x: x * 2, list_numbers)
print(list(sample_map))


# Filter operation:

# 'Filter' is similar to map function, only distinguishing feature being that it requires the function to look for
# a condition and then returns only those elements from the collection that satisfy the condition.

# The syntax of the filter function looks as shown below:
# filter(function,iterable object)
# The function object passed to the filter function should always return a boolean value.
# The iterable object can be a string, list, tuple, set or dictionary.

# Filter command used to create an application that can count the number of students whose age is above 18.
students_data = {
    1: ["Sam", 15],
    2: ["Rob", 18],
    3: ["Kyle", 16],
    4: ["Cornor", 19],
    5: ["Trump", 20],
}

len(list(filter(lambda x: x[1] > 18, students_data.values())))
print(len(list(filter(lambda x: x[1] > 18, students_data.values()))))

# 'Reduce' is an operation that breaks down the entire process into pair-wise operations and uses the result
# from each operation, with the successive element. The syntax of reduce function is given below.

# reduce(function,iterable object)

# The function object passed to the reduce function decides what expression is passed to the iterable object.
# The iterable object can be a string, list, tuple, set or dictionary. Also, reduce function produces a single output.

# One important thing to note is that the reduce function needs to be imported from the 'functools' library.
# from functools import reduce

# Let's take a look at an example to understand the reduce  function:
from functools import reduce

list_1 = ["Paul", "Ted"]
print(reduce(lambda x, y: x + y, list_1))

# importing functools library is being imported to access reduce function. In the implementation of the reduce function,
# the lambda function x,y : x+y, list_1 is appending two objects; remember here if the objects are strings it appends
# them if the objects are numbers it adds them.
