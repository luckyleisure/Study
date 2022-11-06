"""------------------2.json文件读写--------------"""
import json

####loads和load###
Isloads = False
with open("./小车.json", "r", encoding="utf-8") as file1:
    if Isloads:
        datacar = file1.read()
        print(datacar)
        print(type(datacar))  # <class 'str'>
        dictdata = json.loads(datacar)  # 字符串转list|dict       loads     传递的是字符串
        print(dictdata)
        print(type(dictdata))
    else:
        datacar = json.load(file1)  # 字符串转list|dict      load      传递的是文件对象
        print(datacar)
        print(type(datacar))  # <class 'list'>

####dumps和dump###
item = [
    [
        {
            "style": "星越L",
            "price": "13.72万"
        },
        {
            "style": "长安CS75 PLUS",
            "price": "11.79万"
        },
        {
            "style": "领克06",
            "price": "11.86万"
        }
    ]
]
print(type(item))
Isdumps = False
with open("车.json", "w", encoding="utf-8") as file2:
    if Isdumps:
        # 由于写入的参数必须是字符串类型的数据 所以需要在写入之前 讲数据转换成字符串
        # dumps 是把dict|list >>str  方法  方便进行文件写入
        strcar = json.dumps(item, ensure_ascii=False, indent="\t")
        file2.write(strcar)
    else:
        # dump  传递一个 文件对象  就能实现自动进行dict|list >>str  并且进行文件写入的操作
        json.dump(item, file2, ensure_ascii=False, indent="\t")

"""----------------------------3.jsonpath使用---------------------------------------"""
"""
重点语法介绍
$ 根节点   从哪个节点开始   $book
.或者[]   取子节点    节点与节点之间的过度
* 选取全部的意思     可以和[] 配合使用
..  不管在娜个位置  选择所有符合条件的条件   跨节点匹配最常用的语法符号!   最常和$配合使用
"""
from jsonpath import jsonpath

book_dict = {
    "store": {
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
}
# 使用jsonpath提取  title  author  price     认识jsonpath有点 缺点

# title
title = jsonpath(book_dict, "$..book[*].title")
print(title)
# author
author = jsonpath(book_dict, "$..book[*].author")
print(author)
# price
price = jsonpath(book_dict, "$..book[*].price")  # $..book.*.price  .*==[*]
print(price)
color = jsonpath(book_dict, "$..color")
print(color)
bycy_price = jsonpath(book_dict, "$..bicycle.price")
# bycy_price = jsonpath(book_dict, "$..store.bicycle.price")
print(bycy_price)

"""--------------------4.采集LoL英雄数据-------------------------------"""
"""
目的
采集https://101.qq.com/hero-detail?heroid=81&datatype=5v5
英雄名字  技能 皮肤数据  保存到本地为json文件!
"""
import requests
import json
from jsonpath import jsonpath
from fake_useragent import FakeUserAgent

urls = "https://game.gtimg.cn/images/lol/act/img/js/hero/81.js?ts=2779547"
useragent = FakeUserAgent().random
headers = {
    "user-agent": useragent
}
# 方法一：
# response = requests.get(url=urls, headers=headers)
# data = response.content.decode()
# print(data)  # "name":"\u63a2\u9669\u5bb6"  采集下来的数据 进行了 ascli转码 正常情况 ！ 直接进行josn文件转换
# jsdata = json.loads(data)
# print(jsdata)
# 方法二：
responses = requests.get(url=urls, headers=headers).json()
# print(type(responses),responses)
# 英雄名字
name = jsonpath(responses, "$..hero.name")
nick_name = jsonpath(responses, "$..hero.title")
print(name)
print(nick_name)
new_name = name[0] + nick_name[0]
print(new_name)
# 技能
skill = jsonpath(responses, "$..spells[*].name")
print(skill)
# 皮肤数据
skin = jsonpath(responses, "$..skins[*].name")
print(skin)
item = {
    "new_name": new_name,
    "skill": skill,
    "skin": skin

}
with open("lol.json", "w", encoding="utf-8") as file3:
    json.dump(item, file3, ensure_ascii=False, indent="\t")
