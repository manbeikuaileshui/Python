# -*- coding = utf-8 -*-
# Time: 2022/3/25 18:28
# Author: Mr Wu
# File: 9.列表生成式.py
# Software: PyCharm

#              列表生成式
# 语法格式：[i*i for i in range(start,stop)]
# i*i:表示列表元素的表达式  i:自定义变量  range(start,stop):可迭代对象
# 注意事项：“表示列表元素的表达式中”通常包含自定义变量
lst = [i for i in range(1,10)]
print(lst)

lst = [i*i for i in range(1,10)]
print(lst)

lst = [i*2 for i in range(1,10)]
print(lst)