from mpi4py import MPI
import numpy as np
import time
start = time.time()
punten = np.linspace(0,999999,1000000)
kwadraten = np.square(punten)
stop = time.time()
#print(kwadraten)
print(stop-start)
