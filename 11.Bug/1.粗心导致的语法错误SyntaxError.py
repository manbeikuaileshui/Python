# -*- coding = utf-8 -*-
# Time: 2022/4/9 15:38
# Author: Mr Wu
# File: 1.粗心导致的语法错误SyntaxError.py
# Software: PyCharm

# 1.
# age = input('请输入你的年龄：')  # input默认返回值类型为字符串
# if age>=18  # 没加 ':'  另外，age为字符串无法与18进行比较
#     print('成年人，做事需要负法律责任了')
# 更正后：
age = input('请输入你的年龄：')
if int(age)>=18:
    print('成年人，做事需要负法律责任了')

# 2.
# while i<10:  # i没有初始值
#     print（i）  # 使用了中文的括号
# 更正后：
i=0
while i<10:
    print(i,end='\t')
    i+=1

# 3.
# for i in range(3):
#     uname=input('请输入用户名：')
#     pwd=input('请输入密码：')
#     if uname='admin' and pwd='admin':  # 把赋值符号当做判断符号使用
#         print('登录成功！')
#         break
#     else  # 未加 ‘：’
#         print('输入有误')
# else
#     print('对不起，三次均输入错误')

# 更正后：
for i in range(3):
    uname=input('请输入用户名：')
    pwd=input('请输入密码：')
    if uname=='admin' and pwd=='admin':
        print('登录成功！')
        break
    else:
        print('输入有误')
else:
    print('对不起，三次均输入错误')