
import os
# path = r"E:\大前端\阶段一\01.认识大前端【daobanke.com】\第1章 课程介绍" #文件夹目录
path = r"C:/Users/stayfoolish/Desktop/test" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
replace = []
for file in files:
    replace.append(file)
# A-01-1-3 如何学习本课程.e4[更多IT资源访问daobanke.com] 【daobanke.com】.mp4
# A-01-1-4 寻求帮助&课程资源&课程更新.e4[更多IT资源访问daobanke.com]【daobanke.com】.mp4

# s = []
# for file in files: #遍历文件夹
#      if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
#           f = open(path+"/"+file) #打开文件
#           iter_f = iter(f) #创建迭代器
#           str = ""
#           for line in iter_f: #遍历文件，一行行遍历，读取文本
#               str = str + line
#           s.append(str) #每个文件的文本存到list中
# print(s) #打印结果
file_name=1
for file in files:
    os.rename(path+'/'+file,path+'/'+str(file_name)+'.txt')
    file_name+=1

