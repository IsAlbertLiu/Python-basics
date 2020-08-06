# 表达式
a = 1
b = 2
c = 2
print(not a or b + 2 == c)

#  -------------Python条件语句
# if 语句

account = 'qiyue'
password = '123456'

print('please input account')
user_account = input()

print('please input password')
user_password = input()

if account == user_account and password == user_password:
    print('success')
else:
    print('error')

#  pass  空语句/占位语句

# ------一个小问题
m = input()
if m ==1:
    print('apple')
else:
    if m ==2:
        print('orange')
    else:
        if  m ==3:
            print('banana')
        else:
            print('shopping')
