# -*- coding = utf-8 -*-
# Time: 2022/5/11 16:27
# Author: Mr Wu
# File: __init__.py.py
# Software: PyCharm

# 1.引入requests
import requests as r

# 2.设置爬取的URL地址
url_add = "https://www.baidu.com"

# 3.开始爬取页面
resp = r.get(url=url_add)

# 4.输出返回的数据
resp.encoding = "utf-8"
print(resp.text)

# 5.保存返回的数据到文件中
with open("./baidu.html", "w", encoding="utf-8") as f:
    f.write(resp.text)

