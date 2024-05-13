## Simple Hello world program from mpi4py:
"""
 the installation of mpi4py due to the missing mpi.h header file. This file is required for compiling mpi4py, and its absence indicates that the MPI development files are not installed on your system.

To resolve this issue, you need to install the MPI development package. The package name may vary depending on your operating system and MPI implementation.
"""
# sudo apt-get install libmpich-dev
# pip install mpi
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print("Hello world from process",rank,"of",size)
# Hello world from process 0 of 1