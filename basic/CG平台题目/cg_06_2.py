# ASCII  小写字母 97-122  大写字母 65-90 3str3rAa*bRb
str = input()
new_str = []
only_char =[]
only_lower_char = ''
# 去重之后的小写数组
just_only_lower_char = []

# 将输入的字符串转换为数组
for i in range(len(str)):
    new_str.append(str[i])

# 去掉数组里面重复的字符串，且只保留大小写字母，之后，将大写字母转换为小写字母
for i in new_str:
    if ord(i)>=65 and ord(i)<=90 or ord(i)>=97 and ord(i)<=122:
        only_char.append(i.lower())

# 排序
for i in range(len(only_char)-1):
    for j in range(len(only_char)-i-1):
        if only_char[j]>only_char[j+1]:
            only_char[j],only_char[j+1] = only_char[j+1],only_char[j]

# 将只有小写字母的数组转换为字符串
for i in only_char:
    only_lower_char +=i

# 去重之后的数组
for i in only_char:
    if i not in just_only_lower_char:
        just_only_lower_char.append(i)


# print("just_only_lower_char",just_only_lower_char)

# print("new_str",new_str)
# print("only_lower_char",only_lower_char)

# 统计字母出现的次数
# print(only_lower_char.count('a'))
for i in  just_only_lower_char:
    print(i ,only_lower_char.count(i))



# print("only_char", only_char)


