import threading
import time

def countdown(num):
    while num > 0:
        time.sleep(1)
        num -= 1
        print(num)


t = threading.Thread(target=countdown, args=(100,))
t2 = threading.Thread(target=countdown, args=(20,))

t.start()
t2.start()



def add(x, y):
    time.sleep(25)
    return x+y

t = threading.Thread(target=add, args=(2,3))

t.start() # where does it return the answer?
# the one thing you can do with a thread: a join
t.join() # Wait for termination. Doesn't return an answer


# how to handle this? pass it an instance, ie
class Result:
    def __init__(self, value=None, exception=None):
        self.value = value
        self.exception = exception

    def unwrap(self):
        if self.exception:
            raise self.exception
        else:
            return self.value

result = Result()
def add(x,y, result):
    time.sleep(25)
    result.value = x + y

t = threading.Thread(target=add, args=(2,3, result))

