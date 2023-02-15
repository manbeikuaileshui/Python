# -*- coding = utf-8 -*-
# Time: 2022/5/18 19:50
# Author: Mr Wu
# File: 12-1.py
# Software: PyCharm

#网页解析，获取数据
import re
#正则表达式，进行文字匹配
from bs4 import BeautifulSoup
#制定URL，获取网页数据
import urllib.request,urllib.error
#进行Excel操作
import xlwt
#进行SQLite数据操作
import sqlite3

def main() :
    # 1.设置爬取数据的网址
    baseurl = "https://movie.douban.com/top250?start="

    # 2.爬取网页
    datalist = getData(baseurl)

    # 5.保存数据
    savepath = ".\\豆瓣电影Top250.xls"
    # saveData(savepath)
    askURl("https://movie.douban.com/top250?start=0")
# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10):  # 调用获取页面信息的函数，10次
        url = baseurl + str(i*25)
        html = askURl(url)  # 保存获取到的网页源码
        # 3.逐一解析数据

    return datalist

# 得到指定一个URL的网页内容
def askURl(url):
    # 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器(本质上是告诉浏览器，我们可以接收什么水平的文件内容)
    head = {  # 模拟浏览器头部信息，向豆瓣服务器发送信息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }
    request = urllib.request.Request(url, headers = head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

# 保存数据
def saveData(savepath):
    print("df")


if __name__ == "__main__":
    main()
