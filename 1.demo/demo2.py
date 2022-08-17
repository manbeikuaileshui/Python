# -*- coding = utf-8 -*-
# Time: 2022/3/17 12:36
# Author: Mr Wu
# File: demo2.py
# Software: PyCharm

  #数据类型转换
"""
  1.str():将其他数据类型转成字符串
  <1>可用引号转换
  例：str(123)-->'123'
  2.int():将其它数据类型转成整数
  <1>文字类和小数类字符串，无法转化成整数
  <2>浮点数转化成整数：抹零取整
  例：int('hello')-->无法转化
     int('9.8')-->无法转化
     int(9.8)-->9
  3.float():将其它数据类型转成浮点数
  <1>文字类无法转成整数
  <2>整数转成浮点数，末尾为.0
  例：float('hello')-->无法转换
     float(9)-->9.0
"""
name = '张三'
age = 20
height = 175.5
print(type(name),type(age)) #说明name与age的数据类型不相同
# print('我叫'+name+'，今年'+age+'岁')  #  当将str类型与int类型进行连接时，报错，解决方案，类型转换
print('我叫'+name+'，今年'+str(age)+'岁，身高'+str(height)+'cm')  #  将int类型通过str()函数转成了str类型
print('我叫%s，今年%d岁，身高%fcm' % (name,age,height))
print('我叫%s，今年%d岁，身高%.1fcm' % (name,age,height))
print('我叫%s，今年%d岁，身高%.2fcm' % (name,age,height))
#  python3.6版本开始支持f-string,占位统一使用{}占位，填充的数据直接写在{}里边
print(f'我叫{name}，今年{age}岁，身高{height}cm')

#  输出50%，使用格式化输出的时候，想要输出一个%，需要使用两个%
#  print('及格的人数占比为%d%'%50)
print('及格的人数占比为%d%%'%50)
print(f'及格的人数占比为{50}%')

print('----------int()常用函数：将其它类型转换成int类型----------')
s1 = '128'
s2 = '76.77'
s3 = 'hello'
f1 = 98.7
ff = True
print(type(s1),type(s2),type(s3),type(f1),type(ff))
print(int(s1),type(int(s1)))  #  将str转换成int类型，字符串为数字串
# print(int(s2),type(int(s2)))  #  将str转换成int类型，报错，因为字符串为小数串
# print(int(s3),type(int(s3)))  #  将str转换成int类型时，字符串必须为数字串(整数)，非数字串是不允许转换的
print(int(f1),type(int(f1)))  #  将float转换成int类型，截取整数部分，舍掉小数部分
print(int(ff),type(int(ff)))  #  将bool转换成int类型，True为1，Flase为0

print('----------float()常用函数:将其它数据类型转成float类型----------')
s1 = '128.89'
s2 = '76'
s3 = 'hello'
f1 = 98
ff = True
print(type(s1),type(s2),type(s3),type(f1),type(ff))
print(float(s1),type(float(s1)))  #  128.89
print(float(s2),type(float(s2)))  #  76.0
# print(float(s3),type(float(s3)))  #  字符串中的数据如果是非数字串，则不允许转换
print(float(f1),type(float(f1)))  #  98.0
print(float(ff),type(float(ff)))  #  1.0

a,b = 10,20  #  解包赋值
a,b = b,a  #  交换两个变量的值
print(a,b)

"""
一个变量由三部分组成：标识(id)、类型、值(value)
'='：表示赋值
'=='：比较值是否相等
'is'：比较标识是否相等
"""
a = 10
b = 10
print(a == b)  #  True,说明a与b的值相等
print(a is b)  #  True,说明a与b的标识相等
lst1 = [11,22,33,44]
lst2 = [11,22,33,44]
print(lst1 == lst2)  #  True
print(lst1 is lst2)  #  False
print(id(lst1))
print(id(lst2))
print(a is not b)
print(lst1 is not lst2)

a,b=1,2
print('----------and 并且----------')  #  当两个运算符都为True时，运算结果才为True
print(a == 1 and b == 2)  #  True and True-->True
print(a ==1 and b != 2)  #  True and Flase-->Flase
print(a != 1 and b == 2)  #  Flase and True-->Flase
print(a != 1 and b != 2)  #  Flase and Flase-->Flase

print('----------or 或者----------')  #  只要一个运算数为True时，运算结果就为True
print(a == 1 or b == 2)  #  True or True-->True
print(a ==1 or b != 2)  #  True or Flase-->True
print(a != 1 or b == 2)  #  Flase or True-->True
print(a != 1 or b != 2)  #  Flase or Flase-->Flase

print('----------not 对bool类型操作数取反----------')  #  如果运算符为True，运算结果为Flase；反之
f1 = True
f2 = False
print(not f1)
print(not f2)

print('----------in 在什么之间----------')
s = 'helloworld'
print('w'in s)
print('k' in s)

print('----------not in 不在什么之间----------')
print('w' not in s)
print('k' not in s)


