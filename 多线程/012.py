import threading

sum = 0
num = 1000000

lock = threading.Lock()

class myThread:

    def __init__(self, name):
        self.name = name

    def myAdd(self):
        global sum, num
        for i in range(1, num):
            lock.acquire()
            sum += 1
            lock.release()


    def myReuduce(self):
        global sum, num
        for i in range(1, num):
            lock.acquire()
            sum -= 1
            lock.release()

if __name__ == '__main__':
    print("Starting is sum = ", sum)

    t1 = threading.Thread(target = myThread("add").myAdd, args=())
    t2 = threading.Thread(target = myThread("ruduce").myReuduce, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("All Done sum = ", sum)