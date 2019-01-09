import char
import 内置函数random练习

print("请选择游戏\n1.字母游戏\n2.random游戏")
game = input("输入1或者2: ")

total = 0
score = 0
while True:
    if game == '1':
        inchar = input("输出字母A-L: ")
        if inchar == 'A':
            char.Char.A("A")
        if inchar == 'B':
            char.Char.B("B")
        if inchar == 'C':
            char.Char.C("C")
        if inchar == 'D':
            char.Char.D("D")
        if inchar == 'E':
            char.Char.E("E")
        if inchar == 'F':
            char.Char.F("F")
        if inchar == 'G':
            char.Char.G("G")
        if inchar == 'H':
            char.Char.H("H")
        if inchar == 'I':
            char.Char.I("I")
        if inchar == 'J':
            char.Char.J("J")
        if inchar == 'K':
            char.Char.K("K")
        if inchar == 'L':
            char.Char.L("L")
    elif game == '2':
        内置函数random练习.rand_gane(total, score)
    else:
        print("输出错误,程序退出")
