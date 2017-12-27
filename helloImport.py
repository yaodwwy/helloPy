#!/usr/bin/python3
# Windows 下可以不写第一行注释:

import sys
from sys import path  # 导入特定的成员

print('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)

print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path


def example(anything):
    """形参为任意类型的对象，
       这个示例函数会将其原样返回。
    """
    return anything + 'ok'


print(example('999'))
# help() 函数可以打印输出一个函数的文档字符串
print(help(print))
