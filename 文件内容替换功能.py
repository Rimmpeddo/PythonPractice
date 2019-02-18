file_name = input("请输入修改文件的名称: ")
old_content = input("原文件需要修改的内容: ")
new_content = input("替换的新内容: ")

def repalce_content(file_name, old_content, new_content):
    f = open(file_name)
    content = []

    for eachline in f:
        if old_content in eachline:
            eachline = eachline.replace(old_content, new_content)

        content.append(eachline)

    decide = input("你确定要这么做吗 输入YES/NO: ")

    if decide in ["YES", "yes", "Yes"]:
        f_write = open(file_name, "w")
        f_write.write("".join(content))
        f_write.close()

repalce_content(file_name, old_content, new_content)