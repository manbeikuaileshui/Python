# -*- coding = utf-8 -*-
# Time: 2022/4/6 22:59
# Author: Mr Wu
# File: 4.第四题.py
# Software: PyCharm

# 4、要求用户从键盘输入一个三位数的整数，
# 编写一个能输出其百位、十位、个位及三位数字之和的程序。
# 方法1
str = input('请输入一个三位数的整数：')
b = str[:1]
s = str[1:2]
g = str[2:3]
print(int(b),int(s),int(g),int(b)+int(s)+int(g))
# 方法2
str = int(input('请输入一个三位数的整数：'))
b = str // 100
s = str // 10 % 10
g = str % 10
print(b,s,g,b+s+g)