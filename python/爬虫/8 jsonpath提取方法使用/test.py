"""
# unicode-escape ignore

1.dump dumps 和load loads的区别

2.jsonpath的提取语法掌握

3.jsonpath提取不同节点 但有相同键名的数据时 应该如何处理才能达到数据的精确提取?

https://101.qq.com/#/hero-detail?heroid=81&datatype=5v5









1.什么同步加载 什么是异步加载?
答:
(1)同步请求 则是每次获取新的数据  都需要进行请求 但是会（覆盖原来的数据）的请求
(2)异步请求则是获取新数据是不需要进行页面刷新（即不会覆盖原本的数据）依旧能获取新数据 的请求

2.同步异步的数据包在抓包方法上有区别吗？  数据清洗方法有区别吗？
答:没有区别，都是通过network      都用正则则没有区别

3.关于爬虫爬取的网络数据中 最常见的是哪几种数据类型?
答:json格式（上课讲的）   html格式

4.对json格式数据可以运用到哪些方式进行数据清洗?
答:
1.目前讲了正则   因为都是字符串
2.转换成json(python里面的dict数据类型)格式数据
json模块
json.loads字符串转json字典    str>dict
通过python对字典键取值的形式对数据进行提取




"""
import json

word = """
{"store": {
    "book": [
        {"category": "reference",
         "author": "Nigel Rees",
         "title": "Sayings of the Century",
         "price": 8.95
         },
        {"category": "fiction",
         "author": "Evelyn Waugh",
         "title": "Sword of Honour",
         "price": 12.99
         },
        {"category": "fiction",
         "author": "Herman Melville",
         "title": "Moby Dick",
         "isbn": "0-553-21311-3",
         "price": 8.99
         },
        {"category": "fiction",
         "author": "J. R. R. Tolkien",
         "title": "The Lord of the Rings",
         "isbn": "0-395-19395-8",
         "price": 22.99
         }
    ],
    "bicycle": {
        "color": "red",
        "price": 19.95
    }
}
}"""

style = ['长安UNI-V', '宋PLUS DM-i', '领克03', '星越L', '哈弗H6', '星瑞', '五菱宏光MINIEV', '长安CS75 PLUS', '红旗H5', '艾瑞泽8', '汉DM',
         '坦克300', '逸动', '海豹', '秦PLUS DM-i', '海豚', '传祺M8', '唐DM', '汉EV', '帝豪', '领克06', '红旗HS5', '长安CS55 PLUS', '哈弗大狗',
         'ZEEKR 001', '长安深蓝SL03', '五菱星辰', '缤越', '锐程PLUS', '元PLUS']
price = ['10.89万', '15.28万', '13.68万', '13.72万', '9.89万', '11.37万', '3.28万', '11.79万', '15.98万', '10.89万', '21.58万',
         '19.88万', '7.29万', '20.98万', '11.18万', '10.28万', '17.98万', '20.58万', '21.48万', '6.99万', '11.86万', '18.38万',
         '9.29万', '11.99万', '29.90万', '16.89万', '6.98万', '7.58万', '9.99万', '13.78万']

for i in zip(style, price):
    print(i)
    item = {
        # (长安UNI-V,10.89万)
        "style": i[0],
        "price": i[1]
    }
    # print(item)
