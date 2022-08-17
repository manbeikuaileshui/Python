# -*- coding = utf-8 -*-
# Time: 2022/3/26 21:20
# Author: Mr Wu
# File: 5.字典元素的遍历.py
# Software: PyCharm

# 字典元素的遍历
scores = {'张三':100,'李四':98,'王五':45}
for item in scores:
    print(item,scores[item],scores.get(item))
for item in scores.items():
    print(item)