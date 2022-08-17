# -*- coding = utf-8 -*-
# Time: 2022/3/23 22:22
# Author: Mr Wu
# File: 2.查询.py
# Software: PyCharm

#                             列表的查询操作
a = ['hello',98.98,[11,'world'],98,98,True]
#           1.index():获取列表中指定元素的索引
print(a.index(98))          #<1> 如果列表中存在N个相同元素，只返回相同元素中的第一个元素的索引
print(a.index(98.98,1,5))   #<2> 在指定的start和stop之间进行查找，即在下标为1-4之间查找，不包括5
# print(a.index('python'))  #<3> 如果查询的元素在列表中不存在，则会抛出ValueError

#     2.获取列表中的单个元素
print(a[3])     #<1> 正向索引从0到N-1  举例：lst[0]
print(a[-3])    #<2> 逆向索引从-N到-1  举例：lst[-N]
# print(a[10])  #<3> 指定索引不存在，抛出IndeError

#     3，获取列表中的多个元素
# 语法格式：列表名[start:stop:step]
# 切片操作  在拷贝的列表中操作
lst = [10,20,30,40,50,60,70,80]
# <1>切片结果：原列表片段的拷贝
print('原列表：',lst,id(lst))
print('切的片段：',lst[1:6:1],id(lst[1:6:1]))
# <2>切片范围：[start,stop]  不包括stop
print(lst[1:3])
# <3>step默认为1：简写[start:stop]
print(lst[1:6])  #默认步长为1
print(lst[1:6:])
# <4>step为正数：
# ①[:stop:step]:切片的第一个元素默认是列表的第一个元素（从start开始往后计算）
print(lst[:6:2])
# ②[start::step]:切片的最后一个元素默认是列表的最后一个元素（从start开始往后计算）
print(lst[1::2])  #包括最后一个元素
# <5>step为负数：
# ①[:stop:step]:切片的第一个元素默认是列表的最后一个元素（从start开始往前计算）
print(lst[::-1])
print(lst[7::-1])
# ②[start::step]:切片的最后一个元素默认是列表的第一个元素（从start开始往前计算）
print(lst[6:0:-2])