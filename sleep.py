
import time
while True:
    localtime=time.localtime()
    result=time.strftime("%I:%M:%S %p",localtime)
    print(result)
    time.sleep(1)

import threading

def print_hello():
    for i in range(3):
        time.sleep(0.7)
        print("Hello")

def print_hi():
    for i in range(3):
        time.sleep(0.9)
        print("Hi")
        
t1=threading.Thread(target=print_hello)
t2=threading.Thread(target=print_hi)

t1.start()
t2.start()

    