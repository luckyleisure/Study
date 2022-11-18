"""
业务场景   以高频率采集网页的数据   （暴露自己ip的），如果ip访问频率过高被监测    封ip！  （不能采集数据！）
ip?
确认你这台计算机在互联网上的身份信息 192.168.xx.xx

查看ip的方法:
cmd  >>ipconfig

8


不论使用什么类型的ip  都不是只有一个ip
代理平台会给你一个请求ip的接口url    >>>  一个列表[ip1,ip2,ip3]

怎么获取代理？
通过代理平台
https://free.kuaidaili.com/free/

如何在进行数据采集时带入代理作用？
代理是通过proxies 关键参数进行传递的
可以构建到post/get请求的方法里面去

构建形式:字典


"""
import requests
# 构建代理参数
# proxies={
#     "http":"http://223.82.60.202:8060"
# }
# 
# url="https://www.baidu.com/"
#
# headers={
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
# }
#
# response=requests.get(url=url,headers=headers,proxies=proxies)
#
# print(response.content.decode())




























