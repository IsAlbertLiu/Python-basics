# 请编写一个程序，实现删除列表重复元素的功能。
# 【输入形式】输入一行数据，以空格作为间隔。
# 【输出形式】输出删除重复元素的一行数字，以空格作为间隔。
# 【样例输入】5 12 9 12 6 23 9 5
# 【样例输出】5 12 9 6 23






arr = input()
new_arr = arr.split(' ')
no_repeat_arr = []
str = ''
# 遍历
for i in new_arr:
    if i not in no_repeat_arr:
        no_repeat_arr.append(i)

# print(new_arr)
# print(no_repeat_arr)
for i in no_repeat_arr:
    str += i+' '
print(str)