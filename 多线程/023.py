import multiprocessing
from time import ctime

def consumer(pull_q):
    print("into consumer.....", ctime())
    while True:
        pull = pull_q.get()
        if pull is None:
            break
        print("pull", pull, "out of")
        pull_q.task_done()
    print("Out of consumer......", ctime())

def producer(sequence, put_q):
    print("into producer.....", ctime())
    for item in sequence:
        put_q.put(item)
        print("push", item, "into of")
    print("Out of producer.....", ctime())

if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    con_q = multiprocessing.Process(target = consumer, args=(q, ))
    con_q.start()

    sequence = [1,2,3,4]
    producer(sequence, q)

    q.put(None)
    con_q.join()