# -*- coding = utf-8 -*-
# Time: 2022/3/30 21:16
# Author: Mr Wu
# File: 9.字符串的格式化.py
# Software: PyCharm

# 格式化字符串的两种方法
# 1. %作为占位符
name = '小明'
age = 15
print('我的名字叫：%s，今年%d岁了。'%(name,age))

# 2. {}作占位符
name = '小明'
age = 15
print('我的名字叫：{0}，今年{1}岁了。'.format(name,age))

# 3. f-string
name = '小明'
age = 15
print(f'我的名字叫：{name}，今年{age}岁了。')

# 宽度设置：
# 1.'%xd' % 数据      x:宽度大小   d:数据类型
print('%5d' % 99) # 5表示的是宽度
# 2.'{索引：5d}'.format(数据)
print('{0:5d}'.format(99))
print('hellohello')

# 小数点设置：   .x:保留几位小数   f:数据类型
# 1.'%.xf' % 数据
print('%.3f' % 3.141592653) # .3表示保留小数点后三位
# 2.'{索引：.xf}'.format(数据)
print('{0:.3}'.format(3.141592653)) # .3表示的是保留三位数
print('{0:.3f}'.format(3.141592653)) # .3f表示的是保留三位小数

# 两者同时表示
print('%10.3f' % 3.141592653) # 宽度为10，小数点后保留三位小数
print('{0:10.3f}'.format(3.141592653)) # 宽度为10，小数点后保留三位小数