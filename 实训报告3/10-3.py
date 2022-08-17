# -*- coding = utf-8 -*-
# Time: 2022/5/7 18:45
# Author: Mr Wu
# File: 10-3.py
# Software: PyCharm

# 3、编写一个函数，接收一个学生的成绩，按要求输出评语（优秀（90以上）、良好（89-80）、合格（60-79）、不及格（60以下））
def SCORE(score) :
    if score >= 90 :
        print('成绩{}分，为优秀'.format(score))
    elif score >= 80 and score <=89 :
        print('成绩{}分，为良好'.format(score))
    elif score >= 60 and score <=79 :
        print('成绩{}分，为合格'.format(score))
    else :
        print('成绩{}分，为不及格'.format(score))
score = float(input('请输入一个成绩:'))
if score > 100 or score <0 :
    print('成绩输入有误！')
else :
    SCORE(score)