# -*- coding = utf-8 -*-
# Time: 2022/4/18 23:11
# Author: Mr Wu
# File: 2.Python中常见的异常类型.py
# Software: PyCharm

# 1.ZeroDivisionError:除（或取模）零（所有数据类型）
# print(10/0)

# 2.IndexError:序列中没有此索引（index）
# l=[1,2,3,4]
# print(l[4])

# 3.KeyError：映射中没有这个键
# d={'name':'张三','age':15}
# print(d['sex'])

# 4.NameError：未声明/初始化对象（没有属性）
# print(a=a+1)

# 5.SyntaxError：Python语法错误
# int a = 20

# 6.ValueError：传入无效的参数
# a=int('hello')  # 字符串是不能转成十进制整数的
