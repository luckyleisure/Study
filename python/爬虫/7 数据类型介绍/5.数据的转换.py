

import json
import requests
# url = "https://www.dongchedi.com/motor/pc/car/brand/select_series_v2"
#
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
#     "cookie": 'cookie: ttwid=1%7C6jEs46CsofE7T0B7ssR9B1UDxvhPxAldbc081lT0WIo%7C1665571010%7C7aa598655f90b5bcbc0f8d996edd2a4002dbd62feabcd23034edd5133a1f19c3; tt_webid=7153572979443877407; tt_web_version=new; MONITOR_WEB_ID=9602a685-a787-4eb7-adca-7bac303f7e2c; _ga=GA1.2.547468968.1665571011; _gid=GA1.2.772147004.1665571011; s_v_web_id=verify_l95hz5fx_4KAGaUSJ_SzqY_48zb_9Ye7_gbnjJiUzgNpI; city_name=%E6%88%90%E9%83%BD; is_dev=false; is_boe=false; Hm_lvt_3e79ab9e4da287b5752d8048743b95e6=1665571011,1665573831,1665574550,1665577029; Hm_lpvt_3e79ab9e4da287b5752d8048743b95e6=1665578084'
# }
# data = {
#     "country": "0",
#     "sort_new": "hot_desc",
#     "city_name": "成都",
#     "limit": "30",
#     "page": "3"
# }
# response=requests.post(url=url,headers=headers,data=data)
# # 返回字符串类型的数据
# datas=response.content.decode()
# print(datas)
# print(type(datas))  #<class 'str'>
# 直接从网页上采集下来的数据类型都是   str类型的  不论是在网页上看着是json的还是html的

# 执行第一步  str > python类型的数据(dict|list)  取决于 网页上的数据是像字典的还是像list的

str111="""
{"data":"哪吒汽车"}
"""
print(type(str111))  #<class 'str'>
# 把str111转换成python处理的数据  通过json模块     python自带的 不要下载直接导入
datassss=json.loads(str111)
# print(type(datassss))  #<class 'dict'>
# 转换过以后成了 字典  或者列表   就可以进行索引取值的操作    或者使用jsonpath进行提取!
# 字典|列表   转换成 str      dict|list >> str
# ensure_ascii=False 不对保存的数据进行转码
# indent= 2   每条数据的提行是2个空格
str_data=json.dumps(datassss,ensure_ascii=False,indent=2)
print(str_data)
print(type(str_data))
with open("懂车帝1.json","w",encoding="utf-8")as file1:
    file1.write(str_data)
"""

 raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 3 column 1 (char 2)
报错原因是因为  需要被转换的在网页上看起来像列表|字典的数据 不对称

"""




