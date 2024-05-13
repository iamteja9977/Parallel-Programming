#!/usr/bin/python3
# Parallizing bubble sort with multi-threading

#  Bubble Sort:
#     eg: [93, 63, 61, 60, 86, 70, 6, 47, 31, 53]
#     If you notice, two adjacent elements are compared in bubble sort.
#     How about we create two functions which can the inner loop swapping for
#     odd and even indices of the array.
#     This will take some time less than regular algorithm.
#     However, due to context switching between threads, there is some overhead.

"""
Till now we created threads using objects of the Thread class,

    tObj = Thread(target=..., args=...)

Now, we will see how to create a class which inherits Thread class.

Python is "supposed" to support OOP just like C++.
--------------------------------------------------
also note that all threads are not running parallely,
There is some context switching happening that
allows only one thread to run at a time.
This is due to Global Interpreter Lock

"""

def bubbleSort(lst):
    size = len(lst)
    for i in range(size):
        swap = False
        for j in range(size-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swap = True
        if swap is False:
            break


if '__main__' == __name__:
    from sys import argv, exit
    from random import randint
    from time import perf_counter
    from threading import Thread

    if len(argv) <= 1:
        print('pass size')
        exit(1)

    size = int(argv[1])
    lst = [randint(1, size * 10) for _ in range(size)]
    start = perf_counter()
    print('Before List: ', lst)
    tObj = Thread(target=bubbleSort, args=[lst])  # first time sorting
    tObj.start()
    tObj.join()
    print('After List: ', lst)
    end = perf_counter()
    print(f'Time taken: {round(end-start, 3)}')
