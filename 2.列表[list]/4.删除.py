# -*- coding = utf-8 -*-
# Time: 2022/3/25 17:15
# Author: Mr Wu
# File: 4.删除.py
# Software: PyCharm

#      列表元素的删除操作
lst = [10,20,30,40,50,60,30]

# 1. 列表名.remove(元素)
# ①一次删除一个元素 ②重复元素只删除第一个 ③元素不存在抛出ValueError
print('删除元素之前：',lst)
lst.remove(30)
print('删除元素之后：',lst)

print('-'*40)
# 2. 列表名.pop(下标)
# ①删除一个指定索引位置上的元素    ②指定索引不存在抛出IndexError
# ③未指定索引默认删除最后一个元素  ④返回值为删除的元素
print('删除元素之前：',lst)
lst.pop(1)
print('删除元素之后：',lst)
lst.pop()
print('删除元素之后：',lst)

print('-'*40)
# 3.切片：一次至少删除一个元素
print('删除元素之前：',lst)
lst[1:3]=[]  #实际是把[1:3]的元素替换成空
print('删除元素之后：',lst)

print('-'*40)
# del 变量名[下标]: 删除一个指定索引位置上的元素
print('删除元素之前：',lst)
del lst[0]
print('删除元素之后：',lst)

print('-'*40)
# 4.clear():清空列表
print('清空列表之前：',lst)
lst.clear()
print('清空列表之后：',lst)

print('-'*40)
# 5. del 变量名： 删除列表
print('清空列表之前：',lst)
del lst
print('删除列表之后：')
