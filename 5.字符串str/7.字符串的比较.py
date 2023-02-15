# -*- coding = utf-8 -*-
# Time: 2022/3/30 20:40
# Author: Mr Wu
# File: 7.字符串的比较.py
# Software: PyCharm

# 字符串的比较操作
# 运算符：>,<,>=,<=,==,!=
# 比较规则：首先比较两个字符串中的第一个字符，如果相等则继续比较下一个字符，依次比较下去，直到两个字符串中的字符不相等时，
#         其比较结果就是两个字符串的比较结果，两个字符串中的所有后续字符将不再被比较
# 比较原理：两个字符串进行比较时，比较的是其 ordinal value(原始值)，调用内置函数 ord可以得到指定字符的 ordinal value。
#         与内置函数 ord对应的是内置函数 chr，调用内置函数 chr时指定 ordinal value可以得到其对应的字符
print('apple'>'app') # True
print('ab'>'app') #False
print(ord('b'),ord('p'),ord('巫'))
print(chr(98),chr(112),chr(24043))

# '=='与'is'的区别
# '==':比较的是value
# 'is':比较的是id是否相等
a = 'python%'
b = 'python%'
print(a == b) # True
print(a is b) # 在IDLE模式下，结果为False

