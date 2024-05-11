from threading import Thread

# which takes an argument nums. This function prints 'X' nums times in a loop.
def doSomeJob(nums):
    for _ in range(nums):
        print('X', end="")


if __name__ ==  "__main__":             # main thread
    tObj = Thread(target = doSomeJob, args=(100,))
    tObj.start()
    # 'O' will be printed 200 times here
    for _ in range(200):
        print('O', end="")

# the doSomeJob function takes an argument nums that specifies how many times to print 'X'.
#  This allows for more flexibility in controlling the number of iterations within the thread.