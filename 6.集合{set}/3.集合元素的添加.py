# -*- coding = utf-8 -*-
# Time: 2022/3/28 18:39
# Author: Mr Wu
# File: 3.集合元素的添加.py
# Software: PyCharm

# 集合元素的新增操作
s  = {10}
# 1.调用add()方法，一次添加一个元素
s.add(70)
print(s)

# 2.调用update()方法至少添加一个元素
s.update([1,2])  #()里面可以放列表
print(s)
s.update((3,4))  #()里面可以放元组
print(s)
s.update({5,6})  #()里面可以放集合
print(s)
s.update('python')  #()里面可以放字符串
print(s)