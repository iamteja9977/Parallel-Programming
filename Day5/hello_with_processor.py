'''
    Simple hello world ...
'''

from mpi4py import MPI

comm = MPI.COMM_WORLD # default communicator
rank = comm.Get_rank()

if rank == 0:
    print(f"Hello world...From first processor")
elif rank == 1:
    print(f"Hello world...From second processor")
else:
    print(f"Hello world...From others")

# compile and run this program by going to anaconda environments, play button, open in terminal
# the type following commands in the cmd:

# run the program with this command
# mpiexec -n 4 python hello_world_with_processor.py
'''
output: only rank till 4 becoz we given 4 in the command

 mpiexec -n 4 python3 hello_with_processor.py 
Hello world...From others
Hello world...From others
Hello world...From first processor
Hello world...From second processor
'''