import threading
from time import sleep

lock1 = threading.Lock()
lock2 = threading.Lock()

def fun_1():
    print("Starting fun 1")
    lock1.acquire()
    print("fun 1 申请 lock 1")
    sleep(2)
    print("等待 lock 1  ")
    lock2.acquire()
    print("fun 1 申请 lock 2")
    lock2.release()
    print("fun 1 释放 lock 2")
    lock1.release()
    print("fun 1 释放 lock 1")
    print("Fun 1 All done")

def fun_2():
    print("Starting fun 2")
    lock2.acquire()
    print("fun 2 申请 lock 2")
    sleep(4)
    print("等待 lock 2")
    lock1.acquire()
    print("fun 2 申请 lock 1")
    lock2.release()
    print("fun2 释放 look 2")
    lock1.release()
    print("fun2 释放 look 1")
    print("Fun 2 All done")

if __name__ == '__main__':
    print("程序启动")

    thr_1 = threading.Thread(target = fun_1, args=())
    thr_2 = threading.Thread(target = fun_2, args=())

    thr_1.start()
    thr_2.start()
