file_name = input("请输入要创建的文件名: ")


def input_file(file_name):
    f = open(file_name, "w", encoding="UTF-8")

    while True:
        inpt = input("文件的内容: ")
        if inpt != ":w":
            f.write("%s\n" %inpt)
            print("请继续录入.")
        else:
            print("保存并退出.")
            break
    f.close()

input_file(file_name,)