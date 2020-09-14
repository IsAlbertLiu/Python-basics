def factor_sum(x):
    f_sum = 1
    for i in range(2,x):
        if x % i ==0:
            f_sum +=i
    return f_sum


def is_close(a):
    b = factor_sum(a)
    if factor_sum(b) == a and a<b:
        return True
    else:
        return False

num = int(input())
for n in range(num+1):
    if is_close(n):
        print(n,factor_sum(n))