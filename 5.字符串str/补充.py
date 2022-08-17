# -*- coding = utf-8 -*-
# Time: 2022/4/1 16:17
# Author: Mr Wu
# File: 补充.py
# Software: PyCharm

# 去除字符串的左右空白
# 字符串名.strip()
s = '   I am a student   '
print(s,len(s),id(s))
print(s.strip(),len(s.strip()),id(s.strip())) # 产生了新的字符串

# python中字符串的一些方法
# in、len()、ord()、chr()
s = 'I am a student'

print('I' in s) # in
print('I' not in s)

print(len(s)) # 求字符串长度

print(ord(s[0])) # 求元素的ASSIC码值
print(chr(97)) # 求ASSIC码值代表的字符

print(s.startswith('I')) # 判断字符串的第一个元素
print(s.startswith('a'))
print(s.endswith('t')) # 判断字符串中的最后一个元素
print(s.endswith('s'))

# 统计字符串中某字符出现的次数
s = 'abcdefefef'
print(s.count('e'))