import time
import threading

def loop1(par):
    print("Start loop 1 at: ", time.ctime())
    print("参数", par)
    time.sleep(4)
    print("End loop 1 at: ", time.ctime())

def loop2(par1,par2):
    print("Start loop 2 at: ", time.ctime())
    print("参数1", par1, "参数2", par2)
    time.sleep(2)
    print("End loop 2 at: ", time.ctime())

def main():
    print("Starting at: ", time.ctime())
    t1 = threading.Thread(target=loop1, args=("哈哈", ))
    t1.start()
    t2 = threading.Thread(target=loop2, args=("神魔", "传说"))
    t2.start()
    print("All done at:", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)