# -*- coding = utf-8 -*-
# Time: 2022/3/23 19:01
# Author: Mr Wu
# File: else语句.py
# Software: PyCharm

"""
else 语句
    与else语句配合使用的三种情况
    1.  if...else  表达式不成立时执行else
    2.  while...else  没有碰到break时执行else
    3.  for...else  没有碰到break时执行else
"""
# 1.  if...else
a=int(input('请输入一个整数：'))
if a>0:
    print('正整数')
else:
    print('负整数')

# 2.  while...else
i=0
while i<3:
    a=input('请输入密码：')
    if a=='1223':
        print('密码正确')
        break
    else:
        print('密码错误')
        i+=1
else:
    print('对不起，三次密码均错误')

# 3.  for...else
for i in range(3):
    a=input('请输入密码：')
    if a=='1223':
        print('密码正确')
        break
    else:
        print('密码错误')
else:
    print('对不起，三次密码均错误')
