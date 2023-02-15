# -*- coding = utf-8 -*-
# Time: 2022/4/21 15:10
# Author: Mr Wu
# File: 9.多态的实现.py
# Software: PyCharm

'''
多态：
简单地说，多态就是“具有多种形态”，它指的是：即便不知道一个变量所引用的对象到底是什么类型，仍然可以通过这个变量
调用方法，在运行过程中根据变量所引用对象的类型，动态决定调用那个对象中的方法
'''
class Animal:
    def eat(self):
        print('动物会吃...')
class Dog(Animal):
    def eat(self):
        print('狗吃屎...')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼...')
class Person:
    def eat(self):
        print('人吃五谷杂粮...')
# 定义一个函数
def fun(obj):
    obj.eat()
# 开始调用函数
fun(Dog())
fun(Cat())
fun(Animal())
print('------------------------------')
fun(Person())

'''
静态语言与动态语言
静态语言和动态语言关于多态的区别：
1.静态语言实现多态的三个必要条件：
  <1> 继承
  <2> 方法重写 
  <3> 父类引用指向子类对象
2.动态语言的多态崇尚“鸭子类型”当看到一只鸟走起来像鸭子、游泳起来像鸭子、走起来也想鸭子，那么这只鸟就可以被称为
  鸭子。在鸭子类型中，不需要关心对象是什么类型，到底是不是鸭子，只关心对象的行为。
'''