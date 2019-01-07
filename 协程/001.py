from collections import namedtuple

ResClass = namedtuple("Res", "count average")

def averager():
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield
        if term == None:
            break
        total += term
        count += 1
        average = total / count
    return ResClass(count, average)

def proder(storages, key):
    while True:
        storages[key] = yield from averager()

def client():
    process_data = {
        'l_a' : [44.0,75.2,53.5,46,28,96,86.4]
    }

    storages = {}
    for k,v in  process_data.items():
        coroutine = proder(storages, k)

        next(coroutine)

        for dt in v:
            coroutine.send(dt)

        coroutine.send(None)
    print(storages)

if __name__ == '__main__':
    client()