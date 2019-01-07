import time

def loop1():
    print("Start loop 1 in", time.ctime())
    time.sleep(2)
    print("End loop 1 in", time.ctime())

def loop2():
    print("Start loop 2 in", time.ctime())
    time.sleep(4)
    print("End loop 2 in", time.ctime())

def main():
    loop1()
    loop2()

if __name__ == '__main__':
    main()