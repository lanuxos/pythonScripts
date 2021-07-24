# multitasks.py
import time, threading

def Tasks():
    for i in range(1, 6):
        print('Task', i)
        time.sleep(0.5)

def Duty():
    for i in range(1, 6):
        print('Duty', i)
        time.sleep(0.5)

# Tasks()
# Duty()

t = threading.Thread(target=Tasks)
d = threading.Thread(target=Duty)

t.start()
d.start()

t.join()
d.join()