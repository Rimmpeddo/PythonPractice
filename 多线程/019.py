import multiprocessing
from time import sleep, ctime

def func(interval):
    while True:
        print("The time is ", ctime())
        sleep(interval)

if __name__ == '__main__':
    t = multiprocessing.Process(target = func, args=(5, ))
    t.start()
    while True:
        print("Starting process")
        sleep(2)