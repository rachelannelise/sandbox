
# %%
# map() function returns a map object(which is an iterator) of
# the results after applying the given function to each item of
# a given iterable (list, tuple etc.)

# Returns a list of the results after applying the given function
# to each item of a given iterable (list, tuple etc.)

def addition(n):
    return n + n


# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# %%
# The reduce(fun,seq) function is used to apply a particular
# function passed in its argument to all of the list elements
# mentioned in the sequence passed along.This function is
# defined in “functools” module.

# importing functools for reduce()
import mapreduce

# initializing list
lis = [1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

# %%

val = [1, 2, 3, 4, 5, 6]

# Multiply every item by two
list(map(lambda x: x * 2, val)) # [2, 4, 6, 8, 10, 12]
# Take the factorial by multiplying the value so far to the next item
functools.reduce(lambda x, y: x * y, val, 1) # 1 * 1 * 2 * 3 * 4 * 5 * 6