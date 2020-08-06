# 循环

# 循环语句
# while for

# CONDITION = True
#
# while CONDITION:
#     print('I am While') # 无限循环


# while还可以与else一起使用
counter = 1

while counter<10:
    counter+=1
    print(counter)
else:
    print('EOF')
# 递归的场景用到while比较多

# -------------for循环：主要是用来便利/循环 序列或者集合，字典
a = ['apple','orange','banana','grape']
for x in a:
    print(x)


# --多重循环
b = [['apple','orange','banana','grape'],(1,2,3)]
for x in b:
    for y in x:
        print(y)
else:
    print('EOF')

# for 与else搭配使用，else所配对的是最外层的for

# --break 和 continue

b = [['apple','orange','banana','grape'],(1,2,3)]
for x in b:
    for y in x:
        if y == 'orange':
            continue        # continue的作用是结束当前循环，并且执行下次循环
        print(y)
else:
    print('EOF')
b = [['apple','orange','banana','grape'],(1,2,3)]
for x in b:
    for y in x:
        if y == 'orange':
            break        # break的作用是结束当前循环，跳出当前循环体，
        print(y)
else:
    print('EOF')
# 此处使用了break，为什么else还会执行，是因为break结束的是第一个循环，而else对应的是最外面的循环，所以else仍然可以执行


# --------for range
for x in range(0,10):
    print(x)        # 0,1,2,3,4,5,6,7,8,9

# 让输出结果在一行显示
for x in range(1,10):
    print(x,end='')     # 123456789

print('---------')
# 让输出结果是从大到小的，
for x in range(10,0,-1):    # -1表示的是相隔几位显示。可以是-2等可改变的
    print(x,end='')  # 10987654321

print('-----------')
# 作业：打印出 c = [1,2,3,4,5,6]使中间相隔
c=[1,2,3,4,5,6,7,8]
for x in range(0,len(c),2):
    print(c[x],end=' | ')

print('-----------')
b = c[0:len(c):2]
print(b)









