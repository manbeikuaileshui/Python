# -*- coding = utf-8 -*-
# Time: 2022/5/7 18:33
# Author: Mr Wu
# File: 10-2.py
# Software: PyCharm

# 2、编写一个函数，接收N个正整数，输出其中的最大值和最小值。
def getMaxMin(n) :
    list = []
    for i in range(1,n+1) :
        num = int(input('请输入{}个正整数:'.format(i)))
        list.append(num)
    print('最大值是{},最小值是{}'.format(max(list),min(list)))
n = int(input('请输入元素个数:'))
getMaxMin(n)