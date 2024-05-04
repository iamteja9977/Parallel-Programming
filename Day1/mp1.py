import multiprocessing as mp

# it utilizes the multiprocessing module
print(f'Total number of processors: {mp.cpu_count()}')

# mp.cpu_count() is a function provided by the multiprocessing module which returns the number of CPUs (Central Processing Units) in the system.
# This function detects the number of logical CPUs (cores) available to the Python process.

# output the total number of processors (cores) available on your system.
