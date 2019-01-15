import random


score = 0
total = 0

def line10():
    for i in range(4):
        str_a = random.randrange(65, 91)
        str_b = chr(str_a)
        print(str(str_b),end=' ')

    for i in range(8):
        str_c = random.randrange(1,101)
        print(str(str_c),end=' ')


def rand_gane(total,score):
    while 1:
        num = input("请输入Dight,输入ESC退出:")
        nums = random.randrange(100, 999)

        if num == "ESC":
            break

        if num == "esc":
            break

        if num.isdigit() and int(num) >=100  <=999:


            num = int(num)

            total += 1
            print("第{}次运行".format(total))

            score += 100

            if num > nums:
                a = nums//100
                b = nums%100//10
                c = nums%10
                print("输入数字大于系统随机数字")
                print("系统随机数: ",nums)
                print("百位{}个位{}十位{}".format(a,b,c))

            if num == nums:
                i += 100
                print("输入数字等于系统随机数")
                print("系统随机你数:",score)
                print("恭喜你中奖了:{} 积分加{}".format(nums,i))
                print("中奖的几率是{}".format(score))

            if num < nums:
                print("输入数字小于系统随机数")
                print("系统随机数: ",nums)
                line10()
                print()

        else:
            print("请按照规定输入")
            print("-"*30)


        print("-"*30)

rand_gane(total,score)
