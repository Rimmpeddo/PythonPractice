import random



total = 0
score = 0

while 1:
    prt = input("请输入数字1,2,3,ESC退出: ")
    ran = random.randrange(1, 4)
    prt = int(prt)

    if prt <= 3:
        pass

        total += 1
        score += 100

        # print("执行次数",total)
        if prt > ran:
            print("系统随机数: ",ran)
            print("你离中奖还有一步距离")
        if prt == ran:
            score += 100
            print("系统随机数: ",ran)
            print("你中奖啦")
            print("中奖概率是{}".format(score/total))
        if prt == ran:
            print("系统随机数: ",ran)
            print("再接再厉")

    else:
        print("请看清楚规则")