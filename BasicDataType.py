#!/usr/bin/python3
counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串

print(counter)
print(miles)
print(name)
print("------------------------------------")
a = b = c = 1
print(str(a) + '---' + str(b) + '---' + str(c))
a, b, c = 1, 2, "runoob"
print(str(a) + '---' + str(b) + '---' + str(c))
print("------------------------------------")
"""
六个标准的数据类型：
    Number（数字）
    String（字符串）
    List（列表）
    Tuple（元组）
    Sets（集合）
    Dictionary（字典）
"""
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))


class A:
    pass


class B(A):
    pass


# isinstance()会认为子类是一种父类类型。
print(isinstance(A(), A))  # returns True
print(type(A()) == A)  # returns True
print(isinstance(B(), A))  # returns True
print(type(B()) == A)  # returns False
print("------------------------------------")
var = 'var'
var_a = 'var_a'
var_b = 'var_b'
del var
del var_a, var_b
# print(var) # name 'var' is not defined
print("------------------------------------")
# 数值运算
print(5 + 4)  # 加法
print(4.9 - 2)  # 减法
print(3 * 7)  # 乘法
print(2 / 4)  # 除法，得到一个浮点数
print(2 // 4)  # 除法，得到一个整数
print(17 % 3)  # 取余
a = 2 ** 5  # 乘方
print(a)
print("------------------------------------")
