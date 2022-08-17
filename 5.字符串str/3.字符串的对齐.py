# -*- coding = utf-8 -*-
# Time: 2022/3/30 0:14
# Author: Mr Wu
# File: 3.字符串的对齐.py
# Software: PyCharm

s = 'hello,python'
# 字符串内容对齐操作的方法
# 指定宽度小于或等于实际宽度返回原字符串，大于产生新的字符串

# 1.center():居中对齐   2.ljust():左对齐  3.rjust():右对齐   4.zfill():右对齐
# 共同特点：第一个参数指定宽度，第二个参数指定填充符，第二个参数是可选的，默认是空格，
#         如果设置宽度小于或等于实际宽度则返回原字符串，若大于则产生新的字符串。
#         zfill()该方法只接收一个参数，用于指定字符串的宽度,左边用0填充
print(s,id(s))
print('居中对齐')
s1 = s.center(20,'*')
print(s1,id(s1)) # 第一个参数指定的宽度大于实际宽度，产生居中对齐的新字符串
s2 = s.center(12,'*')
print(s2,id(s2)) # 第一个参数指定的宽度等于实际宽度，返回原字符串
s3 = s.center(11,'*')
print(s3,id(s3)) # 第一个参数指定的宽度小于于实际宽度，返回原字符串
s4 = s.center(14)
print(s4,id(s4)) # 第二个参数默认为空格
print('-'*40)


print(s,id(s))
print('左对齐')
s1 = s.ljust(20,'*')
print(s1,id(s1)) # 第一个参数指定的宽度大于实际宽度，产生左对齐的新字符串
s2 = s.ljust(12,'*')
print(s2,id(s2)) # 第一个参数指定的宽度等于实际宽度，返回原字符串
s3 = s.ljust(11,'*')
print(s3,id(s3)) # 第一个参数指定的宽度小于于实际宽度，返回原字符串
s4 = s.ljust(14)
print(s4,id(s4)) # 第二个参数默认为空格
print('-'*40)


print(s,id(s))
print('右对齐')
s1 = s.rjust(20,'*')
print(s1,id(s1)) # 第一个参数指定的宽度大于实际宽度，产生右对齐的新字符串
s2 = s.rjust(12,'*')
print(s2,id(s2)) # 第一个参数指定的宽度等于实际宽度，返回原字符串
s3 = s.rjust(11,'*')
print(s3,id(s3)) # 第一个参数指定的宽度小于于实际宽度，返回原字符串
s4 = s.rjust(14)
print(s4,id(s4)) # 第二个参数默认为空格
print('-'*40)

print(s,id(s))
print('右对齐')
s1 = s.zfill(20)
print(s1,id(s1)) # 第一个参数指定的宽度大于实际宽度，第二个参数默认为0,产生右对齐的新字符串
s2 = s.zfill(12)
print(s2,id(s2)) # 第一个参数指定的宽度等于实际宽度，返回原字符串
s3 = s.zfill(11)
print(s3,id(s3)) # 第一个参数指定的宽度小于于实际宽度，返回原字符串
