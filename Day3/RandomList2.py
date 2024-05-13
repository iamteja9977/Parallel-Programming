from random import randint

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
#  RandomList2.py 5
# Good args are passed....  RandomList2.py 5
# List:  [45, 26, 28, 32, 20]

#  python3 RandomList2.py 10
# Good args are passed....  RandomList2.py 10
# List:  [44, 68, 40, 37, 99, 54, 37, 74, 53, 18]