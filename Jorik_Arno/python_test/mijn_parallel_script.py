#!/usr/bin/env python
"""
Parallel Hello World
"""

from mpi4py import MPI
import sys
import time

comm = MPI.COMM_WORLD
size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()

if rank == 0:
    start = time.time()
    data = [(x+1)*10 for x in range (size)]
else:
    data = None

data = comm.scatter(data,root=0)
print 'rank',rank,'has data: ', data

data = data ** 10000

macht = comm.gather(data, root=0)

if rank == 0:
    #print macht
    stop = time.time()
    print(stop-start)
