# -*- coding = utf-8 -*-
# Time: 2022/3/29 11:25
# Author: Mr Wu
# File: 2.字符串的大小写转换.py
# Software: PyCharm

# 字符串的大小写转换操作
# 转换后，原来的字符串没有改变，都会产生新的字符串
s = 'HEllo,PYthon'

# 1. 字符串名.upper():把字符串中所有字符都转成大写
print(s.upper(),id(s.upper()))
print(s,id(s))
print('-'*40)

# 2. 字符串名.lower():把字符串中所有字符都转成小写
print(s.lower(),id(s.lower))
print(s,id(s))
print('-'*40)

# 3. 字符串名.swapcase():把字符串中所有大写字母转成小写字母，把所有小写字母都转成大写字母
print(s.swapcase(),id(s.swapcase))
print(s,id(s))
print('-'*40)

# 4. 字符串名.capitalize():把第一个字符转换为大写，把其余字符转换为小写
print(s.capitalize(),id(s.capitalize))
print(s,id(s))
print('-'*40)

# 5. 字符串名.title():把每个单词的第一个字符转换为大写，把每个单词的剩余字符转换成小写
print(s.title(),id(s.title))
print(s,id(s))
print('-'*40)