user_pass = {"Rimm":"hncsm", "Repker":"cyf"}

def creat_user(username, password):
    usernames = user_pass.keys()

    if username in usernames:
        print("此名称已被注册")
    else:
        print("恭喜你成为本站会员")
        user_pass[username] = password

def login_user(username, password):
    usernames = user_pass.keys()

    if username not in usernames:
        print("此战没有该会员")
    elif password != user_pass[username]:
        print("密码错误")
    else:
        print("登录成功")

