file1 = input("文件名: ")
file2 = input("文件名: ")

def differ_file(file1,file2):
    f1 = open(file1)
    f2 = open(file2)

    count = 0
    differ = []

    for line1 in f1:
        line2 = f2.readline()

        count += 1
        if line1 != line2:
            differ.append(count)

    f1.close()
    f2.close()

    return differ

dif = differ_file(file1,file2)

if len(dif) == 0:
    print("文件完全相同")
else:
    print("文件共有%s处不同" % len(dif))
    for each in dif:
        print("文件第%s出现不同" % each)