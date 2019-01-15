def func(filename):
    try:
        file = open(filename)
    except Exception as error:
        print("出现异常:{}".format(error))
    else:
        print(file.read())
        file.close()
func("hahaha")

