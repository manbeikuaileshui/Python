# -*- coding = utf-8 -*-
# Time: 2022/4/19 19:36
# Author: Mr Wu
# File: 1.类的创建.py
# Software: PyCharm

# 1.创建类的语法：
class Student:  #Student为类的名称（类名），有一个或多个单词组成，每个单词的首字母大写，其余小写
    pass
# python中一切皆对象，那Student是对象吗？内存又开空间吗？
print(id(Student))  # 2557275792512
print(type(Student))  # <class 'type'>
print(Student)  # <class '__main__.Student'>

# 2.类的组成：类属性、实例方法、静态方法、类方法
class Student:  #Student为类的名称（类名），有一个或多个单词组成，每个单词的首字母大写，其余小写

    # 直接写在类里面的变量，称为类属性
    native_pace='吉林'

    # name,age为实例属性
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # 实例方法
    def eat(self):
        print('学生在吃饭')

    # 静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰，所以我是静态方法')

    # 类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')

#  在类之外定义的称为函数，在类之内定义的称为方法
def drink():
    print('喝水')