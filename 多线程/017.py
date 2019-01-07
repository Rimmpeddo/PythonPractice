import time
import threading

def func():
    print("I am runing.....")
    time.sleep(5)
    print("I am done.....")

if __name__ == '__main__':
    t = threading.Timer(6,func)
    t.start()

    i = 0
    while True:
        print("{}..............".format(i))
        time.sleep(4)
        i += 1