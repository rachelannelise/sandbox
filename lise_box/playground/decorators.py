# %%

#  the @ symbol is basically a syntactic sugar for passing
#  in the decorated function as an argument to the decorator.

class Foo:
    def bar(self,a):
        ...

    @staticmethod
    def spam(a):
        pass
        # @staticmethod is used to define a so - called
        # static class methods(from C++ / Java).A static method
        # is a function that is part of the class, but which does
        #     not operate on instances.

    @classmethod
    def grok(cls,a):
        pass
        # @classmethod is used to define class methods.
        # A class method is a method that receives the class
        # object as the first parameter instead of the instance.

    @property
    def name(self):
        ...


# Examples
class Foo:
    def bar(self):
        print(self)

    @classmethod
    def spam(cls):
        print(cls)

class Foo(object):
    @staticmethod
    def bar(x):
        print('x =', x)
Foo.bar(2)

# Class methods are most often used as a tool for defining
# alternate constructors.

# %%
class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        # Notice how the class is passed as an argument
        tm = time.localtime()
        # And used to create a new instance
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)

import time
tm = time.localtime()

d = Date.today()
test = Date(tm.tm_year, tm.tm_mon, tm.tm_mday)

# %%
# example
import time

def timethis(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            return func(*args,**kwargs)
        finally:
            end = time.time()
            print("%s.%s : %f" % (func.__module__,func.__name__,end-start))
    return wrapper

if __name__ == '__main__':
    @timethis
    def countdown(n):
        while n > 0:
            n-= 1

    countdown(1000000)


# A decorator is usually implemented as a function that creates a
# so-called wrapper function.  Here is a very basic example that shows
# how to define one for logging:

from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

# Example use

@logged
def add(x, y):
    return x + y

add(2,3)   # Should see the "Calling add" message added