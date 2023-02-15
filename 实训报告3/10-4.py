# -*- coding = utf-8 -*-
# Time: 2022/5/7 18:56
# Author: Mr Wu
# File: 10-4.py
# Software: PyCharm

# 4、编写一个函数，输出所有的三位数的水仙花数。所谓水仙花数是指一个 3 位数，
#   它的每位上的数字的 3次幂之和等于它本身。例如：13 + 53+ 33 = 153。”
def sxh() :
    for i in range(100,1000) :
        b = i // 100
        s = i // 10 % 10
        g = i % 10
        if b**3 + s**3 + g**3 == i :
            print('{}是水仙花数'.format(i))
sxh()