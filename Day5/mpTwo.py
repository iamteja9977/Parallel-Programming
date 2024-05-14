'''
    Sending data from one process to another

    Your code seems to be using MPI (Message Passing Interface) for inter-process communication in Python.
    It's structured to send data from one process (rank 0) to another (rank 1)
'''

from mpi4py import MPI

comm = MPI.COMM_WORLD  # default communicator
rank = comm.Get_rank()

# similarly we can send various other data types in python like,
# numpy arrays or python lists, sets, dictionaries and tuples.
print(rank)

if rank == 0:
    data = ["Hello", 32352, 5324.234532, True, (234, "grofea", 432.234)]
    print(f"First Processor sending")
    comm.send(data, dest=1)
elif rank == 1:
    data = comm.recv(source=0)
    print(f"Received data from the first processor: {data}")


'''
mpiexec -n 4 python3 mpTwo.py
2
3
0
First Processor sending
1
Received data from the first processor: ['Hello', 32352, 5324.234532, True, (234, 'grofea', 432.234)]
'''