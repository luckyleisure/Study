"""
翻页数据获取   每一位同学 自己抓一下异步加载的数据包  对比每个数据包的参数    构建每一页的参数发送请求
1采集十页数据(不能点击下一页抓包  只能通过向下滑动抓包！) 保存到本地为json格式数据  每30条数据保存到一个json格式文件
       提示:可以把每一页的数据保存到列表里面再通过    转换方法把列表转换成字符串类型数据 再写入json文件
       不然json文件会报错

2自己使用正则匹配车的价格和型号
提示
第1页： country=0&sort_new=hot_desc&city_name=%E6%88%90%E9%83%BD&limit=30&page=1
第2页： country=0&sort_new=hot_desc&city_name=%E6%88%90%E9%83%BD&limit=30&page=2
第3页： country=0&sort_new=hot_desc&city_name=%E6%88%90%E9%83%BD&limit=30&page=3



流程
1.是采集翻页的汽车数据
做作业先完成  再完美   (先采集一页的数据,再采集多页的数据!)
翻页？    亘古不变的原理     抓翻页数据的重点!
涉及找每一个url对应的参数变化!

第一次 参数
country: 0
sort_new: hot_desc
city_name: 成都
limit: 30
page: 2

第二次 参数
country: 0
sort_new: hot_desc
city_name: 成都
limit: 30
page: 3

第三次 参数
country: 0
sort_new: hot_desc
city_name: 成都
limit: 30
page: 4

抓多页的数据包发现  page参数在变化  每次以1的值在递增

"""
#
import requests
import re
import json

url = "https://www.dongchedi.com/motor/pc/car/brand/select_series_v2"
# # 请求头
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "cookie": "ttwid=1%7C6jEs46CsofE7T0B7ssR9B1UDxvhPxAldbc081lT0WIo%7C1665571010%7C7aa598655f90b5bcbc0f8d996edd2a4002dbd62feabcd23034edd5133a1f19c3; tt_webid=7153572979443877407; tt_web_version=new; MONITOR_WEB_ID=9602a685-a787-4eb7-adca-7bac303f7e2c; _ga=GA1.2.547468968.1665571011; _gid=GA1.2.772147004.1665571011; s_v_web_id=verify_l95hz5fx_4KAGaUSJ_SzqY_48zb_9Ye7_gbnjJiUzgNpI; city_name=%E6%88%90%E9%83%BD; is_dev=false; is_boe=false; Hm_lvt_3e79ab9e4da287b5752d8048743b95e6=1665577029,1665581587,1665668310,1665750043; Hm_lpvt_3e79ab9e4da287b5752d8048743b95e6=1665750047"
}
# # 发送请求  采集多业数据 构建请求每一页数据的参数  data参数 type=dict
num = 1
# # 0 1 2
# 使用w重复被调用时 会覆盖原本的文件内容   这里只打开一次  所以用a  和w都可以
# a追加不会覆盖原来的内容
# w直接写入 并且覆盖
with open("懂车帝2.json", "w", encoding="utf-8") as file1:
    for i in range(num):
        data = {
            "country": "0",
            "sort_new": "hot_desc",
            "city_name": "成都",
            "limit": "30",
            "page": i + 1
        }
        response = requests.post(url=url, headers=headers, data=data)
        res_data = response.content.decode()
        print(res_data)
        # 数据清洗!  [xxx]  or  []
        # 写正则确认唯一性的标准   可以根据数据包的返回数据数量(30)乘请求的次数 根据自己搜索的关键字，看和数量是否能对上
        style = re.findall('"outter_name":"(.*?)","pre', res_data)
        price = re.findall(',"official_price":"(.*?)","out', res_data)
        print(style)
        print(price)
        print(len(price))
        print(len(style))
        # 手动写一个字典   写车子的价格和名字
        for i in zip(style, price):
            #
            item = {
                # (长安UNI-V,10.89万)
                "style": i[0],
                "peice": i[1]
            }
            # 由于写入的参数必须是字符串类型的数据 所以需要在写入之前 讲数据转换成字符串
            str_data = json.dumps(item, ensure_ascii=False, indent=2)
            file1.write(str_data + ",\n")

"""
采集翻页数据已经掌握   参数在变化  

采集二级目录数据?采集详情页数据    通过一级目录的二级目录url进行访问就叫向二级目录发送请求  
https://www.dongchedi.com/auto/series/5283   09 二级目录的url
https://www.dongchedi.com/auto/series/742    x6
https://www.dongchedi.com/auto/series/4637   阿尔法  
找二级目录url的重点     找每个二级目录url的关键参数     

目的向每个车子的二级目录发送请求获取数据
根据以上条件  发现 每个车子的前置url是固定的 https://www.dongchedi.com/auto/series/
数字在变化   需要在一级目录 找到能向二级目录发送请求的参数不定的可能是整体url/残缺的url/参数(重点)
发现每一个车的 参数都在 一级目录里面  
使用正则 匹配每个车的id 和 固定的url拼接     >>.得到了每个二级目录的url  >>>  可以向每个车子的二级目录发送请求获取数据  


"""

# 匹配二级目录url参数
url = "https://www.dongchedi.com/motor/pc/car/brand/select_series_v2"
# 请求头
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "cookie": "ttwid=1%7C6jEs46CsofE7T0B7ssR9B1UDxvhPxAldbc081lT0WIo%7C1665571010%7C7aa598655f90b5bcbc0f8d996edd2a4002dbd62feabcd23034edd5133a1f19c3; tt_webid=7153572979443877407; tt_web_version=new; MONITOR_WEB_ID=9602a685-a787-4eb7-adca-7bac303f7e2c; _ga=GA1.2.547468968.1665571011; _gid=GA1.2.772147004.1665571011; s_v_web_id=verify_l95hz5fx_4KAGaUSJ_SzqY_48zb_9Ye7_gbnjJiUzgNpI; city_name=%E6%88%90%E9%83%BD; is_dev=false; is_boe=false; Hm_lvt_3e79ab9e4da287b5752d8048743b95e6=1665577029,1665581587,1665668310,1665750043; Hm_lpvt_3e79ab9e4da287b5752d8048743b95e6=1665750047"
}
data = {
    "country": "0",
    "sort_new": "hot_desc",
    "city_name": "成都",
    "limit": "30",
    "page": 1
}
response = requests.post(url=url, headers=headers, data=data)
res_data = response.content.decode()
print(res_data)
idss = re.findall('"concern_id":(.*?),"', res_data)
print(idss)
print(len(idss))

gudingurl = "https://www.dongchedi.com/auto/series/"

for i in idss:
    second_url = gudingurl + i
    print(second_url)
