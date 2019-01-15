import random

secret = random.randrange(1,101)

times = 6

while times:
    num = input("输入你猜测的数字: ")
    if num.isdigit():
        temp = int(num)
        if temp == secret:
            print("恭喜你猜对了")
            break
        elif temp < secret:
            print("猜测的数字小了")
            times -= 1
        elif temp > secret:
            print("猜测的数字大了")
        if times == 1:
            print("你还有最后一次机会")
    else:
        print("请输入数字")
