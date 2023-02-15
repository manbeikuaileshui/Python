# -*- coding = utf-8 -*-
# Time: 2022/5/11 16:39
# Author: Mr Wu
# File: 11-2.py
# Software: PyCharm

# 1.引入requests
import requests as rp

# 2.设置爬取的URL地址
name = input('请输入你要搜索的明星：')
url_add = "https://www.sogou.com/web?query={}".format(name)

# 3.存在反爬虫机制，需添加反反爬虫的策略
dic = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

# 4.开始爬取数据
resp = rp.get(url = url_add, headers = dic)

# 5.输出返回的数据
resp.encoding = "utf-8"
print(resp.text)

# 6.保存返回的数据到文件中
with open("./sogou.html", "w", encoding="utf-8") as f:
    f.write(resp.text)