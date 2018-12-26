str = "我的身高{},我的体重{}"
rst = str.format(180,60)
print(rst)

print("="*30)

str = "我的身高{0},我的体重{1},我的身{0}"
rst = str.format('180cm','60kg')
print(rst)

print("="*30)

str = "我的身高{height},我的体重{weight}"
rst = str.format(height='180cm',weight='60kg')
print(rst)

print("="*30)

str = "我的身高{0[0]},我的体重{0[1]}"
rst = str.format("180cm","60kg")
print(rst)

str = "我的身高{0[h]},我的体重{0[w]}"
dict = {'h':'180cm','w':'60kg'}
rst = str.format({'h':'180cm','w':'60kg'})
print(rst)

print("="*30)

rst = "结果{:0.03f}".format(3.1415926)
print(rst)

print("="*30)

rst = '10的二进制是{:b}'.format(10)
print(rst)
rst = '10的八进制是{:o}'.format(10)
print(rst)
rst = '10的十六进制是{:x}'.format(10)
print(rst)
rst = '10的十进制是{:d}'.format(10)
print(rst)

print("="*30)

rst = '{:,}'.format(9000000000000000000000)
print(rst)

print("="*30)

rst = "无所谓{:^8}".format("谁会")
print(rst)
rst = "无所谓{:>8}".format("谁会")
print(rst)
rst = "无所谓{:*>8}".format("谁会")
print(rst)

print("="*30)

for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}".format(i,j,i*j),end=' ')
    print()

print("="*30)

for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d"%(i,j,i*j),end=' ')
    print()
