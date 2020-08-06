# def curve_pre():
#     a = 25
#     def curve(x):
#         return a*x*x
#     return curve
#
#
# a = 10
# f = curve_pre()
# print(f.__closure__)    # (<cell at 0x00393DC0: int object at 0x0F7CE930>,)
# print(f.__closure__[0].cell_contents)   # 25
# print(f(2))  # 100


# def f1():
#     a = 10
#     def f2():
#         a = 20
#         return a
#     return f2
#
#
# f = f1()
# print(f) # <function f1.<locals>.f2 at 0x01191538>
# print(f.__closure__)    # None


origin = 0


def move(step):
    global origin
    end_step = origin+step
    origin = end_step
    return end_step


print(move(3)) # 3
print(move(3)) # 6
print(origin) # 6


# def move(origin):
#     def add(step):
#         nonlocal origin
#         end_step = origin + step
#         origin = end_step
#         return end_step
#
#     return add
#
#
# f = move(origin)
# print(f(1))  # 1
# print(f(1))  # 2
# print(origin)
