from threading import Thread

# basic multithreading program in python:

# child thread:
def doSomeJob():
    while True:
        print('X', end="")

# main thread:
if __name__ ==  "__main__":

    # using Thread class to spawn child threads:
    tObj = Thread(target = doSomeJob)
    # Inside the main block, it creates an instance of the Thread class named tObj, specifying doSomeJob as the target function.
    tObj.start()

    while True:
        print('O', end="")
        # Outside the Thread block, there's another infinite loop that continuously prints the character 'O'. This loop runs in the main thread.

#  two characters being printed simultaneously: 'X' from the child thread (because of the doSomeJob function) and 
# 'O' from the main thread.