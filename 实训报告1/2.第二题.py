# -*- coding = utf-8 -*-
# Time: 2022/4/6 23:03
# Author: Mr Wu
# File: 2.第二题.py
# Software: PyCharm

# 2、给出一个字母组成的字符串，先将字符串全部换成大写字母输出；
# 接着统计字母“e”出现的次数；最后将字母“e”全部替换为“abc”并输出。
s = input("请输入包含'e'的字符串：")
print('换成大写后的字符串：',s.upper())
print("字母'e'出现的次数：",s.count('e'))
print('替换之后的字符串：',s.replace('e','abc'))