# 矩形
for i in range(1,5):
    for j in range(1,6):
        print('*',end=' ')
    print()

print("*"*30)

# 空心矩形
for i in range(1,5):
    for j in range(1,6):
        if i==1 or i==4 or j==1 or j==5:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

print("*"*30)

# 等腰三角形
for i in range(1,6):
    for j in range(6-i,6):
        print("*",end=' ')
    print()

print('*'*30)

# 空心等腰三角形三角形
for i in range(1,7):
    for j in range(7-i,7):
        if i==1 or i==6 or j==7-i or j==6:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

print("*"*30)

# 倒等腰三角形
for i in range(1,6):
    for j in range(1,7-i):
        print("*",end=' ')
    print()

print("*"*30)

# 倒等腰三角形空心
for i in range(1,6):
    for j in range(1,7-i):
        if i==1 or i==5 or j==1 or j==7-i-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

print("*"*30)

# 三角形
for i in range(1,6):
    for j in range(1,6-i):
        print(end=' ')
    for  n in range(6-i,6):
        print("*",end=' ')
    print()

print("*"*30)

# 空心三角形
for i in range(1,6):
    for j in range(1,6-i):
        print(end=" ")
    for n in range(6-i,6):
        if i==5 or  n==6-i or n==5:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

print("*"*30)

# 字母A
for i in range(1,7):
    for j in range(1,7-i):
        print(end=' ')
    for n in range(7-i,7):
        if i==1 or i==4 or n==7-i or n==6:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

print("*"*30)

# 菱形
for i in range(1,6):
    for j in range(1,6-i):
        print(end=' ')
    for n in range(6-i,6):
        print("*",end=' ')
    print()

for i in range(1,5):
    for j in range(6-i,6):
        print(end=' ')
    for n in range(1,6-i):
        print("*",end=' ')
    print()

print("*"*30)

# 空心菱形
for i in range(1,5):
    for j in range(1,6-i):
        print(end=' ')
    for n in range(6-i,6):
        if i == 1 or n==6-i or n==5:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

for i in range(1,6):
    for j in range(6-i,5):
        print(end=' ')
    for n in range(1,7-i):
        if i==5 or n==1 or n==7-i-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

print("*"*30)

# 实心矩形或实心三角形或空心矩形或空心三角形或等实心腰三角形或空心等腰三角形
def shape():
    # 实心矩形
    def a_jx():
        for i in range(1,5):
            for j in range(1,6):
                print("*",end=' ')
            print()

    # 空心矩形
    def b_jx():
        for i in range(1,5):
            for j in range(1,6):
                if i==1 or i==4 or j==1 or j==5:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            print()

    # 实心三角形
    def a_sjx():
        for i in range(1,6):
            for j in range(1,6-i):
                print(end=' ')
            for n in range(6-i,6):
                print("*",end=' ')
            print()

    # 空心三角形
    def b_sjx():
        for i in range(1,6):
            for j in range(1,6-i):
                print(end=' ')
            for n in range(6-i,6):
                if i==1 or i==5 or n==6-i or n==5:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()

    # 实心等腰三角形
    def c_sjx():
        for i in range(1,6):
            for j in range(6-i,6):
                print("*",end=' ')
            print()

    #空心等腰三角形
    def d_sjx():
        for i in range(1,6):
            for j in range(6-i,6):
                if i==1 or i==5 or j==6-i or j==5:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            print()

    print("输入ESC结束")
    shape = input("请输入形状.实心矩形.空心矩形.实心三角形.空心三角形.实心等腰三角形.空心等腰三角形: ")
    if shape == "ESC":
        exit()
    elif shape == "实心矩形":
        a_jx()
    elif shape == "空心矩形":
        b_sx()
    elif shape == "实心三角形":
        a_sjx()
    elif shape == "空心三角形":
        b_sjx()
    elif shape == "实心等腰三角形":
        c_sjx()
    elif shape == "空心等腰三角形":
        d_sjx()
    else:
        print("提示！！！请输入实心矩形.空心矩形.实心三角形.空心三角形.实心等腰三角形.空心等腰三角形中的一个")


# 字母D
for i in range(1,5):
    for j in range(1,4):
        if j == 1:
            print("*",end=' ')
        elif i == 1 or i == 4:
            if j > 2:
                break
            else:
                print("*",end=' ')
        elif i == 2 or i == 3:
            if j > 2:
                print("*",end=' ')
            else:
                print(" ",end=' ')
    print()

print("*"*30)

# 字母B
for i in range(1,4):
    for j in range(1,4):
        if j == 1:
            print("*",end=' ')
        elif i==1:
            if j>2:
                break
            else:
                print("*",end=' ')
        elif i == 2 or i ==3:
            if j > 2:
                print("*",end=' ')
            else:
                print(" ",end=' ')
    print()

for i in range(1,5):
    for j in range(1,4):
        if j == 1:
            print("*",end=' ')
        elif i == 1 or i == 4:
            if j > 2:
                break
            else:
                print("*",end=' ')
        elif i == 2 or i == 3:
            if j > 2:
                print("*",end=' ')
            else:
                print(" ",end=' ')
    print()

print("*"*30)

# 字母P
for i in range(1,7):
    for j in range(1,4):
        if j == 1:
            print("*",end=' ')
        elif i == 1 or i== 4:
            if j > 2:
                break
            else:
                print("*",end=' ')
        elif i == 2 or i == 3:
            if j > 2:
                print("*",end=' ')
            else:
                print(" ",end=' ')
    print()

print("*"*30)

# 字母R
for i in range(1,6):
    for j in range(1,4):
        if j == 1:
            print("*",end=' ')
        elif i == 1 or i == 4:
            if j > 2:
                break
            else:
                print("*",end=' ')
        elif i == 2 or i == 3 or i == 5:
            if j > 2:
                print("*",end=' ')
            else:
                print(" ",end=' ')
    print()

print("*"*30)

