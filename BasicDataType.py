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

stra = 'Runoob'

print(stra)  # 输出字符串
print(stra[0:-1])  # 输出第一个到倒数第二个的所有字符
print(stra[0])  # 输出字符串第一个字符
print(stra[2:5])  # 输出从第三个开始到第五个的字符
print(stra[2:])  # 输出从第三个开始的后的所有字符
print(stra * 2)  # 输出字符串两次
print(stra + "TEST")  # 连接字符串
print("------------------------------------")
# List（列表）
l1 = ['abcd', 786, 2.23, 'runoob', 70.2]
l2 = [123, 'runoob']
print(l1)  # 输出完整列表
print(l1[0])  # 输出列表第一个元素
print(l1[1:3])  # 从第二个开始输出到第三个元素
print(l1[2:])  # 输出从第三个元素开始的所有元素
print(l2 * 2)  # 输出两次列表
print(l1 + l2)  # 连接列表
a = [1, 2, 3, 4, 5, 6]
a[0] = 9
a[2:5] = [13, 14, 15]
print(a)
a[2:5] = []  # 将对应的元素值设置为 []
print(a)
print("------------------------------------")
# Tuple（元组）
tuple1 = ('abcd', 786, 2.23, 'runoob', 70.2)
tuple2 = (123, 'runoob')

print(tuple1)  # 输出完整元组
print(tuple1[0])  # 输出元组的第一个元素
print(tuple1[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple1[2:])  # 输出从第三个元素开始的所有元素
print(tuple2 * 2)  # 输出两次元组
print(tuple1 + tuple2)  # 连接元组
# tuple1[0] = 11  # 修改元组元素的操作是非法的
tup1 = ()  # 空元组
tup2 = (20,)  # 一个元素，需要在元素后添加逗号
print(tup1)
print(tup2)
# string、list和tuple都属于sequence（序列）
print("------------------------------------")
# Set（集合）
value01 = 'a'
value02 = 'b'
value03 = 'b'
parame = {value01, value02, value03}
print(parame)
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)  # 输出集合，重复的元素被自动去掉
# 成员测试
if ('Rose' in student):
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)  # a和b的差集
print(a | b)  # a和b的并集
print(a & b)  # a和b的交集
print(a ^ b)  # a和b中不同时存在的元素
print("------------------------------------")
# Dictionary（字典）
dict1 = {}
dict1['one'] = "1 - 菜鸟教程"
dict1[2] = "2 - 菜鸟工具"
tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(dict1['one'])  # 输出键为 'one' 的值
print(dict1[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值
d = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(d)
d.clear()
print(d)
d = {x: x ** 2 for x in (2, 4, 6)}
print(d)
d = dict(Runoob=1, Google=2, Taobao=3)
print(d)
print("------------------------------------")


# int(x [,base])将x转换为一个整数
# float(x)将x转换到一个浮点数
# complex(real [,imag])创建一个复数
# str(x)将对象 x 转换为字符串
# repr(x)将对象 x 转换为表达式字符串
# eval(str)用来计算在字符串中的有效Python表达式,并返回一个对象
# tuple(s)将序列 s 转换为一个元组
# list(s)将序列 s 转换为一个列表
# set(s)转换为可变集合
# dict(d)创建一个字典。d 必须是一个序列 (key,value)元组。
# frozenset(s)转换为不可变集合
# chr(x)将一个整数转换为一个字符
# ord(x)将一个字符转换为它的整数值
# hex(x)将一个整数转换为一个十六进制字符串
# oct(x)将一个整数转换为一个八进制字符串
# 可变长参数
def test(*args):
    print(args)
    return args


print(type(test(1, 2, 3, 4)))  # 可以看见其函数的返回值是一个元组


def example(d):
    # d 是一个字典对象
    for c in d:
        print(c)
        # 如果调用函数试试的话，会发现函数会将d的所有键打印出来;
        # 也就是遍历的是d的键，而不是值.


f = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
e = example(f)
print(e)
for c in f:
    print(c, ':', f[c])
print("------------------------------------")
list = ['abcd', 786, 2.23, 'runoob', 70.2]
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2])
print(list[2:3])
a = 1
a = 1.001
a = "python"
print(a)
dict1 = {'abc': 1, "cde": 2, "d": 4, "c": 567, "d": "key1"}
for k, v in dict1.items():
    print(k, ":", v)
dict_1 = dict([('a', 1), ('b', 2), ('c', 3)])  # 元素为元组的列表
print(dict_1)
dict_2 = dict({('a', 1), ('b', 2), ('c', 3)})  # 元素为元组的集合
print(dict_2)
dict_3 = dict([['a', 1], ['b', 2], ['c', 3]])  # 元素为列表的列表
print(dict_3)
dict_4 = dict((('a', 1), ('b', 2), ('c', 3)))  # 元素为元组的元组
print(dict_4)
