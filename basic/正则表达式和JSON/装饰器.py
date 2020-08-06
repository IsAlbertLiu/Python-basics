import time


def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)

    return wrapper


@decorator
def f1(func_name1, func_name2):
    print('This is a function ' + func_name1)
    print('This is a function ' + func_name2)


@decorator
def f2(func_name1, func_name2, **kw):
    print('This is a function ' + func_name2)
    print('This is a function ' + func_name2)
    print(kw)


f1('test_func1', 'test_func2')
# 1589290932.327042
# This is a function test_func1
# This is a function test_func2

f2('test_1', 'test_f2', a=1, b=2, c='123')
# 1589291278.1557262
# This is a function test_f2
# This is a function test_f2
# {'a': 1, 'b': 2, 'c': '123'}
