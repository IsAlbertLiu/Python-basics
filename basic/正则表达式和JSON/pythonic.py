# case = 10
#
#
# def get_monday():
#     return 'Monday'
#
#
# def unknown():
#     return 'unknown'
#
#
# lot = {
#     1: get_monday,
#     2: 'Tuesday',
#     3: 'Wednesday'
# }
#
# r = lot.get(case, unknown)()
# print(r)

# 列表推导式

a = [1,2,3,4,5,6]
b = [i*i for i in a] #[1, 4, 9, 16, 25, 36]
# b = [i**2 for i in a]
# 有条件的删选出要进行运算的数字
b = [i**2 for i in a if i>=5]
print(b)    #[1, 4, 9, 16, 25, 36]


