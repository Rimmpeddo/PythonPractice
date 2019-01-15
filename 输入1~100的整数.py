num = input("请输入数字: ")

if num.isdigit():
    num = int(num)
    if 1 <= num <= 100:
        print("你真帅")
    else:
        print("天黑请关灯")
else:
    print("你玩蛇")