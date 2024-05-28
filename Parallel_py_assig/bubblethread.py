import threading


def usrinput():
    user_input = input("Enter 100 numbers separated by spaces: ")
    lst = list(map(int, user_input.split()))
    return lst


def bubble(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


def printlist(lst):
    for num in lst:
        print(num, end=" ")
    print()  # to add a newline after printing the list


if __name__ == "__main__":
    userlist = usrinput()
    print("Original list:", userlist)

    sorted_list = userlist.copy()
    sortThread = threading.Thread(target=bubble, args=(sorted_list,))
    sortThread.start()
    sortThread.join()

    print("Sorted list:", end=" ")
    printlist(sorted_list)
