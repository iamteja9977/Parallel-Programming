'''
    working on single process --- no parallelism
'''

from time import sleep, perf_counter
# sleep is used to pause the execution of the program for a specified number of seconds, and perf_counter is used to measure the elapsed time.
from os import getpid
# the getpid function from the os module. getpid returns the current process's ID.


def doSomeJob():
    print(f'Job Started...{getpid()}')
    sleep(1)
    print(f'Job Completed...')
    print('*' * 40)


# if __name__ == '__main__':: This is a Python idiom. It ensures that the following code block is only executed if the script is run directly, not if it's imported as a module into another script.
if __name__ == '__main__':
    # records the current time before starting the jobs.
    start = perf_counter()

    doSomeJob()  # job1 #sequential execution
    doSomeJob()  # job2
    doSomeJob()  # job3

    end = perf_counter()  # records the current time after completing all jobs.

    print(f'Time taken: {round(end-start,3)} secs')
# Finally, it measures the time taken to complete all three jobs and prints the elapsed time in seconds.
