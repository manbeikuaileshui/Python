# -*- coding = utf-8 -*-
# Time: 2022/3/23 18:26
# Author: Mr Wu
# File: break、continue语句.py
# Software: PyCharm

"""
break语句
   用于结束循环结构，通常与分支结构if一起使用
"""
# 从键盘录入密码，最多录入3次，如果正确就结束循环
# for i in range(3):
#     a=input('请输入密码：')
#     if a=='1223':
#         print('密码正确')
#         break
#     else:
#         print('密码错误')

i=0
while i<3:
    a=input('请输入密码：')
    if a=='1223':
        print('密码正确')
        break
    else:
        print('密码错误')
        i+=1
"""
continue语句
   用于结束当前循环，进入下一次循环，通常与分支结构中的if一起使用
"""
"""
要求输出1-50之间所有5的倍数，5,10,15....
5的倍数共同的特点：模5余数为0的数都是的倍数
什么样的数不是5的倍数：模5余数不为0的数都不是5的倍数
"""
for i in range(1,51):
    if i%5 != 0:
        continue
    print(i,end=' ')