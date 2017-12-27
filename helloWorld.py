#!/usr/bin/python3
# 说明：用于执行 './script.py' 时制定路径
import keyword

print("Hello, World!")
print("------------------------------------")
# python保留字
print(keyword.kwlist)
print("------------------------------------")
# 单行注释
'''
多行注释一
'''
"""
多行注释二
"""
if True:
    print("True")
else:
    print("False")
# print("缩进不一致，会导致运行错误")
print("------------------------------------")
# 多行语句
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
        item_two + \
        item_three
print(total)
total = ['item_one', 'item_two', 'item_three',
         'item_four', 'item_five']
print(total)
total = 'item_one' \
        + 'item_two' \
        + 'item_three' \
        + 'item_four' \
        + 'item_five'
print(total)
print("------------------------------------")
# 类型：整数、长整数、浮点数和复数
n1 = 1
n2 = 1.23
n3 = 999999999999999999999999999999999999
n4 = 1.1 + n3
print(str(type(n1)) + ' -->> ' + str(type(n2)) + ' -->> ' + str(type(n3)) + ' -->> ' + str(type(n4)))
print(n4)
# 自然字符串
print("this is a line with \n")
print(r"this is a line with \n", end='')  # 不换行需要在变量末尾加上 end=""：
print(R"this is a line with \n")
print("------------------------------------")
word = '字符串，'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""
print(word + sentence + paragraph)
print("------------------------------------")
# input("\n按下 enter 键后退出。")
print('已退出')
print("------------------------------------")
expression = True
if expression:
    print('suite11')
elif expression:
    print('suite22')
else:
    print('suite33')
