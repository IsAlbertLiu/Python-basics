# ---------------------数据的基本类型
# 1.Number  Bool  String
# 1.Number--> int float bool
# 有整数型，浮点数型，
print(type(1))  # --><class 'int'>
print(type(1.0))  # --><class 'float'>


# 重要的点：Bool类型
# Bool类型的表示有True False 注意：都是大写开头

# ---------------------Bool值的判断
# --对数值的bool值判断：0 的bool值是False 其他数值都是True
print(bool(1))  # True
print(bool(1.19))  # True
print(bool(-1.19))  # True
print(bool(0))  # False
# 非空字符串的bool值是True，空字符串的bool值是False
print(bool("123"))  # True
print(bool(""))  # False

# ---------------------数据的运算
# 常见的运算有 + - * /  **（平方） //(取整)

print(1+2)  # 3
print(1-2)  # -1
print(2*4)  # 8
print(2**4)  # 16
print(2/4)   # 0.5
print(2//4)  # 0
print(2%4)  # 2


# ---------------------字符串
# 字符串的表示方式有三种：
# 1.单引号 '' 2.双引号 ""
# 3.三个引号 ''' ''' 或者""" """
print('hello world')
print("hello world")
# 当同时需要使用单引号或者双引号的时候。需要成对出现。对内容进行包裹
print("let's go")
print('''
hello 
world
''')
# 三个引号的作用是进行多行输出

# ----------------------转义字符
# \n \t \'
print('\n hello world')
# --示例：输出文件路劲
# 会当作转义字符进行输出
print('c:\nor\nt')
# 正常输出
print('c:\\nor\\nt')
# 在前面加上r,会把这个字符串当作原始字符串进行正常输出。r可以小写，也可以大写
print(r'c:\nor\nt')
print(R'c:\nor\nt')

# -----------------------对字符串进行操作
# 1.字符串的加法:拼接字符串
print("world"+"hello")
# 2.字符串的乘法：重复输出字符串
print("hello"*3)
# 3.获取字符串中的某一字符，
# --获取第一个字符，字符串的下标。从0开始计数
print("hello"[0])
# --最后一个字符，从-1开始计数
print("hello"[-1])
# 4.获取字符串的某一串字符
print("hello world"[0:3])  # -->hel
print("hello world"[0:-1])  # -->hello worl 步长的概念，
# 实例：通过两种不同的方式获取 world
print("hello world"[6:])  # --> world
# 负数开头的意思是我们从后面开始截取
print("hello world"[-5:])  # --> world
