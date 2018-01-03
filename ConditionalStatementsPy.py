#!/usr/bin/python3
import random

var1 = 100
if var1:
    print("1 - if 表达式条件为 true")
    print(var1)

var2 = 0
if var2:
    print("2 - if 表达式条件为 true")
    print(var2)
print("Good bye!")
print("-------------------------------------------")

age = 0  # = int(input("请输入你家狗狗的年龄: "))
print("")
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

# 退出提示
# input("点击 enter 键退出")
print("-------------------------------------------")

# 该实例演示了数字猜谜游戏
number = 7
guess = -1
print("数字猜谜游戏!")
while guess != number:
    guess = int(input("请输入你猜的数字："))

    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")

print("-------------------------------------------")

x = random.choice(range(100))
y = random.choice(range(200))
if x > y:
    print('x:', x)
elif x == y:
    print('x+y', x + y)
else:
    print('y:', y)

print("=======欢迎进入狗狗年龄对比系统========")

while True:
    try:
        age = int(input('请输入您家狗的年龄:'))
        print(' ')
        age = float(age)
        if age < 0:
            print("您在逗我？")
        elif age == 1:
            print("相当于人类14岁")
            break
        elif age == 2:
            print("相当于人类22岁")
            break
        else:
            human = 22 + (age - 2) * 5
            print("相当于人类：", human)
            break
    except ValueError:
        print("输入不合法，请输入有效年龄")
# 退出提示
input("点击 enter 键退出")

print("-------------------------------------------")

print('二、数字猜谜游戏')
print('数字猜谜游戏！')

a = 1
i = 0
while a != 20:
    a = int(input('请输入你猜的数字：'))
    i += 1
    if a == 20:
        if i < 3:
            print('真厉害，这么快就猜对了！')
        else:
            print('总算猜对了，恭喜恭喜！')
    elif a < 20:
        print('你猜的数字小了，不要灰心，继续努力！')
    else:
        print('你猜的数字大了，不要灰心，继续加油！')
