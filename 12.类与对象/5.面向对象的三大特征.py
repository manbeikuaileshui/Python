# -*- coding = utf-8 -*-
# Time: 2022/4/20 22:57
# Author: Mr Wu
# File: 5.面向对象的三大特征.py
# Software: PyCharm

'''
面向对象的三大特征：
1. 封装：提高程序的安全性
   <1> 将数据（属性）和行为（方法）包装到类对象中。在方法内部对属性进行操作，在类对象的外部调用方法。
       这样，无需关心方法内部的具体实现细节，从而降低了复杂度。
   <2> 在Python中没有专门的修饰符用于属性的私有，如果该属性不希望在类对象外部被访问，前边使用两个“_”
2. 继承：提高代码的复用性
3. 多态：提高程序的可扩展性和可维护性
'''
class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age  # 年龄不希望在类的外部使用，所以加了两个__
    def show(self):
        print(self.name,self.__age)
stu=Student('张三',20)
stu.show()
# 在类的外部使用name与age
print(stu.name)
# print(stu.__age)  # 加了两个'_',不能再类的外部使用
# 强行访问
print(dir(stu))
print(stu._Student__age)  # 在类的外部可以通过  _Student__age  进行访问