# -*- coding = utf-8 -*-
# Time: 2022/4/7 12:35
# Author: Mr Wu
# File: 4.函数的返回值.py
# Software: PyCharm


# 函数的返回值
# 1.如果函数没有返回值，即函数执行完毕之后，不需要给调用处提供数据，return可以省略不写
def fun1():
    print('hello')
fun1()

# 2. 函数的返回值，如果是1个，直接返回类型
def fun2():
    return 'hello'
print(fun2())

# 3. 函数的返回值，如果是多个，返回的结果为元组
def fun3():
    return 'hello','world'
print(fun3())

def fun(num):
    odd=[] # 存奇数
    even=[] # 存偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even
lst = [10,29,34,23,44,53,55]
print(fun(lst))
