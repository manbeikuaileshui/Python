# -*- coding = utf-8 -*-
# Time: 2022/5/7 19:48
# Author: Mr Wu
# File: 10-6.py
# Software: PyCharm

# 6、定义一个函数，输出100以内所有的素数。所谓素数是指对于一个自然数，
# 如果除了1和它自身不能再被其整数整除，则该数称为素数，比如：2，3，5，7……
import math
def sushu() :
    for i in range(2,101) :
        flag = True
        for j in range(2,i) :
            if i % j == 0 :
                flag = False
                break
        if flag == True :
            print('{}是素数'.format(i))
sushu()