# -*- coding = utf-8 -*-
# Time: 2022/3/15 10:49
# Author: Mr Wu
# File: demo1.py
# Software: PyCharm

# 将数据输出文件中，注意点：1.所指定的盘符应存在  2.使用file = 设置的变量名（file = fp）
fp = open('D:/text.txt','a+')  #  a+:如果文件不存在就创建，存在就在文件内容的后面继续追加
print('hello world',file = fp)

# 不进行换行输出（输出内容在一行当中）
print('hello','world','python')

#  转义字符
print('hello\nworld')  #  \ + 转义功能的首字母  n-->newline的首字符表示换行
print('hello\tworld')  #  空开’\t‘前后的字符，空格个数取决于前后字符的个数,4-前字符个数/4
print('helloooo\tworld')
print('hello\rworld')  #  world将hello进行了覆盖
print('hello\bworld')  #  \b是退一个格，将o退没了

# 原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r，或R
# 注意事项：最后一个字符不能是反斜杠‘\‘，但可以是两个反斜杠
print('http:\\www.baidu.com')
print('http:\\\\www.baidu.com')
print(r'http:\\www.baidu.com')
print(R'http:\\www.baidu.com')
# print(r'http:\\www.baidu.com\')  #  错误示范
print(R'http:\\www.baidu.com\\')

# print('老师说:'大家好'')  #  错误语法
# print("老师说：“大家好”")  #  错误语法
print('老师说：\'大家好\'')
print("老师说：\"大家好\"")
print("老师说：'大家好'")

name = '玛丽亚'
print(name)
print('标识:',id(name))
print('类型:',type(name))
print('值:',name)

print('十进制:',118)  #  打印十进制数以十进制输出
print('二进制:',0b10101111)  #  打印二进制数以十进制输出
print('八进制:',0o176)  #  打印八进制以十进制输出
print('十六进制:',0x1EAF)  #  打印十六进制以十进制输出

n1=1.1
n2=2.2
n3=2.1
print(n1+n3)
print(n1+n2)  #  计算结果为3.3000000000000003不精确（个别不精确），实际值为3.3，改进如下
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

str1='人生苦短，我用python'  # 可用单引号概括字符串，不能换行
str2="人生苦短，我用python"  # 可用双引号概括字符串，不能换行
str3="""人生苦短，
我用python"""  # 可用三个双引号概括字符串，一般是由于一行不够写，才使用三个双引号进行换行
str4='''人生苦短，
我用python'''  # 可用三个单引号概括字符串，一般是由于一行不够写，才使用三个单引号进行换行
print(str3,type(str3))


# 正常除(/):商必定带小数
print(4/2)
# 地板除方式(//)：正常除得到的数向下取整
print(5/2)
"""
求余数的方式：
1.通过地板除，得到商
2.通过公式：余数 = 被除数 -商 * 除数
"""
print(5//2)  #2
print(5%2)  #1
print(-5//2)  #-3
print(-5%2)  #1
print(5//-2)  #-3
print(5%-2)  #-1
print(-5//-2)  #2
print(-5%-2)  #-1

#从外部设备输入数据：input()常用函数，返回的值类型为字符串类型
num = input("请输入一个整数：")
print(num,type(num))
num = int(input("请输入一个整数："))
print(num,type(num))

#eval()函数的作用：去掉最外层的包裹符
a = "'老师说：大家好！'"
print(a)
print(eval(a))

#  打印格式
"""
  %c-->字符       %d-->有符号十进制整数     %x-->十六进制整数(小写字母ox)
  %s-->字符串     %u-->无符号十进制整数     %X-->十六进制整数(大写字母OX)
  %f-->浮点数     %e-->科学计数法(小写'e')  %g-->%f和%e的简写
  %o-->八进制整数  %E-->科学计数法(大写'E')  %G-->%f和%E的简写
"""

#  print()函数输出之后，默认会添加一个换行，如果不想要这个换行可以去掉
print("hello",end = ' ')
print('world')
print("hello",end = '*_*')
print('world')
#  同一字符串换行打印
print("good good study\nday day up")