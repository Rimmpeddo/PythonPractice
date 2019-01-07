from multiprocessing import Process
import os

def info(title):
    print("My name: ", title)
    print("moudle name: ", __name__)
    print("parent id: ", os.getppid())
    print("process id: ", os.getpid())

def f(name):
    info("function f")
    print("name: ", name)

if __name__ == '__main__':
    info("info")
    pr = Process(target = f, args=("function b", ))

    pr.start()
    pr.join()