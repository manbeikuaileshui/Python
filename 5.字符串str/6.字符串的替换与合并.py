# -*- coding = utf-8 -*-
# Time: 2022/3/30 20:11
# Author: Mr Wu
# File: 6.字符串的替换与合并.py
# Software: PyCharm

s = 'hello python, hello python'
# 1.字符串替换
# replace():第一个参数指定被替换的子串，第二个参数指定替换子串的字符串，第三个参数指定最大替换次数,
#           该方法返回替换后得到的字符串，替换前的字符串不发生变化
print(s,id(s))
s1 = s.replace('hello','java') # 把字符串中的'hello'都替换成'java'
print(s1,id(s1)) # 原字符串不变，产生新的字符串
print('-'*40)

print(s,id(s))
s1 = s.replace('hello','java',1) # 只把第一个'hello'替换成'java'
print(s1,id(s1)) # 原字符串不变，产生新的字符串
print('-'*40)

# 2.join():将列表或元组中的字符串合并成一个字符串
l = ['hello','world']
print('|'.join(l))
t = ('hello','world')
print(' '.join(t))
s = 'python'
print('*'.join(s))
