# -*- coding = utf-8 -*-
# Time: 2022/3/23 20:55
# Author: Mr Wu
# File: 二重循环中的break和continue.py
# Software: PyCharm

# 二重循环中的break和continue用于控制本层循环
for i in range(5):  #外层执行5次
    for j in range(1,11):  #数字1-10
        if j%2==0:  #整除2的数
            break  #跳出这个内层循环，但外层循环还是要执行的
        print(j,end='\t')
    print()

for i in range(5):  #外层执行5次
    for j in range(1,11):  #数字1-10
        if j%2==0:  #整除2的数
            continue  #跳出本次内层循环，继续执行内层循环
        print(j,end='\t')
    print()