# -*- coding = utf-8 -*-
# Time: 2022/4/9 15:18
# Author: Mr Wu
# File: 9.斐波那契数列.py
# Software: PyCharm

# 斐波那契数列：1，1,2,3,5,8,13...... 除第一二 项的第 n 项都等于其前两项之和
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
# 求斐波那契数列第六项的数字
print(fib(6))

# 输出斐波那契数列前六项的数字
for i in range(1,7):
    print(fib(i),end='\t')