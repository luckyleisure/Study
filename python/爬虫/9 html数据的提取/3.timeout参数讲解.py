"""
有个别ip 响应时间过长  会导致采集效率降低  超过16秒自动报链接错误
所以需要将响应时间长的ip剔除!
需要使用到post/get方法的  timeout参数
timeout参数作用:在x秒后没有响应内容返回  抛出异常!


"""
import random
import requests
ip_pool=["60.170.204.30:8060","115.82.55.99:8060","58.20.184.187:9091"]

url="https://www.baidu.com/"

headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
for ip in ip_pool:
    try:
        proxies={
            "http":f"http://{ip}"
        }
        # timeout=3代表  如果本次请求的响应时间超过3秒  就抛出异常!
        response=requests.get(url=url,headers=headers,proxies=proxies,timeout=3)
        print("清洗数据保存数据!")
    except Exception as e:
        print("报错信息为:",e)

























