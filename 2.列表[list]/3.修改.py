# -*- coding = utf-8 -*-
# Time: 2022/3/25 18:10
# Author: Mr Wu
# File: 3.修改.py
# Software: PyCharm

#      列表元素的修改操作
lst = [10,20,30,40]

# 1.为指定索引的元素赋予一个新值
print('修改前：',lst)
lst[3]=50
print('修改后：',lst)

# 2.为指定的切片赋予一个新值
print('修改前：',lst)
lst[1:3]=[50,60,70,80]  #实际是把选中位置的元素替换成想要的元素  两者个数可以不相等
print('修改后：',lst)