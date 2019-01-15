class MyError(Exception):
    def __init__(self, stri):
        self.stri = stri

    def process(self):
        if len(self.stri) < 5:
            print("字符串长度小于5")
        else:
            print("咕咕咕")

try:
    MEr = MyError("waaaa")
    MEr.process()
except MyError as error:
    print(error)