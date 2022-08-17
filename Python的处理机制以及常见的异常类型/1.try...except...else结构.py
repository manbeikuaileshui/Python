# -*- coding = utf-8 -*-
# Time: 2022/4/9 17:51
# Author: Mr Wu
# File: 1.try...except...else结构.py
# Software: PyCharm

# 如果try块中没有抛出异常，则执行else块，如果try中抛出异常，则执行except块
try:
    a = int(input('请输入第一个整数:'))
    b = int(input('请输入第二个整数:'))
    result = a / b
except BaseException as e:
    print("出错了",e)
else:
    print('计算结果为：',result)

# try...except...else...finally结构
# finally块无论是否发生异常都会被执行，能常用来释放try块中申请的资源
try:
    a = int(input('请输入第一个整数:'))
    b = int(input('请输入第二个整数:'))
    result = a / b
except BaseException as e:
    print("出错了",e)
else:
    print('计算结果为：',result)
finally:
    print('谢谢使用')