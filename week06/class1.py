#import for time functions (specific import)
from time import sleep
from time import time
# a+ attendance
strings = ["AMC12", "H45SJS", "WRH3H", "C4SFRD"]
filtered = list(filter(lambda x: len(x) == 5 and x[3].isdigit() and not x[2].isdigit(), strings))
print(filtered[1])
# functions are objects in python and can be passed as arguments or returned
# decorator: @decorator_name
# a function that takes a function and returns a new function, usually an extended version of the passed func
# measure the execution time of a function
def f():
    sleep(0.3) # stops program for 0.3 seconds

def g():
    sleep(0.5)

# create a function that takes another function
# with arguments
# measure is now a decorator
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
f2(.5)
# i do not know why you would do this instead of just making one function that does everything
# for example:
def f3(sleepTime):
    t = time()
    sleep(sleepTime)
    print("this function took ", time()-t)
f3(.5)

# imports allow you to use code from other modules/.py files
# can reuse code by accessing function, classes, and variables defined outside of the file
# searches in current directory, PYTHONPATH, standard library
# import myModule, to use type myModule.funcName(arguments)
# from myModule import funcName, then can just use funcName()
# import myModule as mm -> use mm.funcName()
# from myModule import funcName as fn -> use fn()
