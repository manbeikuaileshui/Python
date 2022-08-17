# -*- coding = utf-8 -*-
# Time: 2022/4/7 12:03
# Author: Mr Wu
# File: 1.函数的创建.py
# Software: PyCharm

# 函数的创建
"""
def 函数名 ([输入参数]):
    函数体
    [return xxx]
"""
# 例：
def sum(a,b):
    c = a + b
    return c
# 函数的调用:函数名([实际参数])
num = sum(10,20)
print(num)