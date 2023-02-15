# -*- coding = utf-8 -*-
# Time: 2022/4/9 16:06
# Author: Mr Wu
# File: 2.知识不熟练导致的错误.py
# Software: PyCharm

# 1.索引越界问题IndexError
lst=[11,22,33,44]
# print(lst[4])  # 索引越界
print(lst[3])  # 更正后

# 2.append()方法的使用掌握不熟练
lst=[]
# lst=append('A','B','C')  # append()函数一次只能追加一个元素，而且也不是用 '=',而是用 '.'
# 更正后：
lst.append('A')
lst.append('B')
lst.append('C')
print(lst)