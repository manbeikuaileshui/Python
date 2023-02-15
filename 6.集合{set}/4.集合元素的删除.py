# -*- coding = utf-8 -*-
# Time: 2022/3/28 18:40
# Author: Mr Wu
# File: 4.集合元素的删除.py
# Software: PyCharm

s  = {10,20,30,40,50,60}
# 集合元素的删除操作
#  1.调用remove()方法，一次删除一个指定元素，如果指定的元素不存在则抛出KeyError
s.remove(10)
print(s)
# s.remove(70)  #报错

#  2.调用discard()方法，一次删除一个指定元素，如果指定的元素不存在不抛出异常
s.discard(20)
print(s)
s.discard(70)  #集合里面没有70，虽然要删除70，但不会报错
print(s)

#  3.调用pop()方法，一次只删除一个任意元素
a=s.pop() # pop()函数的返回值是被删除的元素
print(s)
print(a)

#  4.调用clear()方法，清空集合
s.clear()
print(s)