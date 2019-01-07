import threading
sum = 0
num = 1000000

class myThread:

    def __init__(self,name):
        self.name = name

    def myAdd(self):
        global sum, num
        for i in range(sum, num):

            sum += 1

    def myReduce(self):
        global sum, num
        for i in range(sum, num):
            sum -= 1


if __name__ == '__main__':
    t1 = threading.Thread(target = myThread("add").myAdd, args=())
    t2 = threading.Thread(target = myThread("reduce").myReduce, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(sum)
    print("All done at: ")
