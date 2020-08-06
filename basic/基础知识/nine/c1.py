# 类 对象
# 类 实例化
# 类最基本的作用，封装


class Student():
    # 类变量
    name = 'liuliu'
    age = 10

    def __init__(self,name,age):
        # 实例变量
        # self.name = name
        # self.age = age
        #
        print(name)
        print(self.name)
        print(age)

    def print_file(self):
        print("name: " + self.name)
        print("age: " + str(self.age))


student1 = Student('石敢当',18)
# student2 = Student('刘一手',28)

# 实例下面的属性，首先访问的是类变量。
# 其次是访问的是构造函数里面的实例变量。
# 如果只是定义了构造函数，却没有正确的定义实例变量，属性访问的仍然是类变量
print(student1.name)
# print(student2.name)