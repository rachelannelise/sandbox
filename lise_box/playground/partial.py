import functools

def power(base, exp):
    return base ** exp

# partial, which locks in some of the parameters to the function
cube = functools.partial(power, exp=3)
cube(5)  # returns 125