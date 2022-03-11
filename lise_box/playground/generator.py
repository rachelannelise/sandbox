# %%

# Generator-Function : A generator-function is defined like a
# normal function, but whenever it needs to generate a value, it
# does so with the yield keyword rather than return. If the body
# of a def contains yield, the function automatically becomes a
# generator function.
# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
	yield 1
	yield 2
	yield 3

# Driver code to check above generator function
for value in simpleGeneratorFun():
	print(value)

# %%
# Generator-Object : Generator functions return a generator
	# object. Generator objects are used either by calling
	# the next method on the generator object or using the
	# generator object in a “for in” loop (as shown in the above
	# program).

	# A generator function


def simpleGeneratorFun():
	yield 1
	yield 2
	yield 3


# x is a generator object
x = simpleGeneratorFun()

# Iterating over the generator object using next
print(x.__next__())
print(x.next())
print(x.next())

# Applications : Suppose we to create a stream of Fibonacci
# numbers, adopting the generator approach makes it trivial;
# we just have to call next(x) to get the next Fibonacci number
# without bothering about where or when the stream of numbers ends.

# A more practical type of stream processing is handling large
# data files such as log files. Generators provide a space
# efficient method for such data processing as only parts of the
# file are handled at one given point in time. We can also use
# Iterators for these purposes, but Generator provides a quick
# way (We don’t need to write __next__ and __iter__ methods here).

# Another full example: http://www.dabeaz.com/finalgenerator/
