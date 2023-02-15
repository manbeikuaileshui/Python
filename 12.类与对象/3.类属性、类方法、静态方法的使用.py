# -*- coding = utf-8 -*-
# Time: 2022/4/20 16:40
# Author: Mr Wu
# File: 3.类属性、类方法、静态方法的使用.py
# Software: PyCharm

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

# 1.类属性：类中方法外的变量称为类属性，被该类的所有对象所共享
print(Student.native_pace)
stu1=Student('张三',20)
stu2=Student('李四',30)
print(stu1.native_pace)
print(stu2.native_pace)
Student.native_pace='天津'
print(stu1.native_pace)
print(stu2.native_pace)

# 2.类方法：使用@classmethod修饰的方法，使用类名直接访问的方法
Student.cm()

# 3.静态方法：使用@staticmethod修饰的方法，使用类名直接访问的方法
Student.method()