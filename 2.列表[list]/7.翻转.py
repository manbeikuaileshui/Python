# -*- coding = utf-8 -*-
# Time: 2022/3/25 16:58
# Author: Mr Wu
# File: 7.翻转.py
# Software: PyCharm

# 列表翻转：
lst = [10,20,'hello','world']
# 1. list(reversed(变量名))
print('翻转前：',lst)
print('新列表：',list(reversed(lst)))  #产生新的列表
print('翻转后：',lst)

print('-'*40)

# 2. list.reversed()
print('翻转前：',lst)
print('新列表：',lst.reverse())  #没有产生新的列表，在原列表中直接翻转
print('翻转后：',lst)

print('-'*40)

# 3.
print('翻转前：',lst)
print('新列表：',lst[::-1])  #产生新的列表
print('翻转后：',lst)