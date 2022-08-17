# -*- coding = utf-8 -*-
# Time: 2022/3/30 18:36
# Author: Mr Wu
# File: 5.字符串的判断.py
# Software: PyCharm

# 判断字符串操作的方法
# 1.isidentifier():判断指定的字符串是不是合法的标识符
s1 ='hello python'
print('1.',s1.isidentifier()) # False
s2 = '张三_'
print('1.',s2.isidentifier()) # True

# 2.isspace():判断指定的字符串是否全部由空白字符组成(回车、换行、水平制表符)
s1 = 'hello python'
print('2.',s1.isspace()) # False
s2 = '\t'
print('2.',s2.isspace()) # True

# 3.isalpha():判断指定的字符串是否全部由字母组成
s1 = '张三'
print('3.',s1.isalpha()) # True
s2 = 'hello'
print('3.',s2.isalpha()) # True
s3 = '张三1'
print('3.',s3.isalpha()) # False

# 4.isdecimal():判断指定字符串是否全部由十进制的数字组成
s1 = '123'
print('4.',s1.isdecimal()) # True
s2 = '123四'
print('4.',s2.isdecimal()) # False
s3 = 'ⅡⅡⅡⅡ'
print('4.',s3.isdecimal()) # False

# 5.isnumeric():判断指定字符串是否全部由数字组成
s1 = '123'
print('5.',s1.isnumeric()) # True
s2 = '123四'
print('5.',s2.isnumeric()) # True
s3 = 'ⅡⅡⅡⅡ'
print('5.',s3.isnumeric()) # True

# 6.isalnum():判断指定字符串是否全部由字母或数字组成
s1 = 'abc1'
s2 = '张三123'
print('6',s1.isalnum()) # True
print('6',s2.isalnum()) # True