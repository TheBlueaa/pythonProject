#String functions  = 字符串函数
password = "123"
leaft_password = "lstrip的作用去除左边空格:" + "   123".lstrip()#去除左边空格
right_password = "rstrip的作用去除右边空格:" + "123    ".rstrip()#去除右边空格
center_password = "lstrip的作用去除左右空格:" + "  123   ".strip()#去除左右空格
print(password == leaft_password and password == right_password and  password == center_password)
print(leaft_password)
print(right_password)
print(center_password)

# 字母大写
case1 = "upper的作用就是将所有的字符变为大写：" + "test Test".upper()
case2 = "capitalize的作用就是将字符的首字母变为大写：" + "test Test".capitalize()
case3 = "lower的作用就是将所有的字符变为小写：" + "test Test".lower()
case4 = "title的作用就是将所有的字符的首子母变为大写：" +  "test Test".title()
case5 = "test Test".startswith("e")
case6 = "test Test".endswith("t")
case7 = "test Test".isdigit()
case8 = "test Test".islower()
case9 = "test Test".isupper()
case10 = "test Test".find("k")
case11 =  "test Test".index("T")
case12 = "test Test".count("T")
case13 = "Tesst Test".replace("T", "S")
print(case1)
print(case2)
print(case3)
print(case4)
print( "startswith的作用查看是否以指定的字符串开头：" ,case5)
print("endswith的作用查看是否以指定的字符串结尾：" , case6)
print("isdigit的作用查看是否是一串数字：" , case7)
print( "islower的作用查看是否全是小写字母：" , case8)
print("isupper的作用查看是否全是大写字母：" , case9)
print("find的作用查找字符串中的位置，没有返回false：" , case10)
print("index的作用查看字符串中的位置，没有就报错：" ,case11)
print("count的作用统计字符串出现的次数：" , case12)
print("replace的作用就是替换字符串中某些部分的功能",case13)

r = range(10)
len(r)
print(len(r))
print(len("China"))










