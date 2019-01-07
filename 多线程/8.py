import time
import threading

def loop1():
    print("Start loop 1 at: ")
    time.sleep(4)
    print("End loop 1 at: ")

def loop2():
    print("Start loop 2 at: ")
    time.sleep(2)
    print("End loop 2 at: ")

def loop3():
    print("Start loop 3 at: ")
    time.sleep(5)
    print("End loop 3 at: ")

def main():
    t1 = threading.Thread(target=loop1, args=())
    t1.setName("THR_1")
    t1.start()

    t2 = threading.Thread(target=loop2, args=())
    t2.setName("THR_2")
    t2.start()

    t3 = threading.Thread(target=loop3, args=())
    t3.setName("THR_3")
    t3.start()

    time.sleep(3)
    for i in threading.enumerate():
        print("正在运行的线程是: {}".format(i.getName()))
    print("正在运行的线程数: ", threading.activeCount())
    print("All Done: ")

if __name__ == '__main__':
    main()
    while True:
        time.sleep(10)