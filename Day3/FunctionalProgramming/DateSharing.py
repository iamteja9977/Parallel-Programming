"""
In any assignment of a value, the variable is read first.


Then operation is performed and then, assignment operator is executed.

for eg:

    read varValue
        perform operation
        then assign

So in dataSharing.py, three threads are trying to modify 1 variable data.
if the value of "size" is too large. There will be a race condition.

"""
#code demonstrates a scenario where multiple threads, including the main thread, attempt to modify a shared variable concurrently.

from os import getpid
from threading import Thread
from time import sleep

# this is the data that 2  child threads and 1 main thread will try to modify:
data = 0
# modify thread "size" number of times:
size = 10000000

"""
It initializes a global variable data to 0, and a variable size to 10,000,000,
which determines how many times each thread will try to modify data.

function myFun() which represents the task to be executed by each thread.

Creates two threads (t1 and t2) using the Thread class, with the target function set to myFun().

scenario where multiple threads concurrently attempt to modify a shared variable (data).
 The main thread and two child threads run concurrently, each attempting to increment data a large number of times.
 The purpose is to illustrate potential issues with concurrent access to shared resources, such as race conditions or data inconsistency.
"""


def myFun():
    global data
    print(f"Remember ... {getpid()}--> data: {data}")
    for _ in range(size):
        data += 1
    print("*" * 40)

if __name__ == "__main__":
    print(f"In main... {getpid()}")
    for _ in range(size):
        data += 1

    t1 = Thread(target=myFun)
    t1.start()
    
    print("-" * 40)
    for _ in range(size):
        data += 1

    t2 = Thread(target=myFun)
    t2.start()
    t1.join()
    t2.join()
    print("$" * 40)
    print(f"Finally before exiting: data: {data}")


"""
- Assume there is a 4-way intersection and traffic is coming and going in all directions.
- In the junction of intersection, there will be some conflict between vehicles, on who will go first and who will wait.
- There is a possiblity that two vehicles both move toward the junction and collide. This is called "Race condition".
- There is possibility that vehicles sit stationary in junction due to traffic jam and blocks upcoming traffic. This is called "Deadlock".
- Think of the traffic as read and write operations and junction as data on which read and write operations are working on.
- In programming terminology, this junction is called "Critical section".
- Therefore, to avoid problems, we will appoint a traffic policeman who will manage and schedule traffic.
- Similarly, in programming terms we need a semaphore (counting semaphore) or mutex lock (mutually exclusive lock) to organize the process traffic into our critical section
"""