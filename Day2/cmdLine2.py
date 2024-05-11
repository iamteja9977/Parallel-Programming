#  the script not only checks whether command-line arguments are passed 
# but also computes the sum of all the integer arguments passed through the command line.

if __name__ == '__main__':
    from sys import argv

    if len(argv) > 1:
        print(f"The input arguments are: {argv}")
        sum = 0
        for i in range(1, len(argv)):
            sum += int(argv[i])
        print(f"The sum of all arguments is: {sum}")
    else:
        print("Pass more command line arguments")


# python3 cmdLine2.py  
#output: Pass more command line arguments

#  python3 cmdLine2.py 1 2 3 4 5
# output:
# The input arguments are: ['cmdLine2.py', '1', '2', '3', '4', '5']
# The sum of all arguments is: 15