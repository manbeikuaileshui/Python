# -*- coding = utf-8 -*-
# Time: 2022/4/19 20:43
# Author: Mr Wu
# File: 2.文件的创建.py
# Software: PyCharm

# 对象的创建
# 1.对象的创建又称为类的实例化
# 2.语法：实例名=类名()
# 3.例子：stu=Student()
# # 创建Student类的实例对象
# stu=Student('Jack',20)
# print(stu,name)  # 实例属性
# print(stu,age)  # 实例属性
# stu.info()  # 实例方法
# 4.意义：有了实例，就可以调用类中的内容

class Student:

    native_pace='吉林'

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):
        print('学生在吃饭')

    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰，所以我是静态方法')

    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')

# 创建Student类的对象
stu1=Student('张三',20)
stu1.eat()  # 对象名.方法名()
print(stu1.name)
print(stu1.age)

print('------------------------------')
Student.eat(stu1)  # 37行与42行代码功能相同，都是调用Student中的eat方法
                   # 类名.方法名(类的对象)-->实际上就是方法定义处的self
