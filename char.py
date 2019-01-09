# 打印字母A
class Char():
    def A(self):
        for i in range(5):
            for n in range(5-i):
                print(end=' ')
            for j in range(i+1):
                if j==0 or j==i or i==0 or i==3:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            print()

    def B(self):
        for i in range(2):
            for j in range(3):
                if i==0 or i==2:
                    if j<2:
                        print("*",end=' ')
                    else:
                        print(" ",end=' ')
                elif i==1:
                    if j==2 or j==0:
                        print("*",end=' ')
                    else:
                        print(" ",end=' ')
            print()
        for i in range(3):
            for j in range(3):
                if i==0 or i==2:
                    if j<2:
                        print("*",end=' ')
                    else:
                        print(" ",end=' ')
                elif i==1:
                    if j==2 or j==0:
                        print("*",end=' ')
                    else:
                        print(" ",end=' ')
            print()

    def C(self):
        for i in range(5):
            for j in range(3):
                if i==1 or i==2 or i==3:
                    if j==0:
                        print("*",end=' ')
                    else:
                        print(" ",end=' ')
                elif i==0 or i==4:
                    if j==0:
                        print(" ",end=' ')
                    else:
                        print("*",end=' ')
            print()

    def D(self):
        for i in range(3):
            for j in range(3):
                if i==0 or i==2:
                    if j<2:
                        print("*",end=' ')
                    else:
                        print(" ",end=' ')
                elif i==1:
                    if j==2 or j==0:
                        print("*",end=' ')
                    else:
                        print(" ",end=' ')
            print()

    def E(self):
        for i in range(5):
            for j in range(5):
                if i==0 or i==2 or i==4 or j==0:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            print()

    def F(self):
        for i in range(5):
            for j in range(5):
                if i==0 or i==2 or j==0:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            print()

    def G(self):
        for i in range(5):
            for j in range(4):
                if i==0:
                    if j==1 or j==2:
                        print("*",end=' ')
                    else:
                        print(" ",end=' ')
                elif i==1 and j==0:
                    print("*",end=' ')
                elif i==2:
                    if j==0 or j==2 or j==3:
                        print("*",end=' ')
                    else:
                        print(" ",end=' ')
                elif i==3:
                    print("*",end=' ')
                elif i==4:
                    if j==3:
                        print("*",end=' ')
                    else:
                        print(" ",end=' ')
            print()

    def H(self):
        for i in range(5):
            for j in range(5):
                if j==0 or j==4 or i==2:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            print()

    def I(self):
        for i in range(5):
            for j in range(5):
                if i==0 or i==4 or j==2:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            print()

    def J(self):
        for i in range(5):
            for j in range(5):
                if i==0:
                    print("*",end=' ')
                elif i==1 or i==2:
                    if j==2:
                        print("*",end=' ')
                    else:
                        print(" ",end=' ')
                elif i==3:
                    if j==2 or j==0:
                        print("*",end=' ')
                    else:
                        print(" ",end=' ')
                elif i==4:
                    if j==2 or j==1:
                        print("*",end=' ')
                    else:
                        print(" ",end=' ')
            print()

    def K(self):
        for i in range(5):
            for j in range(3):
                if i==0 or i==4:
                    if j==0 or j==2:
                        print("*",end=' ')
                    else:
                        print(" ",end=' ')
                elif i==1 or i==3:
                    if j==0 or j==1:
                        print("*",end=' ')
                    else:
                        print(" ",end=' ')
                elif  i==2:
                    if j==0:
                        print("*",end=' ')
                    else:
                        print(" ",end=' ')
            print()

    def L(self):
        for i in range(5):
            for j in range(5):
                if j==0 or i==4:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            print()
