# Create a list with some 100 random values using random module,
# and use bubble sort to sort the contents of the list.

from random import randint


def bubbleSort(lst):
    size = len(lst)

    for i in range(size):
        for j in range(size-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


if '__main__' == __name__:
    from sys import argv, exit

    if len(argv) > 1:
        print("Good args are passed.... ", *argv)
    else:
        print("Not Good args are not passed")
        exit(1)

    size = int(argv[1])
    lst = [randint(1, size * 10) for _ in range(size)]
    print("List: ", lst)

    print("List after sorting:")
    bubbleSort(lst)
    print(lst)

#  python3 RandomListBubble3.py 5
# Good args are passed....  RandomListBubble3.py 5
# List:  [5, 47, 20, 48, 23]
# List after sorting:
# [5, 20, 23, 47, 48]