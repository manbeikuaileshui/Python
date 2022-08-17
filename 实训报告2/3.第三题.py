# -*- coding = utf-8 -*-
# Time: 2022/4/20 11:28
# Author: Mr Wu
# File: 3.第三题.py
# Software: PyCharm


# 3.利用循环去计算0-100以内所有奇数或者偶数的和，并输出（可以任意挑选奇数或者偶数）。
sum = 0
ousum = 0
jisum = 0
for i in range(0,101):
    sum = sum + i
    if i % 2 ==0:
        ousum = ousum + i
    else:
        jisum = jisum + i
print(f'总和为{sum}，偶数和为{ousum},奇数和为{jisum}')
