"""with open("./第二次有作业.txt","r") as file1:
    task=file1.read()
print(task)
作业：
翻页数据获取   每一位同学 自己抓一下异步加载的数据包  对比每个数据包的参数    构建每一页的参数发送请求
1采集十页数据(不能点击下一页抓包  只能通过向下滑动抓包！) 保存到本地为json格式数据  每30条数据保存到一个json格式文件
       提示:可以把每一页的数据保存到列表里面再通过    转换方法把列表转换成字符串类型数据 再写入json文件
       不然json文件会报错

2自己使用正则匹配车的价格和型号
提示
第1页： country=0&sort_new=hot_desc&city_name=%E6%88%90%E9%83%BD&limit=30&page=1
第2页： country=0&sort_new=hot_desc&city_name=%E6%88%90%E9%83%BD&limit=30&page=2
第3页：country=0&sort_new=hot_desc&city_name=%E6%88%90%E9%83%BD&limit=30&page=3
"""

import requests
import re
import json


class ClimbCar(object):
    # 静态属性
    def __init__(self):
        self.urls = "https://www.dongchedi.com/motor/pc/car/brand/select_series_v2"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            "cookie": "ttwid=1%7CpjAlR_h5bH0KLALBYDM--RXYH8vd9SLcynPIQMZbCOg%7C1667483837%7Ca193d8a75916923f802f20cba7986008f3039c4a8e526a48e37eae42cc257584; tt_webid=7161788507171276296; tt_web_version=new; MONITOR_WEB_ID=ed4931de-1628-43b5-b411-9e79644579b4; s_v_web_id=verify_la14tpn9_DIb8ihUI_XsGU_4NDY_ApCh_eo6AWLItrok9; _ga=GA1.2.904659687.1667483842; _gid=GA1.2.1551109384.1667483842; city_name=%E5%8D%97%E4%BA%AC; is_dev=false; is_boe=false; Hm_lvt_3e79ab9e4da287b5752d8048743b95e6=1667483839,1667568269; Hm_lpvt_3e79ab9e4da287b5752d8048743b95e6=1667568269; _gat_gtag_UA_138671306_1=1"
        }

    def RequCar(self, datas):
        # 发送请求
        response = requests.post(url=self.urls, headers=self.headers, data=datas)
        datas = response.content.decode()
        return datas

    # 保存数据
    def Savedata(self, jsdatastr):
        with open("小车.json", "w", encoding="utf-8") as file1:
            file1.write(jsdatastr)

    # 单纯采集网页数据 不清洗数据
    def Run(self):
        IsHarvest = 1
        datalst = []
        page = 10
        for i in range(page):
            datas = {
                "country": "0",
                "sort_new": "hot_desc",
                "city_name": "南京",
                "limit": "30",
                "page": i + 1
            }
            datasum = self.RequCar(datas)
            if IsHarvest == 0:
                # print(datasum) 字符串
                # 传换成字典格式
                jsdata = json.loads(datasum)
                # print(type(jsdata))  # <class 'dict'>
                # 以字典形式写入列表 直接以字符串写入列表格式会有错
                datalst.append(jsdata)

            else:
                style = re.findall('"outter_name":"(.*?)","pre_price"', datasum)
                # 车的起始价格
                official_price = re.findall('"official_price":"(.*?)","outter_name":', datasum)
                # print(style)
                # print(official_price)
                dataonepage = []
                for j in zip(style, official_price):
                    items = {
                        "style": j[0],
                        "price": j[1]
                    }
                    dataonepage.append(items)
                datalst.append(dataonepage)
            print(f"第{i + 1}页数据保存完毕")
        jsdatastr = json.dumps(datalst, ensure_ascii=False, indent="\t")
        self.Savedata(jsdatastr)


if __name__ == '__main__':
    car = ClimbCar()
    car.Run()
