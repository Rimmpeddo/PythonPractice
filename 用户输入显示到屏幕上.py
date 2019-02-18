file_name = input("请输入文件名: ")
line_num = input("你所需要的行数: ")

def file_view(file_name, line_num):
    print("文件名:%s, 文件内容的行数%s" %(file_name,  line_num))

    f = open(file_name)
    for i in range(int(line_num)):
        print(f.readline())

    f.close()

file_view(file_name, line_num)