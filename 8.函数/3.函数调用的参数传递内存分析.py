# -*- coding = utf-8 -*-
# Time: 2022/4/7 12:15
# Author: Mr Wu
# File: 3.函数调用的参数传递内存分析.py
# Software: PyCharm

# 函数调用的参数传递内存分析
def fun(arg1,arg2):
    print('arg1 =',arg1)
    print('arg2 =',arg2)
    arg1 = 100 # 这里只是把 arg1 改为100，其实 n1 并没有变化
    arg2.append(10) # 列表 arg2 末尾增加一个元素，实际 n2 也增加了
    print('arg1 =',arg1)
    print('arg2 =',arg2)

n1=11
n2=[22,33,44]
print('n1 =',n1)
print('n2 =',n2)
print('-'*40)
fun(n1,n2) # 位置传参，arg1，arg2,是函数定义处的形参；n1，n2是函数调用处的实参。总结：实参名与形参名可以不一致
print('n1 =',n1) # 所以最终 n1 = 11
print('n2 =',n2) # n2 = [22,33,44,10]