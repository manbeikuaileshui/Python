# -*- coding = utf-8 -*-
# Time: 2022/5/11 17:11
# Author: Mr Wu
# File: 11-3.py
# Software: PyCharm

# 1.引入requests与import
import requests as rq
import time as tt

# 2.设置爬取的URL地址
url_add = "https://movie.douban.com/j/chart/top_list"

# 设置爬取多少数据
for i in range(5):
    num = i * 20
    # 设置访问所携带的参数
    cs = {
        "type": "5",
        "interval_id": "100:90",
        "action":"",
        "start": num,
        "limit": 20
    }
    # 存在反爬机制，需添加反反爬策略
    dic = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }

    # 发送get请求，接收返回数据
    resp = rq.get(url = url_add, params = cs, headers = dic)

    # 输出数据
    print(resp.json())
    print('---'*100)
    tt.sleep(1)