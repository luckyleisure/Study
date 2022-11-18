"""

直接使用单个ip进行数据采集 也可能被封ip
所以可以构建ip池
可以是  列表元祖..

ip_pool=list[ip1,ip2,ip3]

"""
import random
import requests
ip_pool=["60.170.204.30:8060","223.82.60.202:8060","58.20.184.187:9091"]
# 随机使用ip发送请求
ip=random.choice(ip_pool)

print(ip)

url="https://www.baidu.com/"

headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

proxies={
    "http":f"http://{ip}"
}

response=requests.get(url=url,headers=headers,proxies=proxies)

print(response.content.decode())








