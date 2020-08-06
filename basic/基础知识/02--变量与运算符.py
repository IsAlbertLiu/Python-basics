# ------------变量
A = [1,2,3]

# --变量名的命名规则：
# 字母，数字，下划线，首字母不能是数字,系统保留的关键字，
# 变量名区分大小写
# 变量本身是没有类型限制的

# --变量的交换
a = 1
b = a
a = 3
print(a)    # 3
print(b)    # 1
x = True
y = x
x =False
print(x)  # False
print(y)  # True
print(type(x))
# --当赋的值是列表的时候，发生了变化
a = [1,2,3,4,5]
b = a
a[0] = '1'
print(a)    # ['1', 2, 3, 4, 5]
print(b)    # ['1', 2, 3, 4, 5]

# --int str tuple bool (不可变) 值类型  list set dict（可变）引用类型

# --获取某个变量的内存地址
c = 'hello'
print(id(c))    # 25743424
print(c[0])  # h
# c[0] = '1' # 报错，str是不可变的值类型，不可以更改里面的某个字符


# --元组，列表的一些操作
# tuple是值类型，不可以更改里面的值
s = (1,2,3)
# s[1] ='2' # 报错，不可更改
print(s)

c = [1,2,3]
print(c)    # [1,2,3]
c[1] = 4  # 可以更改

s = (1,2,[1,2,3])
# 元组可以被重新定义
print(s)  # (1, 2, [1, 2, 3])
s[2][2]=1
print(s)  # (1, 2, [1, 2, 1]) 元组里面的列表可以被改变

# -----------运算符

# python里面没有自加，自减运算符  -- ++

b=1
b+=b>=1
# >= 的优先级高，先判断 b >=1,结果为 True
# True 对应的值是1，最后就是 b+= 1  结果是2
print(b)    # 2

# --字符串的比较,比较的是ASCII码
print('a'>'b')  # False
# --多个字符串的比较，也是标胶ASCII码，从第一位开始判断
print('abc'<'abd')  # True
# --tuple的比较
print((1,2,3)<(1,2,4))  # True
# --列表的比较
print([1,2,3]>[1,2,5])  # False


# --------------逻辑运算符
# and or not --对应着其他编程语言里面的 && || !

# --and
print(1 and 0)  # 0
print(0 and 1)  # 0

print(2 and 1)  # 1
print(1 and 2)  # 2
print('-------------')
# and的返回结果逻辑，先判断第一个数是True还是False，
# 如果第一个数是True，继续判断第二个数，若果第二个数也是True，就返回第二个数
print(1 and 2)  # 2
# 如果第一个数是True，继续判断第二个数，若果第二个数是False，就返回第二个数
print(1 and 0)  # 0

# 如果第一个数是False，继续判断第二个数，若果第二个数是True，就返回第一个数
print(0 and 1)  # 0
# 如果第一个数是False，继续判断第二个数，若果第二个数是False，就返回第一个数
print(0 and False)  # 0

print('-----------')
# --or
# 如果第一个数是False，就返回第二个数
print(0 or 1)   # 1
# 如果第一个数是True，就返回第一个数
print(1 or 0)   # 1
# 如果第二个数是True，就返回第一个数
print(9 or 2)   # 9


# ------------------成员运算符 in / not in
# 返回结果是True 和 False
i = 1
print(i in [1,2,3])     # True
print(i not in [1,2,3])  # False
o = 'o'
print(o in 'hello')     # True
print(o not in 'hello')     # False

# 判断是否在元组里面
print(i in (1,2,3))     # True
# 判断是否在集合 set 里面
print(i in {1,2,3})     # True

# 判断是否在字典里面，判断某个值是否在字典里面，是去判断是否有对应的key
l = 'b'
print(10 in {'b':10})    # False
print(l in {'b':10})    # True


# --身份运算符（is / not is） is是比较两个变量的身份是否相等
# is 比较的是两个变量内存地址是否相等
# ==
k = 1
p = 9

print(k is p)  # False

# --is 和 == 的比较

k = 1
p = 1.0
print(k == p)   # True
print(k is p)   # False

print('------------')
# 问题：
a = {1,2,3}
b = {2,1,3}
print(a)
print(b)
print(a == b)   # True
print(a is b)   # False
# ---------原因：集合是无顺序的
print(id(a))
print(id(b))

g = (1,2,3)
e = (2,1,3)
print(g)
print(e)
print(g == e)   # False
print(g is e)   # False

# --------
print(a == b) # 是对值的判断
print(a is b) # 是对内存地址 id 的判断
# 类型 type 判断
# 对象 三个特征 一切都是对象

# --Python里面去判断一个变量的数据类型 isinstance(变量,变量类型)
w = 10
print(isinstance(w,str))    # False
print(isinstance(w,(str,int,float)))    # True


# 对象的三个特征  id（内存地址） value（值） type（类型）

# --------------- 位运算符
# & （按位与） |（按位或） ^（按位异或） ~（按位取反）  <<（左移动）  >>（右移动）
# --把数字当作二进制进行运算

print(1 & 2) # 0













