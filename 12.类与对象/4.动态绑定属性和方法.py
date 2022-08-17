# -*- coding = utf-8 -*-
# Time: 2022/4/20 17:00
# Author: Mr Wu
# File: 4.动态绑定属性和方法.py
# Software: PyCharm

# Python是动态语言，在创建对象之后，可以动态地绑定属性和方法
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+'在吃饭')

stu1=Student('张三',20)
stu2=Student('李四',30)
# 为stu2动态绑定性别属性
stu2.gender='女'
print(stu1.name,stu1.age)
print(stu2.name,stu2.age,stu2.gender)

stu1.eat()
stu2.eat()
# 为stu1动态绑定方法
def show():
    print('定义在类之外的，称函数')
stu1.show=show
stu1.show()
