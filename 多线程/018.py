import time
import threading

num = 0
mutex = threading.RLock()

class myThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        if mutex.acquire(1):
            num = num + 1
            msg = self.name + "set num to" + str(num)
            print(msg)
            mutex.acquire()
            mutex.release()
            mutex.release()

def main():
    for i in range(5):
        t = myThread()
        t.start()

if __name__ == '__main__':
    main()