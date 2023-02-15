# -*- coding = utf-8 -*-
# Time: 2022/3/28 19:33
# Author: Mr Wu
# File: 5.集合间的关系.py
# Software: PyCharm

# 1.两个集合是否相等  (元素相同就相等)
s1 = {10,20,30,40}
s2 = {40,30,20,10}
#   <1>可以使用运算符==或！=进行判断
print(s1 == s2) #True
print(s1 != s2) #False
print('-'*40)

# 2.一个集合是否是另一个集合的子集
s1 = {10,20,30,40,50,60}
s2 = {10,20,30,40}
s3 = {10,20,90}
s4 = {50,60,70}
#  调用方法issubset进行判断
print(s2.issubset(s1)) #s2是s1的子集
print(s3.issubset(s1)) #s3不是s1的子集
print('-'*40)

# 3.一个集合是否是另一个集合的超集  (A是B的子集，B就是A的超集)
#  调用方法issuperset进行判断
print(s1.issuperset(s2)) #s1是s2的超集
print(s1.issuperset(s3)) #s1不是s3的超集
print('-'*40)

# 4.两个集合是否没有交集
#   调用方法isdisjoint进行判断
print(s2.isdisjoint(s3)) #s2与s3有交集 False
print(s2.isdisjoint(s4)) #s2与s4没有交集 True
