import builtins

def hello():
    print("Hello World!")


hello()


# 计算面积函数
def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)


print_welcome("Runoob")
w = 4.1
h = 5.9
print("width =", w, " height =", h, " area =", area(w, h))


# 定义函数
def printMe(s):
    """打印任何传入的字符串"""
    print(s)
    return


# 调用函数
printMe("我要调用用户自定义函数!")
printMe("再次调用同一函数")

print("-----------------------------------------------")

""" global 和 nonlocal关键字 """

num = 1


def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)


fun1()

print(num)


def outer():
    num = 10

    def inner():
        nonlocal num  # nonlocal关键字声明
        num = 100
        print(num)

    inner()
    print(num)


outer()

print("-----------------------------------------------")

a = 10


def test():
    global a
    a = a + 1
    print(a)


test()

print("-----------------------------------------------")


# 可写函数说明
# def printinfo(age=35, name):  # 默认参数不在最后，会报错
def printinfo(name, age=35):  # 默认参数不在最后，会报错
    """打印任何传入的字符串"""
    print("名字: ", name)
    print("年龄: ", age)
    return


print("-----------------------------------------------")


def func(country, province, **kwargs):
    print(country, province, kwargs)


func("China", "Sichuan", city="Chengdu", section="JingJiang")

dir(builtins)