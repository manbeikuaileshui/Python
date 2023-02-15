# -*- coding = utf-8 -*-
# Time: 2022/5/7 18:20
# Author: Mr Wu
# File: 10-1.py
# Software: PyCharm

# 1、定义一个函数，接收一个年份，判断该年的2月有多少天，返回对应的天数。
def YEAR(year) :
    if year % 4 ==0 and year % 400 != 0 or year % 400 == 0 :
        return 29
    else :
        return 28
year = int(input('请输入一个年份：'))
day = YEAR(year)
print('{}年的2月有{}天。'.format(year,day))
