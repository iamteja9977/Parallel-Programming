'''
    Simple gather sub arrays from multiple processes and store in full array.
'''

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD  # default communicator
rank = comm.Get_rank()
size = comm.Get_size()  # gives total number of processes (-n 4)

dataPerRank = 10
sendData = np.linspace(rank * dataPerRank + 1, (rank + 1)
                       * dataPerRank, dataPerRank)
# if rank = 0 ---> linspace(1, 10, 10)
# if rank = 1 ---> linspace(11, 20, 10)

recvData = None
if rank == 0:
    recvData = np.empty(dataPerRank * size, dtype='d')
else:
    print(f"rank: {rank} --> sending: {sendData}")


# different processes including rank 0 will send their data stored in "sendData",
# process with rank 0 will gather all data sent in sendData by different processes (including itself)
# and store all the combined data in recvData:
comm.Gather(sendData, recvData, root=0)

if rank == 0:
    print(f'rank --> {rank} --> recvData: {recvData}')

"""
mpiexec -n 4 python3 mpFive.py        
rank: 1 --> sending: [11. 12. 13. 14. 15. 16. 17. 18. 19. 20.]
rank: 3 --> sending: [31. 32. 33. 34. 35. 36. 37. 38. 39. 40.]
rank: 2 --> sending: [21. 22. 23. 24. 25. 26. 27. 28. 29. 30.]
rank --> 0 --> recvData: [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12. 13. 14. 15. 16. 17. 18.
 19. 20. 21. 22. 23. 24. 25. 26. 27. 28. 29. 30. 31. 32. 33. 34. 35. 36.
 37. 38. 39. 40.]
"""