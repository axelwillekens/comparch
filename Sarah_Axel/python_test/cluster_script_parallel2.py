#!/usr/bin/env python
"""
Parallel Programma
"""

from mpi4py import MPI
import sys
import time
import math
import numpy as np

comm = MPI.COMM_WORLD
size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()
aantal = 900000

if rank == 0:
    start = time.time()
    a = np.array([np.random.random_sample()*1000 for x in range(aantal)])
else:
    a = None

aantal_per_pi = aantal/size
local_a = np.zeros(aantal_per_pi)
comm.Scatter(a, local_a, root=0)

gem = np.array(np.mean(local_a))

recv_buf = None
if rank == 0:
    recv_buf = np.empty([size, 1])

comm.Gather(gem, recv_buf ,root=0)
totaalgem = np.mean(recv_buf)

if rank == 0:
    stop = time.time()
    print("gemiddelde: {}".format(totaalgem))
    print("recv array: {}".format(recv_buf))
    print(stop-start)
