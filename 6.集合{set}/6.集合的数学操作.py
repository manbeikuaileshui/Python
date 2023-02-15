# -*- coding = utf-8 -*-
# Time: 2022/3/28 20:03
# Author: Mr Wu
# File: 6.集合的数学操作.py
# Software: PyCharm

s1 = {10,20,30,40}
s2 = {20,30,40,50,60}
print('s1 = ',s1)
print('s2 = ',s2)
# 1.计算两个集合的交集
#   <1> 集合名.intersection(另一个集合名)
print('交集 = ',s1.intersection(s2))
#   <2> 利用符号  &
print('交集 = ',s1&s2)

# 2.计算两个集合的并集
#   <1> 集合名.union(另一个集合名)
print('并集 = ',s1.union(s2))
#  <2> 利用符号 |
print('并集 = ',s1|s2)

print('s1 = ',s1)
print('s2 = ',s2)
# 3.计算两个集合的差集
#   <1> 集合名.difference(另一个集合名)
print('(s1-s2)：差集 = ',s1.difference(s2)) # s1的元素 - 共有的元素
print('(s2-s1)：差集 = ',s2.difference(s1)) # s2的元素 - 共有的元素

#   <2> 利用符号  -
print('(s1-s2)：差集 = ',s1-s2)
print('(s2-s1)：差集 = ',s2-s1)

# 4.计算两个集合的对称差集
#   <1> 集合名.symmetric_difference(另一个集合名)
print('对称差集 = ',s1.symmetric_difference(s2)) # 对称差集 = 两个集合的所有元素 - 共有的元素

#   <2> 利用符号  ^
print('对称差集 = ',s1^s2)