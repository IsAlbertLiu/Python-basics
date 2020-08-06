# --------python函数
a = 1.238913
result = round(a,2)
print(result)   # 1.24 会进行4舍5入

# --------函数练习
# 1.实现两个数字的相加
# 2.打印输入的参数

def add(x,y):
    sum = x+y
    return sum
def print_code(code):
    print(code)
# 相加
b = add(1,2)
c = print_code('python')
print(b,c)
# 执行结果
# python
# 3 None
# --解释：
# 第一个python结果是为在定义print_code的时候，就在函数内部输出了print(),
# 所以在调用这个函数的时候就是输出一次
# 3 none 分别是print(b,c)输出的结果，3是函数add return的值
# none是因为函数print_code没有返回值，当用一个变量去接受这个函数的时候就会返回none


# ----一个函数输出多个值

def damage(skill1,skill2):
    damage1 = skill1*3
    damage2 = skill2*2+10
    return damage1,damage2

damages=damage(2,3)

print(damages)  # (6, 16)
# 当函数同时return多个数值的时候，python会将这些数值组成tuple
print(type(damages))    # <class 'tuple'>


# ------元组的解构
damage_skill1,damage_skill2 = damage(3,6)

print(damage_skill1,damage_skill2)  # 9 22

# 元组的解构 元组的简单定义方式
d = 4,5,6
print(type(d))  # <class 'tuple'>
a,b,c = d
# 此时我们输出a，b，c
print(a,b,c)# 4 5 6


# ----------函数的参数：python中形参有多少个对应的实参就要有多少个
# --1.简单传参
# def info(name,gender,age,school):
#     print('我是'+name)
#     print('我是'+gender+'生')
#     print('我今年'+age+'岁')
#     print('我在'+school+'上学')
#
# # 函数可以指定参数进行传参
# info('张三','男','10','光明小学')

# --2.固定参数传参
# def info(name,gender='男',age=10,school='光明小学'):
#     print('我是'+name)
#     print('我是'+gender+'生')
#     print('我今年'+str(age)+'岁')
#     print('我在'+school+'上学')
#
# # 函数可以指定参数进行传参
# info('李四')
# 我是李四
# 我是男生
# 我今年10岁
# 我在光明小学上学

# --3.对固定的参数进行修改
def info(name,gender='男',age=10,school='光明小学'):
    print('我是'+name)
    print('我是'+gender+'生')
    print('我今年'+str(age)+'岁')
    print('我在'+school+'上学')

# 函数可以指定参数进行传参
info('李四',age=13)
#
# 我是李四
# 我是男生
# 我今年13岁
# 我在光明小学上学