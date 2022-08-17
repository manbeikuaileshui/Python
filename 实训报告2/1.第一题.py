# -*- coding = utf-8 -*-
# Time: 2022/4/20 11:27
# Author: Mr Wu
# File: 1.第一题.py
# Software: PyCharm

# 1.输入一个成绩，判断其是否及格，如果及格就输出及格（成绩大于或者等于60即为及格），否则输出“不及格”。
score=float(input('请输入你的分数：'))
if score > 100 or score < 0:
    print('输入有误')
    exit()
if score >= 60:
    print('及格')
else:
    print('不及格')
