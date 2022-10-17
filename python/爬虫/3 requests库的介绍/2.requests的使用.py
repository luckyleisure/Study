"""
完成练习
采集百度首页的数据，并将其保存到本地的html文件
小知识  网页首页数据包基本都是html类型的数据
完成的步骤
1采集
    1.1抓包(确认要采集的数据百度首页)url
    1.2向url发送请求 获取响应
2保存
    2.1 with open函数保存html文件
"""
# 导入模块
import requests

# 数据包
# 1.1抓包(确认要采集的数据百度首页)url
# url:资源定位符/资源地址 链接  包含了渲染网页的数据的数据包
# 要抓数据包 就得做生成数据包的操作     抓登录数据包 翻页数据包/ 抓包的重点操作
# Request URL: https://www.baidu.com/资源地址
# 通过response的响应内容确认url

url="https://www.baidu.com/"
# # 常用的有get 和post方法
# # 通过数据包下面的
# # Request Method: GET 决定requests.使用方法
# # 通过requests库的get方法 向https://www.baidu.com/发送http请求   服务器返回了 对应的响应对象(response默认)
response=requests.get(url=url)
print(response) #<Response [200]> 本次请求的响应码是 200
print(type(response))  #<class 'requests.models.Response'>
# # 查看响应的文本信息  通过response.text数据方法
# # 自动的对文本类型数据进行解码  而且使用的是 网页自己的编解码方法
data=response.text
print(data)
# # 出现问题 返回的数据  中文位置变成了乱码
# # 产生的原因  是因为 网页自己使用了自己的编码形式进行编解码(对中文) ，但是到了utf-8的文件里面就会是乱码的情况
# # 解决方法 是手动的声明response的编码  改成utf-8  手动进行解码
print(response.encoding)    #ISO-8859-1
response.encoding="utf-8"
print(response.encoding)
# # 查看响应的文本信息  通过response.text数据方法
data=response.text
# print(type(data))  #<class 'str'>
print(data)
# # 操作文件的函数
# # 参数1文件名.类型   参数2 file_method文件操作方式(读r/写w) 参数3指定文件编码 encoding=utf-8
# # 百度.html
# # 声明了一个对百度.html文件操作的文件对象  叫file1
# # 第二个参数 w代表 使用字符类型数据进行写入
with open("百度.html","w",encoding="utf-8")as file1:
    file1.write(data)
# 出现问题
# 在html文件里面点击谷歌浏览器报错  手动配置谷歌浏览器的路径
# C:\Program Files\Google\Chrome\Application
# File>>settings>>Tool>>web browser >>找到谷歌 点击右边的文件夹  根据以上路径找到chrome.exe指定浏览器  即可

# 第二种返回文本类型数据的方法     以后进行数据的清洗
# response.content 响应数据以字节类型进行返回
# response.content.decode方法
url="https://www.baidu.com/"
response=requests.get(url=url)
# response.content.decode方法 是对字节类型数据进行解码  默认的解码方式是utf-8解码方式
datas=response.content.decode()
print(datas)
# with open("百度2.html","w",encoding="utf-8")as file2:
#     file2.write(datas)
#
# # 第三种方式保存文件
url="https://www.baidu.com/"
response=requests.get(url=url)
# response.content.decode方法 是对字节类型数据进行解码  默认的解码方式是utf-8解码方式
datas=response.content
print(datas)
# 文件操作的第三种方式  wb 代表数据以字节类型写入
# 写入数据的重点  以字节类型对文件进行写入 不需要指定编码
with open("百度3.html","wb")as file2:
    file2.write(datas)





