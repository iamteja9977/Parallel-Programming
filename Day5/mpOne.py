'''
    Simple hello world ...
'''

from mpi4py import MPI

comm = MPI.COMM_WORLD  # default communicator
rank = comm.Get_rank()
print(f"Hello world...From  {rank}")

'''
 mpiexec -n 4 python3 mpOne.py 
Hello world...From  1
Hello world...From  3
Hello world...From  0
Hello world...From  2
'''
