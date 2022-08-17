# -*- coding = utf-8 -*-
# Time: 2022/3/22 22:00
# Author: Mr Wu
# File: range()常用函数.py
# Software: PyCharm

"""
range()函数的三种使用方式
1.range(stop):创建一个[0，stop）之间的整数系列，步长为1
2.range(start,stop):创建一个[start,stop)之间的整数系列，步长为1
3.range(start,stop,step):创建一个[start,stop)之间的整数序列，步长为step
返回值是一个迭代器对象
"""
# 方法 1
r = range(10)  #[0,1,2,3,4,5,6,7,8,9],默认从0开始，默认步长为1
print(r)  #range(0,10)
print(list(r))  #用于查看range对象中的整数序列   list:列表的意思
#  方法 2
r = range(1,10)  #指定了起始值，从1开始，到10结束（不包含10），默认不长为1
print(list(r))  #[1,2,3,4,5,6,7,8,9]
# 方法 3
r = range(1,10,2)  #指定了起始值，从1开始，到10结束（不包含10），指定了步长为2
print(list(r))  #[1,3,5,7,9]
# in 与 not in 判断整数序列中是否存在（不存在）指定的整数 例：
print(10 in r)  #False
print(9 in r)  #True
print(10 not in r)  #True
print(9 not in r)  #False
"""
range类型的优点：不管range对象表示的整数序列有多长，所有range对象占用的内存空间都是相同的，因为仅仅需要储存start，stop和Step，
               只有当用到range对象时，才会去计算序列中的相关元素
"""
print(range(1,20,1))  #[1,……,19]
print(range(1,101,1))  #[1,……,100]
# 上面两个在空间中所占的内存是一样大小的