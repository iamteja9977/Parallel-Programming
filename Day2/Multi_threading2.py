
from threading import Thread

# basic multithreading program in python:

# child thread: 
#  No argument will be taken
def doSomeJob():
    for _ in range(10):
        print('X', end="")

# main thread:
if __name__ ==  "__main__":

    # using Thread class to spawn child threads:
    tObj = Thread(target = doSomeJob)
    tObj.start()

    for _ in range(10):
        print('O', end="")

# same code with for loop and range of 10