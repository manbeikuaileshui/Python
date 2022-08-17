# -*- coding = utf-8 -*-
# Time: 2022/3/28 18:00
# Author: Mr Wu
# File: 1.集合的创建.py
# Software: PyCharm

# 集合的创建方式
# 1.直接{}
s = {'python','hello',98,98}
print(s,type(s)) # 集合中的元素不允许重复

print('-'*35)
# 2.使用内置函数set()
s = set(range(6))
print(s,type(s))
print(set([3,4,53,56]),type(set([3,4,53,56]))) # 列表-->集合
print(set((3,4,43,435)),type(set((3,4,43,435)))) # 元组-->集合
print(set('python'),type(set('python'))) # 字符串-->集合
print(set({124,3,4,4,5}),type(set({124,3,4,4,5}))) # 集合-->集合

print('-'*35)
# 3.创建空集合
#  <1> {}
s = {}
print(s,type(s)) # 不能这样创建集合，这样创建出来的是字典
#  <2>
s = set()
print(s,type(s)) # 正确创建集合的方式