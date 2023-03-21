password = "123"
while True:
    pwd = input("请输入你想要输入的密码")
    #如果不输入 则为空 为false 取反则为True 执行break
    if not pwd:
        break
    confirm_password = input("请再次输入你的密码")
    if pwd == confirm_password:
        password = pwd
        break
    else:
        print("两次输入的密码不一致")
print("您的初始密码已设置为：%s"%password)
print("进入开锁程序")
while True:
    for i in range(1,4):
        input_pwd = input("请输入你的密码")
        if input_pwd == password:
            print("恭喜你进入门了")
            break
        else:
           if i != 3:
               print("密码错误，你还有%d次机会输入密码"%(3-i))
           else:
               print("系统已经锁定！！")
               break
    break