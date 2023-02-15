# -*- coding = utf-8 -*-
# Time: 2022/4/20 11:28
# Author: Mr Wu
# File: 4.第四题.py
# Software: PyCharm

# 4.利用循环结构，计算并输出100-999之间所有的水仙花数，并输出。
i = 100
while i < 1000:
    bw = i // 100
    sw = i // 10 % 10
    gw = i % 10
    if bw**3 + sw**3 + gw**3 ==i:
        print(f'{i}为水仙花数')
    i = i + 1