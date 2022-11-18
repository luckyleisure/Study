"""-----------------------------1.代理ip使用--------------------------"""
"""
业务场景   以高频率采集网页的数据   （暴露自己ip的），如果ip访问频率过高被监测    封ip！  （不能采集数据！）
ip?
确认你这台计算机在互联网上的身份信息 192.168.xx.xx

查看ip的方法:
cmd  >>ipconfig

代理ip是什么？
也是一个ip地址
作用:可以帮我们发送请求  从而不暴露自己的ip    从而达到反反爬的效果!
代理ip访问次数过多 也是会被反扒! 所以可以有几种ip 供我们使用!

ip的分类
匿名代理ip      》》》 服务端知道我们使用了代理ip，但是不知道我们的真实ip
高匿代理ip      》》》服务端不知道我们使用了代理ip，而且不知道我们的真实ip
"""
import requests

url = "https://www.baidu.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
proxies = {
    "http": "http://223.96.90.216:8085"
}
response = requests.get(url=url, headers=headers, proxies=proxies)
data = response.content.decode()
print(data)

"""-----------------------------2.ip池--------------------------"""
"""

直接使用单个ip进行数据采集 也可能被封ip
所以可以构建ip池
可以是  列表元祖..

ip_pool=list[ip1,ip2,ip3]

"""
import requests
import random

ip_pool = ["183.247.202.208:30001", "60.170.204.30:8060", "223.96.90.216:8085"]
ip = random.choice(ip_pool)
url = "https://www.baidu.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
proxies = {
    "http": f"http://{ip}"
}

response = requests.get(url=url, headers=headers, proxies=proxies)
data = response.content.decode()
print(data)
"""-----------------------------3.timeout参数讲解--------------------------"""
import requests

url = "https://www.baidu.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
ip_pool = ["183.247.202.208:30001", "60.170.204.30:8060", "223.96.90.216:8085"]
for ip in ip_pool:
    try:
        proxies = {
            "http": f"http://{ip}"
        }
        # print(ip)
        # timeout=3代表  如果本次请求的响应时间超过3秒  就抛出异常!
        response = requests.get(url=url, headers=headers, proxies=proxies, timeout=0.1)
        data = response.content.decode()
        print("清洗数据保存数据!")
    except Exception as e:
        print("错误：", e)

"""-----------------------------6.案例讲解解--------------------------"""
"""
重点掌握语法！
nodename      / div/span/li/p.......  网页里面的标签 就可以称之为一个nodename
/      元素与元素之间的过度
//     不管节点在哪个位置，直接从那个节点开始匹配数据
@            匹配属性数据   ref="https://top.baidu.com/board?platform=pc&amp;sa=pcindex_entry"  xx=属性数据
text()       匹配文本类型数据  itle-content-title">二十大首场记者招待会</span> >文本数据<


目的 采集该网页下的 房产信息
字段   1.标题名  2.标价  3.平方价格  4.户型  5.房屋大小
https://bj.lianjia.com/ershoufang/dongcheng/pg1/
"""
import requests
from lxml import etree
import json
from fake_useragent import FakeUserAgent

url = "https://bj.lianjia.com/ershoufang/dongcheng/pg1/"
us = FakeUserAgent().random
headers = {
    "user-agent": us
}
response = requests.get(url=url, headers=headers)
str_data = response.content.decode()
# print(str_data)
html = etree.HTML(str_data)
# print(html)
# 1.标题名
title = html.xpath('//div[@class="info clear"]/div/a/text()')
# print(len(title), title)
# 2.标价
price = html.xpath('//div[@class="info clear"]/div[6]/div[1]/span/text()')
# print(len(price), price)

# 3.平方价格
per_price = html.xpath('//div[@class="info clear"]/div[6]/div[2]/span/text()')
# print(len(per_price), per_price)

layout = html.xpath('//div[@class="info clear"]/div[3]/div/text()')
# print(len(layout), layout)
# 4.户型

new_layout = []
# 5.房屋大小
housesize = []
for i in layout:
    # print(type(i))
    layoutlst = i.split(" | ")
    new_layout.append(layoutlst[0])
    housesize.append(layoutlst[1])

singlehouse = []
with open("链家.json", "w", encoding="utf-8") as file1:
    for i in zip(title, price, per_price, new_layout, housesize):
        items = {
            "title": i[0],
            "price": i[1] + "万",
            "per_price": i[2],
            "layout": i[3],
            "housesize": i[4]
        }
        singlehouse.append(items)
    json.dump(singlehouse, file1, ensure_ascii=False, indent="\t")
