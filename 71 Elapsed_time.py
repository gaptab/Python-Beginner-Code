import time
start=time.time()
print(22.2*3)
time.sleep(0)
end=time.time()
print("Elapsed time:\n",end-start)

from timeit import default_timer as timer
start=timer()
print(22.9*9)
end=timer()
print("Elapsed time:\n",end-start)
