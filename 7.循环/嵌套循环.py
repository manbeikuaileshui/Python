# -*- coding = utf-8 -*-
# Time: 2022/3/23 20:13
# Author: Mr Wu
# File: 嵌套循环.py
# Software: PyCharm

# 输出一个三行四列的矩形
for i in range(3):  #行
    for j in range(4):  #列
        print('*',end='\t')  #不换行输出
    print()  #换行

# 打印一个直角三角形（9*9）
for i in range(1,10):  #行
    for j in range(1,i+1):  #列
        print('*',end=' ')
    print()

for i in range(1,10):  #行
    for j in range(1,i+1):  #列
        # print(f'{j}x{i}={i*j}',end="\t")
        print(j,'x',i,'=',i*j,end="\t")
    print()