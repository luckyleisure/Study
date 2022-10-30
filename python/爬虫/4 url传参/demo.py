"""-----------------1.useragent池的使用----------------------"""
"""
# 第一种方法:
# 需要先拿一个正确的ua  然后通过理性的方法重新声明新的ua，然后放到列表
# 循环遍历使用 不同ua
"""

ua_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
]

for ua in ua_list:
    headers1 = {
        "user-agent": ua
    }
    # print(ua)

"""
第二种使用随机的方法 获取ua
1随机索引
2直接随机值
for i in range(10):
  index=random.randint(0,len(ua_list)-1)
  print(index)
"""
import random

ua_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
]
# 1随机索引  由于列表只有3条数据  索引0开始 2结束 就写入0 2
index = random.randint(0, len(ua_list) - 1)
headers2 = {
    "user-agent": ua_list[index]
}
# print(headers2)
# 2直接随机值 通过random.choices随机获取ualist里面的ua   返回形式是一个包含了ua的列表
ua1=random.choices(ua_list)
ua2=random.choice(ua_list)
headers22 = {
    "user-agent": ua2
}
# print(headers22)
"""
# 通过第三方模块实现生成ua的功能
# fake-useragent  默认是属于联网
# pip install fake-useragent
# 导入的时候使用下划线导入
# 导入fake_useragent模块里面的FakeUserAgent类

# 配置
import os
import tempfile

__version__ = '0.1.11'
DB = os.path.join(
    tempfile.gettempdir(),
    'fake_useragent_{version}.json'.format(
        version=__version__,
    ),
)
print(DB)
"""
from fake_useragent import FakeUserAgent
# 注意FakeUserAgent是驼峰命令法
# 通过FakeUserAgent类的random方法 获取一个随机请求的ua
useragent=FakeUserAgent().random
print(useragent)
"""-----------------2.urlencode编码----------------------"""
from urllib.parse import quote,unquote
# quote进行中文转urlencode编码的方法
name="古天乐"
encodename=quote(name)
print(encodename)
# unquote进行 urlencode编码转中文的方法
mingname=unquote(encodename)
print(mingname)

"""-----------------3.url传参----------------------"""
import os
import requests
from fake_useragent import FakeUserAgent

# 1抓能传入不同参数的数据包
url="https://www.baidu.com/s?wd="
# 2写input 让用户进行输入
wd=input("请输入要搜索的关键字：")
# wd="古天乐"
# 3.拿网址和关键字进行拼接
newurl=url+wd
print(newurl)
# 4.发送请求获取响应
useragent=FakeUserAgent().random
print(useragent)
headers={
    "user-agent":useragent,
    "Cookie": "BIDUPSID=35DE82EBA87F1A7939F446F0A2F94852; PSTM=1667105886; BAIDUID=35DE82EBA87F1A79220A519743E7C759:FG=1; BD_HOME=1; H_PS_PSSID=26350; BD_UPN=12314753; BAIDUID_BFESS=35DE82EBA87F1A79220A519743E7C759:FG=1; BA_HECTOR=a4210l21a4a424a42h85ee081hls12q1b; ZFY=8NbVHcxLJqBx5q9syiNudM74uCYz8lyBdPeTLLCK9aU:C; delPer=0; BD_CK_SAM=1; PSINO=3; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; B64_BOT=1; BDRCVFR[FIXrT5n2Tgt]=mbxnW11j9Dfmh7GuZR8mvqV; channel=wappass.baidu.com; kleck=9cd59765404d88400e9256d4e27a174c; H_PS_645EC=82e7ASe7SXsdVvH6tQYNcJgrGlDKZZW8L409ql49AFnqxTzez%2FW3r12fgbarlHQSF%2BxBxtgMFXU; baikeVisitId=d82a257d-1cb9-40f0-917b-a4154d578486"

}
response=requests.get(url=newurl,headers=headers)
data=response.content.decode()
print(data)
# 5.保存到本地
with open(f"{wd}.html","w",encoding="utf-8") as file:
    file.write(data)


"""-----------------4.url传参方法----------------------"""

import os
import requests
from fake_useragent import FakeUserAgent

# 1抓能传入不同参数的数据包
url="https://www.baidu.com/s?"
# 2写input 让用户进行输入
wd=input("请输入要搜索的关键字：")
params={
    "wd":wd
}
useragent=FakeUserAgent().random
headers={
    "user-agent":useragent,
    "Cookie": "BIDUPSID=35DE82EBA87F1A7939F446F0A2F94852; PSTM=1667105886; BAIDUID=35DE82EBA87F1A79220A519743E7C759:FG=1; BD_HOME=1; H_PS_PSSID=26350; BD_UPN=12314753; BAIDUID_BFESS=35DE82EBA87F1A79220A519743E7C759:FG=1; BA_HECTOR=a4210l21a4a424a42h85ee081hls12q1b; ZFY=8NbVHcxLJqBx5q9syiNudM74uCYz8lyBdPeTLLCK9aU:C; delPer=0; BD_CK_SAM=1; PSINO=3; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; B64_BOT=1; BDRCVFR[FIXrT5n2Tgt]=mbxnW11j9Dfmh7GuZR8mvqV; channel=wappass.baidu.com; kleck=9cd59765404d88400e9256d4e27a174c; H_PS_645EC=82e7ASe7SXsdVvH6tQYNcJgrGlDKZZW8L409ql49AFnqxTzez%2FW3r12fgbarlHQSF%2BxBxtgMFXU; baikeVisitId=d82a257d-1cb9-40f0-917b-a4154d578486"

}
response=requests.get(url=url,headers=headers,params=params)
data=response.content.decode()
print(data)
