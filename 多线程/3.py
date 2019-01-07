import time
import _thread as thread

def loop1(pra):
    print("Start loop 1 at: ", time.ctime())
    print("参数", pra)
    time.sleep(4)
    print("End loop 1 at: ", time.ctime())

def loop2(pra1,pra2):
    print("Start loop 2 at: ", time.ctime())
    print("参数1", pra1, "参数2", pra2)
    time.sleep(2)
    print("End loop 2 at: ", time.ctime())

def main():
    print("Starting at: ", time.ctime())
    thread.start_new_thread(loop1, ("哈哈", ))
    thread.start_new_thread(loop2, ("神魔", "传说"))
    print("Doneing at: ", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)