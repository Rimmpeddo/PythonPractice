import time
import threading

class MyThread(threading.Thread):
    def __init__(slef,arg):
        super(MyThread,slef).__init__()
        slef.arg = arg

    def run(self):
        time.sleep(2)
        print("The args for this class is {}".format(self.arg))

for i in range(5):
    x = MyThread(i)
    x.start()
    x.join()

print("ALL Done")