"""
https://bj.lianjia.com/ershoufang/dongcheng/pg1/
目的 采集该网页下的 房产信息
字段   1.标题名  2.标价  3.平方价格  4.户型  5.房屋大小

流程
1.抓取包含数据的数据包      html
2.需要进行数据转换!   str  >>  element    element.xpath()方法清洗
    pip install lxml  加源
    导入
    from lxml import etree
3.在进行数据的保存

tips1
在response标签里面全局搜索时  没有搜到可以尝试删减字符串
因为可能网页上的数据是不同标签拼起来的！
tips2
在清洗任何类型数据之前，都先进行所有字符串的打印   验证有没有数据 ！

"""
#
import json

from lxml import etree
import requests
url="https://bj.lianjia.com/ershoufang/dongcheng/pg1/"

# 请求头
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Cookie": "lianjia_uuid=7596eb35-9207-4910-bde1-0c408de4e5a8; _smt_uid=62878bc2.48e47083; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22180e179ef88ad7-0f7a05087685d5-14333270-2073600-180e179ef89ed0%22%2C%22%24device_id%22%3A%22180e179ef88ad7-0f7a05087685d5-14333270-2073600-180e179ef89ed0%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _ga=GA1.2.2134984698.1653050308; _jzqckmp=1; _gid=GA1.2.1405564914.1666002900; gr_user_id=7f98d005-7979-4f26-a79d-1bc6c49b2163; select_city=110000; lianjia_ssid=ffeba38c-075f-4a20-806d-ed197ecb351f; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1666002899,1666003493,1666012872; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1666012872; _qzja=1.1858172798.1653050306451.1666003492689.1666012872691.1666003492689.1666012872691.0.0.0.34.14; _qzjc=1; _qzjto=3.3.0; _jzqa=1.631410031018479600.1653050306.1666003493.1666012873.16; _jzqc=1; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMTg2Mjc4ZGZhZGMwODUyZGUwZDk0YmNhNDQ2ZmU2OTY4NGE3ZDZjMmY5OTMxZDJmZjgxZWYyYzA0ZGU3YzIzMzJhOTY1MThlMzEwYzVhMjc0Yzg5OGIwYTIwNzI0NDRiNzBkZmFjNjM3NTE5NGNkMjQzOTNkZTRhZTFkMDA4YTY1YWIyZjA5ZGM1ODU4ODE3MzNkYTVkMTNjMGUyZDBiZjFlZmFhYzkyZmZkOGE0ZWI3NDBlYWE1OTZlN2ZmYzUxZGQ2OGMzZDRjYTk1NmU3YTljMzdmYWNiZjAyY2QxNWE4NTdmZjNiOWM4NTRlNmY4MmI5MzU1MzA4YmE1NDIwYlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJhNDI2OWRlMFwifSIsInIiOiJodHRwczovL2JqLmxpYW5qaWEuY29tL2Vyc2hvdWZhbmcvZG9uZ2NoZW5nL3BnMS8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ==; _jzqb=1.1.10.1666012873.1; _qzjb=1.1666012872691.1.0.0.0"
}
response=requests.get(url=url,headers=headers)
# 返回响应内容
res_data=response.content.decode()
print(res_data)
print(type(res_data)) #<class 'str'>
# 数据类型转换  str  >>element    目的使用 element的xpath方法
# 通过etree模块的HTML方法   把str类型的响应转换成了 element类型响应
html=etree.HTML(res_data)
print(html) #<Element html at 0x191e8339888>
# 使用element对象的xpath语法时 不会有提示是正常的
# 1.标题名
# 写xpath语法的重点
# 1通过节点的属性确定节点的唯一性
# 2通过指定排名选中父节点下面的兄弟节点   从1开始  不是从0开始
# 3xpath语法最外面的字符串都用单引号！
# 4xpath没有匹配到数据返回空列表!       很重要的机制！
# 5xpath没有匹配到数据的处理方法
#     1打印网页数据  看数据有没有返回     没有数据  考虑被反扒了  加反扒字段
#     2打印网页数据  看数据有没有返回     有数据    xpath语法写错了    重新写
title=html.xpath('//div[@class="info clear"]/div[1]/a/text()')

# 2.标价
price=html.xpath('//div[@class="info clear"]/div[6]/div[1]/span/text()')
print(price)
# 3.平方价格
size_price=html.xpath('//div[@class="info clear"]/div[6]/div[2]/span/text()')
# 4.户型
print(size_price)
huxing=html.xpath('//div[@class="info clear"]/div[3]/div/text()')
newhuxing_list=[]
# 5.房屋大小
home_size=[]
# hx=2室1厅 | 65.18平米 | 东 西 | 精装 | 顶层(共6层) | 1991年建 | 板楼
for hx in huxing:
    hx_list=hx.split(' | ')
    print(hx_list)
    newhuxing_list.append(hx_list[0])
    home_size.append(hx_list[1])
# 关于json文件 保存
# json文件只支持保存 一个字典 或是一个列表  不然文件报错
# 所以可以在循环最外面加一个列表  放需要保存的数据
data_list=[]
with open("链家.json","w",encoding="utf-8")as file1:
    for i in zip(title,price,size_price,newhuxing_list,home_size):
        item={
            "title":i[0],
            "price":i[1]+"万",
            "size_price":i[2],
            "huxing":i[3],
            "home_size":i[4]
        }
        # 把所有的字典添加到列表里面
        data_list.append(item)
    # 需要跳出循环再进行数据转换   再写入文件！
    str_data=json.dumps(data_list,ensure_ascii=False,indent=2)
    file1.write(str_data)


# print(title)
# print(price)
# print(size_price)
# print(newhuxing_list)
# print(home_size)
# print(len(title))
# print(len(price))
# print(len(size_price))
# print(len(newhuxing_list))
# print(len(home_size))







