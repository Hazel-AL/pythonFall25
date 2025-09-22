from time import time, sleep

def measure(func):
    def wrapper(*args, **kwargs):
        t = time() # starting time
        func(*args, **kwargs) # function call
        print(func.__name__, "took: ", time()-t)
    return wrapper
# makes measure a wrapper for f2
@measure
def f2(sleepTime = 0.1):
    sleep(sleepTime)