import re

# a = 'C|C++|Java|C#|Python|Javascript'
#
# # print(a.index('Python') > -1)  # True
# # print('Python' in a)  # True
#
# r = re.findall('Python',a)
# # print(type(r),r)
# if len(r)>0:
#     print('字符串中包含Python')
# else:
#     print('字符串中不包含Python')

# a = 'C0C++7Java8C#9Python6Javascript'
#
# r = re.findall('\D',a)
# print(r)
# s = 'abc,acc,adc,aec,afc,ahc'
#
# r = re.findall('a[cf]c',s)
# m = re.findall('a[^cfd]c',s)
# n = re.findall('a[c-f]c',s)
# print(r)
# print(m)
# print(n)

# a = 'python 1111java&678p\nh\np'
#
# # r = re.findall('[0-9]',a)
# # r = re.findall('\w',a)
# # r = re.findall('\W',a)
# r = re.findall('\S',a)
# print(r)

# a = 'python 1111java&678p\nh\np'
#
# # r = re.findall('[a-z][a-z][a-z]',a)
# r = re.findall('[a-z]{3,6}?',a)
# print(r)

# a ='pytho0python1pythonn2'
#
# r = re.findall('python?',a)
# print(r)

# qq = '1000000001'
# # 4-8
# r = re.findall('^000',qq)
# print(r)

# a = 'PythonPythonPythonPythonPythonPython'
# r = re.findall('Python{3}JS',a)
# print(r)

# lanuage = 'PythonC#JavaC#PHPC#'
# r = re.sub('C#', 'GO', lanuage, 0)
# m = re.sub('C#', 'GO', lanuage, 1)
# print(r)
# print(m)


# language = 'PythonC#JavaC#PHPC#'
# # 因为字符串是不可更改的，所以此处使用新的变量进行接受
# language = language.replace('C#','GO')
# print(language)

# language = 'PythonC#JavaC#PHPC#'
#
#
# def convert(value):
#     matched = value.group()
#     return '!!' + matched + '!!'
#
#
# r = re.sub('C#', convert, language)
# print(r)

# s = 'A8C3721D86'
#
#
# def convert(value):
#     matched = value.group()
#     if int(matched) >= 6:
#         return '9'
#     else:
#         return '0'
#
#
# r = re.sub('\d', convert, s)
# print(r)

# s = 'A83C72D1D8E67'
#
# r = re.match('\D',s)
# print(r.group())
# r1 = re.search('\D',s)
# print(r1.group())

# s = 'life is short,i use python'
# r = re.search('(life.*python)',s)
# r1 = re.search('life.*python',s)
# print(r)    # <re.Match object; span=(0, 26), match='life is short,i use python'>
# print(r1)    # <re.Match object; span=(0, 26), match='life is short,i use python'>
# print(r.group())    #life is short,i use python
# print(r1.group())    #life is short,i use python

s = 'life is short,i use python，i love python'
r = re.search('life(.*)python(.*)python',s)
# group(0)是完整的匹配，包含查询参数括号外面的。
# print(r.group(0))  # life is short,i use python，i love python
# print(r.group(1))  # is short,i use
# print(r.group(2))  # ，i love
print(r.group(0,1,2))  # ('life is short,i use python，i love python', ' is short,i use ', '，i love ')


# s = 'life is short,i use python'
#
# r = re.findall('life(.*)python',s)
# print(r)    # [' is short,i use ']





