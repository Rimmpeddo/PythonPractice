import os
import time
import json

exit_flag = False

count = 0

while count < 3:
    user = input("请输入用户名: ")
    f = user.strip() + '.json'
    if os.path.exists(f):
        fp = open(f, "r+", encoding="UTF-8")
        j_user = json.load(fp)
        if j_user['status'] == 1:
            print("账号已被锁定")
            break
        else:
            expire_dt = j_user['expire_date']
            current_st = time.time()
            expire_st = time.mktime(time.strptime(expire_dt, "%Y-%m-%d"))

            if current_st > expire_st:
                print("用户已过期")
                break
            else:
                while count < 3:
                    pwd = input("请输入密码: ")
                    if pwd.strip() == j_user['password']:
                        print("登录成功")
                        exit_flag = True
                        break
                    else:
                        if count == 2:
                            print("用户输入已经超过3次,锁定账号")
                            j_user['status'] == 1
                            fp.seek(0)
                            fp.truncate()
                            json.dump(j_user,fp)
                        count += 1

    if exit_flag:
        break
    else:
        print("用户不存在")
        count += 1

