# -*- coding = utf-8 -*-
# Time: 2022/3/26 20:09
# Author: Mr Wu
# File: 1.字典的创建.py
# Software: PyCharm

# 字典的创建方式
# 1.使用：{}
scores = {'张三':100,'李四':98,'王五':45}
print(scores,type(scores))

# 2.使用内置函数：dict()
student = dict(name = 'jack', age = 20)
print(student['age'])
print(student,type(student))

# 3.空字典的创建
d = {}
print(d,type(d))
d=dict()
print(d,type(d))