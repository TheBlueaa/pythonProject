# String functions Demo  = 字符串函数demo
cellphone_number_start = '13, 15, 17, 18, 19'
telephone_number_start = '010，020, 021, 022, 025, 0888, 05555'
while True:
    num = input("请输入一个电话好嘛 \n ")
    if num =="exit":
        break
    if not num:
        print("电话号码不能为空")
        continue
    num = num.strip()
    if not num.isdigit():
        print("请输入一个数字字符")
        continue
    if num.startswith('1') and len(num) ==11 and num[0:2] in cellphone_number_start:
        print("这是一个电话号码")
    elif num.startswith('400') and len(num) ==10:
        print("这是一个广告号码")
        continue
    elif num.startswith('0'):
        if(len(num) == 12 and num[0:4] in telephone_number_start or len(num) == 11 \
        and num[0:3] in telephone_number_start):
            print("这是一个固定的电话号码")
            continue
    print("无法识别该号码")







