#!/usr/bin/env python
"""
Serieel Programma
"""

from mpi4py import MPI
import sys
import time
import math
import numpy as np

aantal = 900000

start = time.time()
gemiddelde = np.mean(np.array([np.random.random_sample()*1000 for x in range(aantal)]))
stop = time.time()

print("gemiddelde: {}".format(gemiddelde))
print(stop-start)
