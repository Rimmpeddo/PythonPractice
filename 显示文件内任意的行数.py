file_name = input("请输入文件名: ")
line_num = input("需要打印的的行数,如 1：9，0：2 ：")

def print_line(file_name, line_num):
    f = open(file_name)

    start, end = line_num.split(":")

    if start == "":
        start = "1"
    if end == "":
        end = "-1"

    start = int(start) - 1
    end = int(end)

    lines = end - start

    for i in range(start):
        f.readline()

    if lines < 0:
        print(f.read())
    else:
        for i in range(lines):
            print(f.readline())


print_line(file_name, line_num)