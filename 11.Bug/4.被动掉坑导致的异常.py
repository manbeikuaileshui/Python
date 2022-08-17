# -*- coding = utf-8 -*-
# Time: 2022/4/9 17:25
# Author: Mr Wu
# File: 4.被动掉坑导致的异常.py
# Software: PyCharm

# 被动掉坑：程序代码逻辑没有错，只是因为用户错误操作或者一些“例外情况”而导致的程序崩溃
# 题目要求：输入两个整数并进行除法运算
# a=int(input('请输入一个整数：'))  # 不小心输入了字母、等
# b=int(input('请输入另一个整数：'))  # 不小心输入了0、等
# result=a/b
# print('结果为：',result)
# 更正后：
# 被动掉坑的解决方案：python提供了异常处理机制，可以在异常出现时及时捕获，然后内部“消化”，让程序继续运行
# 多个excep结构：捕获异常的顺序按照先子类后父类的顺序，为了避免遗漏可能出现的异常，
#              可以在最后增加BaseException
try:
    a = int(input('请输入一个整数：'))
    b = int(input('请输入另一个整数：'))
    result = a / b
    print('结果为：', result)
except ZeroDivisionError:
    print('除数不能为0哦！！！')
except ValueError:
    print('请输入整数哦！！！')
except BaseException as e:
    print(e)
print('程序结束')