# 导包
import requests
import time
import lxml
import csv
import re
from bs4 import BeautifulSoup
# 设置爬取地址
url_add = "https://www.piaohua.com/html/kongbu/index.html"
# 发送get请求，接收数据
resp = requests.get(url = url_add)
resp.encoding = "utf-8"
# 将响应字符转为BS4对象
page = BeautifulSoup(resp.text, "html.parser")
# 匹配出所有的电影
lst = page.find_all("li", attrs = {"class":"col-md-6"})
# 创建文件
f = open("kb.csv", mode ="w", encoding="utf-8")
csvwrite = csv.writer(f)
# 遍历每一部电影
for i in lst:
    href = "https://www.piaohua.com"+i.find("div", attrs = {"class":"pic"}).find("a").get("href")
    # 发送二次页面请求
    resp = requests.get(url = href)
    resp.encoding = "utf-8"
    html = lxml.etree.HTML(resp.text)
    content = "".join(html.xpath("/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/text()"))
    down = "".join(html.xpath("(/html/body/div[3]/div[2]/div/div[2]/div[2]/div[3]/ul/li/a/@href)"))
    name = re.search("◎片　　名(?P<n>.*?)◎",content).group("n")
    year = re.search("◎年　　代(?P<y>.*?)◎",content).group("y")
    address = re.search("◎产　　地(?P<a>.*?)◎",content).group("a")
    leibie = re.search("◎类　　别(?P<l>.*?)◎",content).group("l")
    director = re.search("◎导　　演(?P<d>.*?)◎",content).group("d")
    protagonist = list(re.search("◎主　　演(?P<p>.*?)◎",content).group("p"))
    csvwrite.writerow([name,year,address,leibie,director,protagonist[0],down])
    time.sleep(0.1)
f.close()
print("over")


