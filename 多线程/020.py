import multiprocessing
import time

class myProcess(multiprocessing.Process):
    def __init__(self,interval):
        super().__init__()
        self.interval = interval

    def run(self):
        while True:
            print("Time: ", time.ctime())
            time.sleep(self.interval)

if __name__ == '__main__':
    t = myProcess(3)
    t.start()
    while True:
        print("Starting at........")
        time.sleep(2)
