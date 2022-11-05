"""-----------2.异步加载数据包获取------------------------------"""
import requests
import re

urls = "https://www.dongchedi.com/motor/pc/car/brand/select_series_v2"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "cookie": "ttwid=1%7CpjAlR_h5bH0KLALBYDM--RXYH8vd9SLcynPIQMZbCOg%7C1667483837%7Ca193d8a75916923f802f20cba7986008f3039c4a8e526a48e37eae42cc257584; tt_webid=7161788507171276296; tt_web_version=new; MONITOR_WEB_ID=ed4931de-1628-43b5-b411-9e79644579b4; s_v_web_id=verify_la14tpn9_DIb8ihUI_XsGU_4NDY_ApCh_eo6AWLItrok9; _ga=GA1.2.904659687.1667483842; _gid=GA1.2.1551109384.1667483842; city_name=%E5%8D%97%E4%BA%AC; is_dev=false; is_boe=false; Hm_lvt_3e79ab9e4da287b5752d8048743b95e6=1667483839,1667568269; Hm_lpvt_3e79ab9e4da287b5752d8048743b95e6=1667568269; _gat_gtag_UA_138671306_1=1"
}
data = {
    "country": "0",
    "sort_new": "hot_desc",
    "city_name": "南京",
    "limit": "30",
    "page": "5"
}
response = requests.post(url=urls, headers=headers, data=data)
datas = response.content.decode()
# print(type(datas),datas)
# 匹配数据
# 车的型号
style = re.findall('"outter_name":"(.*?)","pre_price"', datas)
# print(len(style))
# print(style)
# 车的起始价格
official_price = re.findall('"official_price":"(.*?)","outter_name":', datas)
# print(len(official_price))
# print(official_price)
# 保存数据
with open("小车.txt", "w", encoding="utf-8") as file1:
    for i in zip(style, official_price):
        print(i)
        item = str(i)
        file1.write(item + "\n")
"""-----------5.数据的转换------------------------------"""

import requests
import re
import json

urls = "https://www.dongchedi.com/motor/pc/car/brand/select_series_v2"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "cookie": "ttwid=1%7CpjAlR_h5bH0KLALBYDM--RXYH8vd9SLcynPIQMZbCOg%7C1667483837%7Ca193d8a75916923f802f20cba7986008f3039c4a8e526a48e37eae42cc257584; tt_webid=7161788507171276296; tt_web_version=new; MONITOR_WEB_ID=ed4931de-1628-43b5-b411-9e79644579b4; s_v_web_id=verify_la14tpn9_DIb8ihUI_XsGU_4NDY_ApCh_eo6AWLItrok9; _ga=GA1.2.904659687.1667483842; _gid=GA1.2.1551109384.1667483842; city_name=%E5%8D%97%E4%BA%AC; is_dev=false; is_boe=false; Hm_lvt_3e79ab9e4da287b5752d8048743b95e6=1667483839,1667568269; Hm_lpvt_3e79ab9e4da287b5752d8048743b95e6=1667568269; _gat_gtag_UA_138671306_1=1"
}
data = {
    "country": "0",
    "sort_new": "hot_desc",
    "city_name": "南京",
    "limit": "30",
    "page": "5"
}
response = requests.post(url=urls, headers=headers, data=data)
datastr = response.content.decode()
print(type(datastr))
data = json.loads(datastr)
print(type(data), data)
strdata = json.dumps(data, ensure_ascii=False, indent="\t")
print(type(strdata), strdata)
with open("车.json", "w", encoding="utf-8") as file1:
    file1.write(strdata)
