# -*- coding = utf-8 -*-
# Time: 2022/4/21 14:04
# Author: Mr Wu
# File: 6.继承及其实现方法.py
# Software: PyCharm

"""
1.语法格式：class 子类类名(父类1，父类2......)
                 pass
2.如果一个类没有继承任何类，则默认继承object
3.Python支持多继承
4.定义子类时，必须在其构造函数中调用父类的构造函数
"""
class Person(object):  # Person继承object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no
class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear

stu=Student('张三',20,1001)
teacher=Teacher('李四',34,10)
stu.info()
teacher.info()

# 多继承
class A(object):
    pass
class B(object):
    pass
class C(A,B):
    pass

