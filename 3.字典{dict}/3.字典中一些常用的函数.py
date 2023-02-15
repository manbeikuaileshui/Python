# -*- coding = utf-8 -*-
# Time: 2022/3/26 20:43
# Author: Mr Wu
# File: 3.字典中一些常用的函数.py
# Software: PyCharm

d = {'张三':100,'李四':98,'王五':45}

# 1.in 和 not in :判断指定的键在不在字典中
# <1> in：指定的key在字典中存在返回True
print('张三' in d)
# <2> not in：指定的key在字典中不存在返回True
print('Mary' not in d)
print('-'*40)

# 2.len():计算字典元素的个数
print(len(d))
print('-'*40)

# 3.max():取字典中的最大值   min():取字典中的最小值
print(max(d))
print(min(d))
print('张:',ord('张'))
print('王:',ord('王'))
print('李:',ord('李'))
print('-'*40)






