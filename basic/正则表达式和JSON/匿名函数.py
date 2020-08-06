# def add(x, y):
#     return x + y
#
#
# print(add(1, 2))  # 3
#
# f = lambda x, y: x + y
#
# print(f(4, 5))  # 9

# x = 1
# y = 2
# r = x if x > y else y
# print(r)    # 2


# list_x = [1, 2, 3, 4, 5, 6, 7, 8]
# list_y = [1, 2, 3, 4, 5, 6, 7, 8]
#
# r = map(lambda x, y: x * x + y, list_x, list_y)
# print(list(r))  # [2, 6, 12, 20, 30, 42, 56, 72]


# from functools import reduce
#
# list_x = ['a', 'b', 'c', 'd', 'e', 'f']
#
# r = reduce(lambda x, y: x + y, list_x, 'aaa,')
# print(r)  # aaa,abcdef


list_x = [1,0,1,0,1,0]
r = filter(lambda x:True if x==1 else False,list_x)
print(list(r))  # [1, 1, 1]









