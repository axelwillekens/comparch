#!/usr/bin/env python
import time
start = time.time()
data = [((x+1) * 10) for x in range (4)]

macht = [data[x] ** 10000 for x in range(4)]

stop = time.time()
print(stop-start)

