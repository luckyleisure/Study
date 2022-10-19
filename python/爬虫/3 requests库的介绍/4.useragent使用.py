"""

user-agent  用户代理 本次请求使用的身份是什么   可以是 谷歌浏览器  360浏览器 xxxxx
User-Agent

和爬虫有什么关系?
服务器会对请求进行字段验证， 其中就包括 ua 检测到不是一个 正常的设备而是一个 第三方库  就会不返回数据  返回错误数据

反反爬操作
模拟真实用户发送请求
在请求的时候 伪造useragent 在请求头里面发送请求

如何添加
需要在 数据包的requests.headers里面找到 关键字段 user-agent
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36

添加useragent到请求头 需要以键值对形式进行请求头的添加

可能会出现的问题
1.遇到百度验证
    原因 请求次数频繁会涉及封 ua 或者 严重点 ip
    解决 可以参考后面的学习内容  加cookie （构建在headers里面的字段）
2.访问百度的时候 报ssl错误
    执行 绕过ssl验证的操作
    在get方法里面 加 verify=False参数 绕过ssl验证
"""
import requests
# 确认url
url="https://www.baidu.com/"

# 请求信息  字典
# 默认使用headers作为请求头变量  字典
# 写useragent的重要操作步骤   不要犯的错误
# 不要在useragent的前面 加空格
headers={

    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
# 对百度发送请求并且返回响应内容
# 请求头 前面的关键字参数不能变化  必须是 headers
# ,verify=False 绕过ssl验证
response=requests.get(url=url,headers=headers,verify=False)
# 返回字符类型的数据
data=response.content.decode()
print(data)
print(type(data))
# 文件保存
with open("百度4.html","w",encoding="utf-8")as file1:
    file1.write(data)





