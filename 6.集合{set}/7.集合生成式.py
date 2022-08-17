# -*- coding = utf-8 -*-
# Time: 2022/3/28 20:35
# Author: Mr Wu
# File: 7.集合生成式.py
# Software: PyCharm

# 集合生成式
# {i*i for i in range(1,10)}
# i*i:表示集合元素的表达式    i:自定义变量    range(1,10):可迭代对象
s = [i for i in range(0,10)]
print(s)
s = {i for i in range(0,10)}
print(s)
s = {i*2 for i in range(0,10)}
print(s)
s = {i*i for i in range(0,10)}
print(s)
s={i for i in "python"}
print(s)
