# -*- coding = utf-8 -*-
# Time: 2022/3/26 20:50
# Author: Mr Wu
# File: 4.字典元素的增加、删除、修改.py
# Software: PyCharm

scores = {'张三':100,'李四':98,'王五':45}

# 字典元素的新增
scores = {'张三':100,'李四':98,'王五':45}
scores['陈六']=98 # 新增元素
print(scores)
print('-'*40)

# 字典元素的修改
scores['陈六']=100 # 修改元素
print(scores)
print('-'*40)

# 字典元素的删除
# 1.pop():指定键名删除这个元素，返回值为删除的元素的值，不给参数会报错
print(scores.pop('张三'))
print(scores)
# print(d.pop())  # 报错
print(scores.pop('赵六','没有这个键名'))# '没有这个键名'是在查找'麻七'所对应的value不存在时，提供的一个默认值
print('-'*40)

# 2.popitem():随机删除一个元素，返回值为被删除的元素
print(scores.popitem())
print(scores)
print('-'*40)

# 3.删除指定的 key-value对
del scores['李四']
print(scores)
print('-'*40)

# 4.清空字典的元素
scores.clear()
print(scores)
print('-'*40)

# 5.删除整个字典
del(scores)
# print(scores) # 字典已删除，直接报错


