#Python script that checks whether command-line arguments are passed when the script is executed.
# It checks if the script is being run directly (if '__main__' == __name__:).
#  This condition ensures that the following block of code executes only when the script is run as the main program.

if '__main__' == __name__:
    from sys import argv

    if len(argv) > 1:
        print('Good args are passed.... ', *argv)
    else:
        print('Not good args are not passed')

# python3 cmdLine1.py        
# output: Not good args are not passed

# python3 cmdLine1.py 5
# output: Good args are passed....  cmdLine1.py 5