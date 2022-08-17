# -*- coding = utf-8 -*-
# Time: 2022/3/25 18:11
# Author: Mr Wu
# File: 5.添加.py
# Software: PyCharm

#    列表元素的增加操作  都在原列表中操作
lst = [10,20,30]

# 1.append():在列表的末尾添加一个元素
print('添加元素之前：',lst)
lst.append(40)
print('添加元素之后：',lst)

print('添加元素之前：',lst)
lst.append([50,60])  #将列表[50,60]当做一个元素添加到列表的末尾
print('添加元素之后：',lst)

print('-'*40)
# 2.extend():在列表的末尾至少添加一个元素  在原列表中操作
print('添加元素之前：',lst)
lst.extend([70,80])
print('添加元素之后：',lst)

print('-'*40)
# 3.insert():在列表的任意位置添加一个元素  在原列表中操作
print('添加元素之前：',lst)
lst.insert(0,1)  #在下标为0的地方插入1
print('添加元素之后：',lst)

print('-'*40)
# 4.切片：在列表的任意位置添加至少一个元素  在原列表中操作
print('添加元素之前：',lst)
lst[1:6]=['hello','world']  #实际就是把选择的位置之后的元素都替换成自己想要的元素（替换的元素个数可以不相等）
print('添加元素之后：',lst)