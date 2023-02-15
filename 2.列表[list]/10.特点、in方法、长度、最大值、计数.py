# -*- coding = utf-8 -*-
# Time: 2022/3/25 18:14
# Author: Mr Wu
# File: 10.特点、in方法、长度、最大值、计数.py
# Software: PyCharm

#    列表的特点
# 1.列表元素按顺序有序排序
# 2.索引映射唯一一个数据
# 3.列表可以存储重复数据
# 4.任意数据类型混存
# 5.根据需要动态分配和回收内存

#      in方法
lst = [10,20,30,40,50,30]

# 1.判断指定元素在列表中是否存在
# <1>元素 in 列表名
print(10 in lst)
print(100 in lst)

# <2>元素 not in 列表名
print(10 not in lst)
print(100 not in lst)

# 求列表的长度：len(列表名)
print(len(lst))

# 求列表的最大值：max(列表名)
print(max(lst))

# 求在列表中某个元素出现的次数： 变量名.count(元素)
print(lst.count(30))