# -*- coding = utf-8 -*-
# Time: 2022/4/20 11:28
# Author: Mr Wu
# File: 2.第二题.py
# Software: PyCharm

'''
2.输入一个0到100之间的成绩：90-100：666，真厉害，80-90：还不错，70-80：还有很大的进步空间，60-70：
要小心，马上就快挂了，<60：孩子多半是废了......
'''
score=float(input('请输入一个0-100之间的成绩：'))
if score > 100 or score < 0:
    print('输入有误')
    exit()
if score >= 90 and score <=100:
    print('真厉害')
elif score >=80 and score <90:
    print('还不错')
elif score >=70 and score <80:
    print('还有很大的进步空间')
elif score >= 60 and score < 70:
    print('要小心，马上就快挂了')
else:
    print('孩子多半是废了......')

