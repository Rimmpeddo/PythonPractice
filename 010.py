import threading
from time import sleep, ctime

class MyThread:

    def __init__(self,name):
        self.name = name

    def loopt(self, loopn, nsec):
        print("Start", loopn, ctime())
        sleep(nsec)
        print("End", loopn, ctime())

def main():
    tx = threading.Thread(target = MyThread("aa").loopt, args=("loop1", 3))
    t = MyThread("x")
    t1 = threading.Thread(target = t.loopt, args=("loop2", 5))
    t1.start()
    tx.start()

    t1.join()
    tx.join()

    print("All Done: ")

if __name__ == '__main__':
    main()