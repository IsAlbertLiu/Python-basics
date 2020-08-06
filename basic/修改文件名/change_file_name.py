import os

# path = r'E:\大前端\阶段一'
path = r'E:\大前端\阶段一\02.开发环境搭建\第3章编辑器WebstormsSCode'
files = os.listdir(path)
print(files)
remove_brand = '【daobanke.com】'
# remove = '.e4[更多IT资源访问daobanke.com]【daobanke.com】'
# remove = '.e4[更多IT资源访问daobanke.com]'
remove ='.e4更多IT资源访问daobanke.com【daobanke.com】'
sum = 0
new_file = ''
new_files = []

# 处理一个路径中的文件名
for file in files:
    new_file = file.replace(' ', '')
    new_file = new_file.replace(remove,'')
    os.rename(path + '/' + file, path + '/' + str(new_file))
    print(type(new_file),new_file)


# 处理文件夹名
# for file in files:
#     new_file = file.replace(remove_brand, '')
#     os.rename(path + '/' + file, path + '/' + str(new_file))
#     print(type(new_file), new_file)

# # 获取每个文件夹所处的路径
# paths = []
# print(type(len(files)))
# # E:\大前端\阶段一\01.认识大前端【daobanke.com】\第1章 课程介绍
# for index in range(len(files)):
#     print(index)
#     # 向路径list中添加一个路径
#     paths.append(path + '\\' + files[index])
#
# print(paths)
#
# # 获取每个文件夹中的文件名
# for finder in range(len(paths)):
#     files = os.listdir(paths[finder])
#     print(files)
