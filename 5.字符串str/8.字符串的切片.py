# -*- coding = utf-8 -*-
# Time: 2022/3/30 21:03
# Author: Mr Wu
# File: 8.字符串的切片.py
# Software: PyCharm

# 字符串的切片操作   与列表的切片操作类似
# 字符串是不可变类型，不具备增、删、改等操作，切片操作将产生新的对象
s = 'hello,python'
print(s,id(s)) # 原字符串
s1 = s[:5]
s2 = s[6:]
s3 = s[::2]
print(s1,id(s1)) # 切出的新字符串
print(s2,id(s2)) # 切出的新字符串
print(s3,id(s3)) # 切出的新字符串
print(s,id(s)) # 切片后，原字符串是否有变化
print(s1+' '+s2,id(s1+' '+s2)) # 字符串相加