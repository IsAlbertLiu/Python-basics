# 3str3rAa*bRb
import re

# s = input()
# # r = re.findall('\w',s)
# r = re.findall('[a-zA-Z]', s)
# print(r)


# a = 10
#
#
# def f():
#     # 此时a 会被Python认为是局部的变量，局部变量不会影响外部的变量
#     a = 20
#     def fn():
#         res = 3*a
#         return res
#     return fn
#
#
# f()
# print(a)

# x = 0
#


def value(x):
    result = x + 0
    def add():
        return result+x
    return add

b = value(10)
b()
























