# -*- coding = utf-8 -*-
# Time: 2022/3/30 17:29
# Author: Mr Wu
# File: 4.字符串的劈分.py
# Software: PyCharm

# 字符串劈分操作的方法
# 1.split():      2.rsplit():
# 左右劈分的共同特点：默认的劈分字符串是空格字符串，返回的值都是一个列表
#                 以通过参数sep指定劈分字符串时的劈分符
#                 通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独作为一部分

# <1> 默认的劈分字符是空格字符串，返回的值都是一个列表
s = 'hello world python'
print(s,id(s))
s1 = s.split()
s2 = s.rsplit()
print('左边：',s1,id(s1)) # 没给参数，默认劈分字符是空格字符串,一直劈分到没有空格为止，会产生一个列表
print('右边：',s2,id(s2)) # 没给参数，默认劈分字符是空格字符串,一直劈分到没有空格为止，会产生一个列表
print('-'*40)

# <2> 以通过参数sep指定劈分字符串时的劈分符
s = 'hello|world|python'
print(s,id(s))
s1 = s.split(sep='|')
s2 = s.rsplit(sep='|')
print('左边：',s1,id(s1))
print('右边：',s2,id(s2))
print('-'*40)

#   <3> 通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独作为一部分
s = 'hello|world|python'
print(s,id(s))
s1 = s.split(sep='|',maxsplit=1)
s2 = s.rsplit(sep='|',maxsplit=1)
print('左边：',s1,id(s1))
print('右边：',s2,id(s2))



