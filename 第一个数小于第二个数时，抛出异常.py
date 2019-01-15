def jiajian(a,b):
    if a < b:
        raise BaseException("被减数不能小于减数")
    else:
        return a - b

try:
    jiajian(4, 5)
except BaseException as error:
    print("发生错误,{}".format(error))
