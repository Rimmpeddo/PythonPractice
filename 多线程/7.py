import time
import threading

def fun():
    print("Start at: ")
    time.sleep(2)
    print("End at: ")

t1 = threading.Thread(target=fun, args=())
t1.setDaemon(True)
# t1.daemon = True
t1.start()

time.sleep(1)
print("All done")