# -*- coding = utf-8 -*-
# Time: 2022/4/1 15:45
# Author: Mr Wu
# File: 3.注意事项.py
# Software: PyCharm

# 1.定义的元组，其数据不可以改变
t = (1,2,3,4,5)
print(t)
# t[1] = 6  # 元组的数据不可修改，除非它本身是可以修改的
# print(t)
print('-'*40)

# 2.可查询元组元素、切片操作、len()、sorted()、in、max()等方法
t = (1,2,3,6,4,5,7)
print(t[2]) # 查询元素
print('-'*40)

print(t,id(t))
print(t[2:5:2],id(t[2:5:2])) # 切片操作，产生新的元组
print(t,id(t))
print('-'*40)

print(len(t)) # 求元组的长度
print('-'*40)

print(t,id(t))
print(sorted(t),id(sorted(t))) # 为元组排升序，产生新的元组
print(t,id(t))
print(sorted(t,reverse=True),id(sorted(t,reverse=True))) # 为元组排降序，产生新的元组
print(t,id(t))
print(sorted(t,reverse=False),id(sorted(t,reverse=False))) # 为元组排升序，产生新的元组
print(t,id(t))
print('-'*40)

print(4 in t) # in
print(4 not in t)
print('-'*40)

print(max(t)) # 求元组中的最大元素
print(min(t)) # 求元组中的最小元素
print('-'*40)
