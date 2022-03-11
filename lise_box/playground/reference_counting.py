# %%
class MyClass:
    def __del__(self):
        print("destroying")

a = MyClass()
b = a

import sys
print(sys.getrefcount(a))

# how does this relate to context management
# CMs are easily explained