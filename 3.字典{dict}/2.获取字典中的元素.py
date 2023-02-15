# -*- coding = utf-8 -*-
# Time: 2022/3/26 20:20
# Author: Mr Wu
# File: 2.获取字典中的元素.py
# Software: PyCharm

# 字典中元素的获取
scores = {'张三':100,'李四':98,'王五':45}
# 1.字典名['键‘]
print(scores['张三'])
# print(scores['陈六']) # KeyError:'陈六'

# 2.字典名.get('键')
print(scores.get('张三'))
print(scores.get('陈六')) #None
print(scores.get('麻七','没有这个键名')) # '没有这个键名'是在查找'麻七'所对应的value不存在时，提供的一个默认值

# []取值与使用get()取值的区别
# 1.[]取值:如果字典中不存在指定的key，抛出keyError异常
# 2.get()方法取值:如果字典中不存在指定的key，并不会抛出keyError而是返回None，
#   可以通过参数设置默认的value，以便指定的key不存在时返回