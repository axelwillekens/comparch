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
aantal = 9000

if rank == 0:
    start = time.time()
    a = np.linspace(1,aantal,aantal)
    b = np.linspace(aantal,1,aantal)
else:
    a = None
    b = None

aantal_per_pi = aantal/size

c = np.empty([size, aantal_per_pi])

local_a = np.zeros(aantal_per_pi)
local_b = np.zeros(aantal_per_pi)

comm.Scatter(a, local_a, root=0)
comm.Scatter(b, local_b, root=0)

local_c = np.arctan(np.log(np.power(np.log(local_a ** 20) + np.log(local_b ** 20),0.05)))
for i in range(1000):
    local_c = local_c + np.arctan(np.log(np.power(np.log(local_a ** 20) + np.log(local_b ** 20),0.05)))

comm.Gather(local_c, c, root=0)

if rank == 0:
    #print c
    stop = time.time()
    print(stop-start)
