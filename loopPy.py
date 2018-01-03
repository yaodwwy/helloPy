#!/usr/bin/env python3

n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print('1到%d 之和为：%d' % (n, sum))

print("-------------------------------------------")

count = 0
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:
    print(count, " 大于或等于 5")

print("-------------------------------------------")

flag = 1
while flag:
    print('欢迎访问菜鸟教程!')
    break
print("Good bye!")

print("-------------------------------------------")

languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x)

for i in range(5, 9):
    print(i)

for i in range(0, 10, 3):
    print(i)

list1 = list(range(5))
print(list1)

for letter in 'Runoob':  # 第一个实例
    if letter == 'o':  # 字母为 o 时跳过输出
        continue
    print('当前字母 :', letter)

var = 10  # 第二个实例
while var > 0:
    var = var - 1
    if var == 5:  # 变量为 5 时跳过输出
        continue
    print('当前变量值 :', var)
print("Good bye!")

print("-------------------------------------------")

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n // x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')

# while True:
# pass  # 等待键盘中断 (Ctrl+C)
sequence = [12, 34, 34, 23, 45, 76, 89]
for i, j in enumerate(sequence):
    print(i, j)

print("-------------------------------------------")

l = 1
while l <= 9:
    j = 1
    while j <= l:
        mut = j * l
        print("%d*%d=%d" % (j, l, mut), end='  ')
        j += 1
    print('')
    l += 1

print("-------------------------------------------")

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end='')
    print('\r')

print("-------------------------------------------")
a = 1
if a > 1:
    pass  # 如果没有内容，可以先写pass，但是如果不写pass，就会语法错误

print("-------------------------------------------")

while True:
    number = input('请输入一个整数(输入Q退出程序)：')
    if number in ['q', 'Q']:
        break  # 如果输入的是q或Q,结束退出
    elif not number.isdigit():
        print('您的输入有误！只能输入整数(输入Q退出程序)！请重新输入')
        continue  # 如果输入的数字不是十进制,结束循环,重新开始
    else:
        number = int(number)
        print('十进制 --> 十六进制 ：%d -> 0x%x' % (number, number))
        print('十进制 -->   八进制 ：%d -> 0o%o' % (number, number))
        print('十进制 -->   二进制 ：%d ->' % number, bin(number))
