#Exercises = 练习题
'''
#if else 练习题
num = 3
if num % 2 ==0:
    print(str(num) + "是一个偶数")
else:
    print(str(num) + "是一个奇数")
# elif 练习题
score = 59
if score < 60:
    print("您的成绩不合格")
elif score < 90:
    print("n您的成绩合格")
else:
    print("您的成绩优秀")
# if嵌套练习题
score01 = 100
if score01 >= 60:
    if score01 < 70:
        print("您的考试成绩合格")
    elif score01 < 90:
        print("您的成绩为良好")
    else:
        print("您的成绩为优秀")
else:
    print("您的考试成绩不合格")
# 流程控制与逻辑运算符练习题
age = 22
if age > 18 and age < 60:
    print("你已经成年了，快滚去自己工作")
if 16 < age < 90:
    print("你已经成年了，快滚去自己工作")
# if elif 后面总是跟着布尔值，
# count = 0  None 则为false 条件不成立， 当为负数的时候，布尔值为true 条件成立
count = 0
if count:
    print("条件成立")
else:
    print("条件不成立")

result = None
if result:
    pass
else:
    print("什么都不做")

# 循环
lap = 0
while lap <11:
    lap += 1
    print("我跑完了第"+ str(lap - 1 ) + "圈")#

while lap <10:
    lap += 1
    print("我跑完了%s圈" %lap)
'''
# for 循环
seq = "hello"
for s in seq:
    print(s)
for i in range(5):
    print(i)
for s in range(10):
    print("我已经跑了%s圈了" %(s + 1))
#嵌套循环
width,height = 7,3
for i in  range(height):
    for j in range(width):
        print("*" , end="over")
    print()
for i in  range(5):
    for j in range(i + 1):
        print("*",end="")
    print()
for i in range(7):
    for j in range(7 - i):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()
for i in range(1,10):
    for j in range(1,i + 1):
        print("%s * %s = %s "%(j, i, i * j ), end="")
    print()
for i in  range(1,10):
    for j in range(1,10 - i):
        print("%s * %s = %s " % (j, i, i * j), end="")
    print()
total = 0
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end="+")
    total += i
print(" = %s " %total)
s = "238.9237834829"
for i in s:
    if i == '.':
        print()
        break
    print(i, end='')
