# -*- coding = utf-8 -*-
# Time: 2022/3/19 18:23
# Author: Mr Wu
# File: if语句.py
# Software: PyCharm

# money = 1000
# ret =int(input('请输入取款金额：'))
# if ret <= money:
#     print('取款成功，剩余余额为：',money - ret)
#
# num = int(input('请输入一个整数：'))
# if num % 2 == 0:
#     print(num,'为偶数')
# else:
#     print(num,'为奇数')
#
# ret = int(input('请输入你的成绩：'))
# if ret >= 90 and ret <= 100:
#     print('A')
# elif ret >=80 and ret <90:
#     print('B')
# elif 80 > ret >= 70:
#     print('C')
# elif 70 > ret >= 60:
#     print('D')
# elif 60 > ret >= 0:
#     print('E')
# else:
#     print('输入错误')
#
# ret = input('您是会员吗？\ny/n:')
# money = float(input('请输入您的消费金额：'))
# if ret =='y':
#     if money >= 200:
#         print('打八折，付款金额为：',money*0.8)
#     elif 200 > money >= 100:
#         print('打九折，付款金额为：',money*0.9)
#     else:
#         print('不打折，付款金额为：',money)
# else:
#     if money >= 200:
#         print('打九五折，付款金额为：',money*0.95)
#     else:
#         print('不打折，付款金额为：',money)
#
a = int(input('请输入一个整数：'))
b = int(input('请输入另一个整数：'))
#  比较大小
if a >= b:
    print(a,'大于等于',b)
else:
    print(a,'小于',b)
print('使用条件表达式比较')

#  条件表达式：if……else的简写
#  语法结构：x if 判断条件 else y
#  运算规则：如果判断条件的布尔值为True,条件表达式的返回值为x,否则条件表达式的返回值为y
a = int(input('请输入一个整数：'))
b = int(input('请输入另一个整数：'))
print( str(a) + '大于等于' + str(b) if a >= b else str(a) + '小于' + str(b) )
print( f'{a}大于等于{b}' if a >= b else f'{a}小于{b}' )
