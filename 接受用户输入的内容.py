filename = input("文件名: ")

def user_inpt(filename):
    f = open(filename, "w", encoding="UTF-8")
    print("用户输入信息录入(:w保存并退出)")

    while True:
        some_ipt = input("输入内容: ")

        if some_ipt != ":w":
            f.write("%s\n" % some_ipt)
            print("继续录入")
        else:
            print("保存退出")
            break
    f.close()

user_inpt(filename)