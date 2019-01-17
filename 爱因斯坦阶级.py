x = 0

while x < 1000:
    if (x % 2 == 1) and (x % 3 == 2) and (x % 5 == 4) and (x % 6 == 5) and (x % 7 == 0):
        print(x)
        x += 1
    else:
        x += 1