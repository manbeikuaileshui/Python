# -*- coding = utf-8 -*-
# Time: 2022/3/27 23:18
# Author: Mr Wu
# File: 1.元组的创建.py
# Software: PyCharm

# 元组的创建
# 1.直接()
t = ('python','hello',90)
print(t,type(t))
t = 'python','hello',90  #  可省略小括号
print(t,type(t))

# 2.使用内置函数tuple()
t = tuple(('python','hello',90))
print(t,type(t))
t = tuple('python')
print(t,type(t))

# 3.只包含一个元组的元素需要使用逗号和小括号
t = (10,)  #  如果元组中只有一个元素，元素后面要加上逗号
print(t,type(t))

# 4.空元组的创建
#   <1> t = ()
print("列表：",[],type([]))
print("字典：",{},type({}))
print("元组：",(),type(()))

#   <2> t = tuple()
print("列表：",list(),type(list()))
print("字典：",dict(),type(dict()))
print("元组：",tuple(),type(tuple()))