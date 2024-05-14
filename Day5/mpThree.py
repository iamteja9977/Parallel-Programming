'''
    broadcasting data from one process to other processes.
'''

from mpi4py import MPI

comm = MPI.COMM_WORLD  # default communicator
rank = comm.Get_rank()

if rank == 0:
    data = 'Some data to be send...'
else:
    data = None

data = comm.bcast(data, root=0)
print(f"Rank: {rank} data: {data}")

# broadcast means it will send one data to everyone, including itself.

# if you want to run a large number of processors
# use this command:
# $mpiexec -20 python mpThree.py -core 4
'''
 mpiexec -n 4 python3 mpThree.py
Rank: 0 data: Some data to be send...
Rank: 1 data: Some data to be send...
Rank: 2 data: Some data to be send...
Rank: 3 data: Some data to be send...
'''
# note that here, 20 is the number of processors
# and 4 is the number of processors.
