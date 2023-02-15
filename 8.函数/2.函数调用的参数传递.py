# -*- coding = utf-8 -*-
# Time: 2022/4/7 12:15
# Author: Mr Wu
# File: 2.函数调用的参数传递.py
# Software: PyCharm

# 函数调用的参数传递
# 1.位置传参：根据形参对应的位置进行实参传递
def sum(a,b):
    sum(10,20)
# 10传给a,20传给b

# 2.关键字传参：根据形参名称进行实参传递
def sum(a,b):
    c = a + b
    return c
num = sum(b = 10, a = 20)
print(num)