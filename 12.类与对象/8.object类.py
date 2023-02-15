# -*- coding = utf-8 -*-
# Time: 2022/4/21 14:53
# Author: Mr Wu
# File: 8.object类.py
# Software: PyCharm

# 1.object类是所有类的父类，因此所有类都有object类的属性和方法。
# 2.内置函数dir()可以查看指定对象所有属性
# 3.Object有一个__str__()方法，用于返回一个对于“对象描述”，对应于内置函数str()经常用于print()方法，
#   帮我们查看对象信息，所以我们经常会对__str__()进行重写
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '我的名字是{0},今年{1}岁了'.format(self.name,self.age)
stu=Student('张三',20)
print(dir(stu))
print(stu)  # 默认会调用__str__()这样的方法

