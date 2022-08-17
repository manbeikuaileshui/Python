# -*- coding = utf-8 -*-
# Time: 2022/3/25 17:40
# Author: Mr Wu
# File: 6.排序.py
# Software: PyCharm

#     列表元素的排序操作:前提是列表中的元素类型是一样的
lst = [20,40,10,98,54]

# 1. 变量名.sort()方法，默认升序，可以指定reverse=True，进行降序排序  在原列表中完成操作
print('排序前：',lst,id(lst))
lst.sort(reverse=False)  #升序排序
print('排序后：',lst,id(lst))

lst.sort(reverse=True)  #降序排序
print('排序后：',lst,id(lst))

lst.sort()  #升序排序  默认升序
print('排序后：',lst,id(lst))

print('-'*40)
# 2.新列表名 = sorted(旧列表名)，可以指定reverse=True，进行降序排序  原列表不变，产生新的列表
lst =[50,56,32,67,98,38]

print('排序前：',lst,id(lst))
new_list=sorted(lst)  #升序排序
print('排序后：',new_list,id(new_list))  #产生新列表

new_list=sorted(lst,reverse=True)  #降序排序
print('排序后：',new_list,id(new_list))  #产生新列表

new_list=sorted(lst,reverse=False)  #升序排序
print('排序后：',new_list,id(new_list))  #产生新列表