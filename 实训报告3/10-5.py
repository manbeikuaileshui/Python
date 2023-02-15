# -*- coding = utf-8 -*-
# Time: 2022/5/7 19:02
# Author: Mr Wu
# File: 10-5.py
# Software: PyCharm

# 5、定义一个函数，输出具有以下特征的四位数。已知某四位数9801具有如下特征：
#   它的前两位数字“98”与后两位数字“01”的和是“99”，而“99”的平方正好等于其本身“9801”
def get() :
    for i in range(1000,10000) :
        q = i // 100
        h = i % 100
        if (q + h)**2 == i :
            print('{}符合特征'.format(i))
get()