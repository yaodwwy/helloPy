#!/usr/bin/python3
import sys

firstList = [1, 2, 3, 4]
it = iter(firstList)  # 创建迭代器对象
print(next(it))  # 输出迭代器的下一个元素
print(next(it))

print('-----------------------------------------')

secondList = [1, 2, 3, 4]
it = iter(secondList)  # 创建迭代器对象
for x in it:
    print(x, end=' ')

print('\n-----------------------------------------')

thirdList = [1, 2, 3, 4]
it = iter(thirdList)  # 创建迭代器对象
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()

print('\n-----------------------------------------')


def fibonacci(n, w=0):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        # yield a
        a, b = b, a + b
        print('%d,%d' % (a, b))
        counter += 1


f = fibonacci(10, 0)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except:
        sys.exit()
print('\n-----------------------------------------')
