# -*- coding = utf-8 -*-
# Time: 2022/3/30 21:16
# Author: Mr Wu
# File: 10.字符串的编码与解码.py
# Software: PyCharm

s = '天涯共此时'
# 1.编码：将字符串转换成二进制数据(bytes)
byte1 = s.encode(encoding='GBK') # 编码
print(byte1) # 在GBK这种编码格式中，一个中文占两个字节
byte2 = s.encode(encoding='UTF-8') # 编码
print(byte2) # 在UTF-8这种编码格式中，一个中文占三个字节

# 2.解码：将bytes类型的数据转换成字符串类型
# byte代表就是一个二进制数据(字节类型的数据)
print(byte1.decode(encoding='GBK')) # 解码
print(byte2.decode(encoding='UTF-8')) # 解码