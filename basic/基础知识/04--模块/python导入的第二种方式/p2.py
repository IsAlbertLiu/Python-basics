# from module import a,def

# 从 p1 模块导入变量 a
# from p1 import a
#
# print(a)


from p1 import *
print(a)
# b 因为没有导入，所以会报错
print(b)    # NameError: name 'b' is not defined
print(c)

# 在你导入某个模块，去使用它的时候，python会自动执行  __init__.py文件
