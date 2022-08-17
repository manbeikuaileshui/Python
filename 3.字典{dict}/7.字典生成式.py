# -*- coding = utf-8 -*-
# Time: 2022/3/26 21:39
# Author: Mr Wu
# File: 7.字典生成式.py
# Software: PyCharm

# 字典生成式

# 内置函zip()
# 用于将可迭代的对象作为参数，将对象中对应的元素打包成一个元组，然后返回由这些元组组成的列表

# {item.upper():price for item, price in zip(items,prices)}
# item.upper():表示字典key的表达式   price：表示字典value的表达式   item：自定义表示key的变量
# price：自定义表示value的变量   (items,prices):可迭代对象

# 列：将第一个列表的元素作为键，第二个列表的元素作为值，创建字典
items = ['Fruits','Books','Others']
prices = [96,78,85]
lst = zip(items,prices)
print(list(lst))
d = {item:price for item, price in zip(items,prices)}
print(d)


