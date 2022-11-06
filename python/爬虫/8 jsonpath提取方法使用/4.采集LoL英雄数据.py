"""
目的
采集https://101.qq.com/#/hero-detail?heroid=81&datatype=5v5
英雄名字  技能 皮肤数据  保存到本地为json文件!



"""
import json

import requests
from jsonpath import jsonpath

url = "https://game.gtimg.cn/images/lol/act/img/js/hero/81.js?ts=2776259"

# 请求头
# 如果发现数据包没有requests header  就随便找一个有ua的数据包复制ua
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
response = requests.get(url=url, headers=headers).json()
# 相当于执行了 json.loads(response.content.decode())
print(type(response))

# 使用了response使用了json方法以后就不能再使用  content.decode()了
# res_data=response.content.decode()
# teError: 'dict' object has no attribute 'content'
print(response)

# 英雄名字
name = jsonpath(response, '$..hero.name')
nick_name = jsonpath(response, '$..hero.title')
print(name)
print(nick_name)
hero = name[0] + nick_name[0]
print("hero", hero)
# 皮肤数据
skins = jsonpath(response, "$..skins[*].name")
print(skins)
# 技能
spells = jsonpath(response, "$..spells[*].name")
print(spells)
item = {
    "hero": hero,
    "skins": skins,
    "spells": spells
}
with open("小黄毛.json", "w", encoding="utf-8") as file1:
    json.dump(item, file1, ensure_ascii=False, indent=2)

"""
"\u63a2\u9669\u5bb6", 采集下来的数据 进行了 ascli转码 正常情况 ！ 
直接进行josn文件转换   

"""
