# -*- coding = utf-8 -*-
# Time: 2022/3/28 22:29
# Author: Mr Wu
# File: 0.字符串的驻留机制.py
# Software: PyCharm

# 字符串：在python中字符串是基本数据类型，是一个不可变的字符序列

# 什么叫字符串驻留机制呢？
#     仅保存一份相同且不可变字符串的方法，不同的值被存放在字符串的驻留池中，python的驻留机制对相同的字符串只保留一份拷贝，
# 后续创建相同字符串时，不会开辟新空间，而是把该字符串的地址赋给新创建的变量
a = 'python'
print(a,id(a))
b = "python"
print(b,id(b))
c = '''python'''
print(c,id(c))
# 相同的字符串在内存中只会存储一份，所以三个地址相同
print('-'*40)

# 驻留机制的几种情况（交互模式）
# 1.字符串的长度为0或1时
s1=''
s2=''
print(s1 is s2)
print(id(s1),id(s2))
s1='%'
s2='%'
print(s1 is s2)
print(id(s1),id(s2))
print('-'*40)

# 2.符合标识符的字符串:含有字母、数字、下划线的字符串
s1='abc%'
s2='abc%'
print(s1 is s2)
print(id(s1),id(s2))  # 在pycharm里面只开辟了一块空间，但在交互模式下(IDLE)，它们的ID是不相同的
s1='abc'
s2='abc'
print(s1 is s2)
print(id(s1),id(s2)) # 在交互模式下它们的ID也相同
print('-'*40)

# 3.字符串只在编译时进行驻留，而非运行时
a='abc'
b='ab'+'c'
c=''.join(['ab','c'])
print(a is b) # id相同
print(a is c) # id不同
print(c,type(c)) # abc <class 'str'>
print(a,type(a)) # abc <class 'str'>
# 内容相同、类型相同，为什么id不同？
# 答：因为b的值在运行之前就已经连接完毕了，c是程序运行时才连接的
print('-'*40)

# 4.[-5,256]之间的整数数字
a=-5
b=-5
print(a is b) # id相同
a=-6
b=-6
print(a is b) # 在pycharm里面只开辟了一块空间，但在交互模式下(IDLE)，它们的ID是不相同的
print('-'*40)

# sys中的intern方法强制2个字符串指向同一个对象
import sys
a='abc%'
b='abc%'
print(a is b) #在pycharm里面为True,但在交互模式下为Flase,可经过下面强制操作
a = sys.intern(b)
print(a is b)

# pycharm对字符串进行了优化处理

# 字符串驻留机制的优缺点
# 1.当需要值相同的字符串时，可以直接从字符串池里拿来使用，避免频繁的创建和销毁，提升效率和节约内存，
#   因此拼接字符串和修改字符串是会比较影响性能的
# 2.在需要进行字符串拼接时建议使用str类型的join方法，而非 ”+“，因为join()方法是先计算出所有字符中的长度，
#   然后再拷贝，只new一次对象，效率要比 “+” 效率高