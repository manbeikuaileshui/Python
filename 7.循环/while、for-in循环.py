# -*- coding = utf-8 -*-
# Time: 2022/3/22 22:44
# Author: Mr Wu
# File: while、for-in循环.py
# Software: PyCharm

"""
while循环
while 条件表达式：
     条件执行体（循环体）
"""
a = 1
while a < 10:
    print(a,end = ' ')
    a+=1

# 计算0-4之间的累加和
a = 0
sum = 0
while a < 5:
    sum += a
    a += 1
print('和为:',sum)

# 计算1-100之间的偶数和
a = 1
sum = 0
while a <= 100:
    if a % 2 ==0:
    # if a % 2:   #求出的是奇数和
        sum += a
    a+=1
print('和为:',sum)

"""
for-in循环
    in表达从（字符串、序列）中依次取值，又称为遍历
    for-in遍历的对象必须是可迭代对象
for-in的语法结构
  for 自定义的变量in可迭代对象：
      循环体
"""
for item in 'Python':
    print(item,end=' ')

for i in range(10):
    print(i, end = ' ')

# 循环体内不需要访问自定义变量，可以将自定义变量替代为下划线
for _ in range(5):
    print('人生苦短，我用python')

# 使用for循环，计算1-100之间的偶数和
sum = 0
for i in range(1,101):
    if i % 2 == 0:
        sum+=i
print('1-100之间的偶数之和：',sum)

"""
输出100-999之间的水仙花数
举例：
153=3*3*3+5*5*5+1*1*1
"""
print('100-999的水仙花数：',end=' ')
for a in range(100,1000):
    ge=a%10
    shi=a//10%10
    bai=a//100
    if ge**3 + shi**3 + bai**3 == a:
        print(a,end=' ')
