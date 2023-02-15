# -*- coding = utf-8 -*-
# Time: 2022/4/9 16:33
# Author: Mr Wu
# File: 3.思路不清导致的问题解决方案.py
# Software: PyCharm

# 1.使用print()函数
# 2.使用“#”暂时注释部分内容
# 题目要求：豆瓣电影Top250排行，使用列表存储电影信息，要求输入名字在屏幕上现实xxx出演了哪部电影
lst=[{'rating':[9.7,50],'id':'1292052','type':['犯罪','剧情'],'title':'肖申克的救赎',
      'actors':['蒂姆.罗宾斯','摩根.佛里曼']},
     {'rating':[9.6,50],'id':'1291546','type':['剧情','爱情','同性'],'title':'霸王别姬',
      'actors':['张国荣','张丰毅','巩俐','葛优']},
     {'rating':[9.6,50],'id':'1296141','type':['剧情','犯罪','悬疑'],'title':'控方证人',
      'actors':['泰隆.鲍华','玛琳.黛德丽']}]
name = input('请输入你要查询的演员：')
# for item in lst:
#     for movie in item:
#         actors=movie['actors']
#         if name in actors:
#             print(name+'出演了：'+movie)

# 更正后：
for item in lst:  # 遍历列表,item是一个又一个的字典
    act_lst=item['actors']
    for actor in act_lst:
        if name in actor:
            print(name+'出演了：'+item['title'])