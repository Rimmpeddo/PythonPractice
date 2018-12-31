with open(r"text.txt",'r',encoding="UTF-8")as f:
    strline = f.readline()
    while strline:
        print(strline)
        strline = f.readline()