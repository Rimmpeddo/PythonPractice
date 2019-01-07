import threading
import time

def fun():
    print("Start at: ")
    time.sleep(2)
    print("End at: ")

print("Starting as: ")

t1 = threading.Thread(target=fun, args=())
t1.start()

time.sleep(1)
print("All done")