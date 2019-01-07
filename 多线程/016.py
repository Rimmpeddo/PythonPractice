import threading
from time import sleep

semaphore = threading.Semaphore(3)

def fun():
    if semaphore.acquire():
        for i in range(5):
            print(threading.currentThread().getName() + "get acquire")
        sleep(5)
        semaphore.release()
        print(threading.currentThread().getName() + "realse semaphore")

if __name__ == '__main__':
    for i in range(8):
        thr_a = threading.Thread(target=fun)
        thr_a.start()