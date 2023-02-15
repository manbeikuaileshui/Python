# -*- coding = utf-8 -*-
# Time: 2022/4/21 15:43
# Author: Mr Wu
# File: 10.特殊方法和特殊属性.py
# Software: PyCharm

# 特殊属性：__dict__,获得类对象或实例对象所绑定的所有属性和方法的字典
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
class D(A):
    pass
# 创建C类的对象
x=C('Jack',20)
print(x.__dict__)  # 实例对象的属性字典
print(C.__dict__)  # 类对象的属性字典
print('----------------------------')
print(x.__class__) # <class '__main__.C'> 输出了对象所属的类
print(C.__bases__) # C类的父类类型的元素
print(C.__base__) # 类的基类，即输出离C类最近的父类
print(C.__mro__) # 查看类的层次结构
print(A.__subclasses__()) # 子类的列表，即查看子类
print('--------------------------------------')

# 特殊方法：
# 1.__len__():通过重写__len__()方法，让内置函数len()的参数可以是自定义类型
lst=[11,22,33,44]
print(len(lst))
print(lst.__len__())
class Student:
    def __init__(self,name):
        self.name=name
    def __len__(self):
        return len(self.name)
stu1=Student('张三')
stu2=Student('李四')
print(len(stu1))
print('-------------------')

# 2.__add__():通过重写__add__()方法，可使用自定义对象具有“+”功能
a=20
b=100
c=a+b
print(c) # 两个整数类型的对象的相加操作
d=a.__add__(b)
print(d)

class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self,other):
        return self.name+other.name
stu1=Student('张三')
stu2=Student('李四')
s=stu1+stu2  # 实现了两个对象的加法运算（因为在Student类中，编写__add__()特殊的方法）
print(s)
s1=stu1.__add__(stu2)
print(s1)
print('____________________________________')

# 3.__new__():用于创建对象
# 4.__init__():对创建的对象初始化
class Person(object):

    def __new__(cls,*args,**kwargs):
        print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))
        obj=super().__new__(cls)
        print('创建的对象的id为：{0}'.format(id(obj)))
        return obj

    def __init__(self,name,age):
        print('__init__被调用了，self的id值为：{0}'.format(id(self)))
        self.name=name
        self.age=age

print('object这个类对象的id为：{0}'.format(id(object)))
print('Person这个类对象的id为：{0}'.format(id(Person)))

# 创建Person类的实例对象
p1=Person('张三',20)
print('p1这个Person类的实例对象的id：{0}'.format(id(p1)))