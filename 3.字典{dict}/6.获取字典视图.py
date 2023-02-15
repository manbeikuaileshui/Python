# -*- coding = utf-8 -*-
# Time: 2022/3/26 21:01
# Author: Mr Wu
# File: 6.获取字典视图.py
# Software: PyCharm

# 获取字典视图的方法
scores = {'张三':100,'李四':98,'王五':45}
# 1.keys():获取字典中所有的key
keys = scores.keys()
print(keys,type(keys))
print(list(keys)) # 将所有的key组成的视图转成列表

# 2.values():获取字典中所有value
values = scores.values()
print((values,type(values)))
print(list(values)) # 将所有的value组成的视图转成列表

# 3.items():获取字典中所有key,value对
items = scores.items()
print(items,type(items))
print(list(items)) # 转换之后的列表元素是由元组组成的