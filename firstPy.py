#!/usr/bin/python3
# 说明： Fibonacci series: 斐波纳契数列
#       两个元素的总和确定了下一个数
a, b, c = 0, 1, []
while b < 10000:
    # print(b, end=',')
    # print(a, b, sep='@')
    c.append(b)
    a, b = b, a + b
# 输出结果
print('\n10000以内的斐波纳契数列总计：' + str(len(c)) + '个，如下：')
print(c)
