# -*- coding = utf-8 -*-
# Time: 2022/4/8 22:23
# Author: Mr Wu
# File: 7.变量的作用域.py
# Software: PyCharm

# 变量的作用域
# 1.程序代码能访问该变量的区域
# 2.根据变量的有效范围可分为：
# <1> 局部变量：
#        在函数内定义并使用的变量，只在函数内部有效，局部变量使用global声明，这个变量就会变成全局变量
def fun(a,b):
    c=a+b
# c,就称为局部变量，因为c是在函数体内进行定义的变量。a,b函数的形参，作用范围也是函数内部，相当于局部变量
    print(c)
# print(c)  # 报错，因为a超出了起作用的范围(超出了作用域)
# print(c)  # 报错，因为c超出了起作用的范围(超出了作用域)
fun(10,20)

# <2> 全局变量：
#        函数体外定义的变量，可作用于函数内外
name = '杨老师'  # name的作用范围为函数内部和外部都可以使用-->称为全局变量
print(name)
def fun():
    print(name)
fun()

# <3> global：把局部变量变为全局变量
def fun():
    global age  # 把局部变量变为全局变量
    age = 20
    print(age)
fun()
print(age)
