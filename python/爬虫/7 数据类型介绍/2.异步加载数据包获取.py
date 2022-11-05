"""
同步加载数据包和异步加载的数据包在请求方法上有没有区别?
没有不同  都是通过request库发送请求     参数构建好即可
构建协议的时候也是一样的     写在headers里面 即可

目的 采集懂车的车子信息
    字段  1款式  2起始价格

https://www.dongchedi.com/auto/library/x-x-0-x-x-x-x-x-x-x-x

判断 一个网页是不是异步加载的数据包     上下滑动(看玩也是否会进行异步请求)
抓包过程中  发现有数据在某个数据包里面时要进行判断  要进行多个数据的验证    如果多条数据都在数据包内 则是真实的数据包
如果遇到网页加载的数据和数据包不符的情况   以数据包返回的为准  （不能控制！）
"""

import requests
import re
# 请求车子数据的接口
url = "https://www.dongchedi.com/motor/pc/car/brand/select_series_v2"

# 请求头
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "cookie": 'cookie: ttwid=1%7C6jEs46CsofE7T0B7ssR9B1UDxvhPxAldbc081lT0WIo%7C1665571010%7C7aa598655f90b5bcbc0f8d996edd2a4002dbd62feabcd23034edd5133a1f19c3; tt_webid=7153572979443877407; tt_web_version=new; MONITOR_WEB_ID=9602a685-a787-4eb7-adca-7bac303f7e2c; _ga=GA1.2.547468968.1665571011; _gid=GA1.2.772147004.1665571011; s_v_web_id=verify_l95hz5fx_4KAGaUSJ_SzqY_48zb_9Ye7_gbnjJiUzgNpI; city_name=%E6%88%90%E9%83%BD; is_dev=false; is_boe=false; Hm_lvt_3e79ab9e4da287b5752d8048743b95e6=1665571011,1665573831,1665574550,1665577029; Hm_lpvt_3e79ab9e4da287b5752d8048743b95e6=1665578084'
}
# 复制cookie构建到headers里面去以后  保存   可能是cookie里面的引号和自定义的引号冲突

# data参数
data = {
    "country": "0",
    "sort_new": "hot_desc",
    "city_name": "成都",
    "limit": "30",
    "page": "3"
}
# 发送请求
response=requests.post(url=url,headers=headers,data=data)
# 返回字符串类型的数据
datas=response.content.decode()
print(datas)
# 清洗数据！
# 1款式  2起始价格
# 根据语法匹配，匹配数据以后，返回包含数据的列表       没有匹配到数据 返回空列表!   特性很重要! 重点!
# findall参数1  正则表达式  ，参数2 需要被匹配的字符串
# 正则 匹配数据的重点!   1需要确定要的数据在哪  传祺M6      2写前标杆和后标杆的正则表达式
"""
"outter_name":"奕炫MAX","pre_price       需要的数据>>>奕炫MAX  
前标杆  "outter_name":"
后标杆  ","pre_price
要的数据用   (.*?)  分组匹配前标杆 后标杆之间的所有数据 

123
143
153
[2,4,5]
"""
# 车的型号
style=re.findall('"outter_name":"(.*?)","pre_price"',datas)
print(style)
print(len(style))
# # 车的起始价格
official_price=re.findall('"official_price":"(.*?)"',datas)
print(official_price)
print(len(official_price))
# 写正则的时候要确认正则的唯一性   降低通配型
# 要学会变通   前标杆不能确认唯一性   写后标杆
# 后标杆也不能确认唯一性   需要被匹配到数据也能作为标杆
# official_price=re.findall('"brand_name":"(.*?车)"',datas)
# print(official_price)
# 保存数据！
with open("车子.txt","w",encoding="utf-8")as file1:
    for i in zip(style,official_price):
        item=str(i)
        print(item)
        file1.write(item+"\n")

# 翻页数据获取   每一位同学 自己抓一下异步加载的数据包  对比每个数据包的参数    构建每一页的参数发送请求
#

