import requests
import os
import time

'''

# 通过response的响应内容确认url
urls = "https://www.baidu.com/?tn=49055317_3_hao_pg"
# 通过requests库的get方法 向https://www.baidu.com/发送http请求   服务器返回了 对应的响应对象(response默认)
responses1 = requests.get(url=urls)
# print(responses) #<Response [200]>
# print(type(responses)) #<class 'requests.models.Response'>
# 查看响应的文本信息  通过response.text数据方法
# 自动的对文本类型数据进行解码  而且使用的是 网页自己的编解码方法
# data=responses.text
# print(data)
# 出现问题 返回的数据  中文位置变成了乱码
# 产生的原因  是因为 网页自己使用了自己的编码形式进行编解码(对中文) ，但是到了utf-8的文件里面就会是乱码的情况
# 解决方法 是手动的声明response的编码  改成utf-8  手动进行解码
# print(responses.encoding) #ISO-8859-1
responses1.encoding = "utf-8"
# print(responses.encoding)
datas1 = responses1.text
# print(data)
print(type(datas1))

# 操作文件的函数
# 参数1 文件名.类型   参数2 file_method文件操作方式(读r/写w) 参数3 指定文件编码 encoding=utf-8
# 百度.html
# 声明了一个对百度.html文件操作的文件对象  叫file
# 第二个参数 w代表 使用字符类型数据进行写入
with open("百度1.html","w",encoding="utf-8") as file:
    file.write(datas1)


# 第二种返回文本类型数据的方法     以后进行数据的清洗
# responses.content.decode方法 是对字节类型数据进行解码  默认的解码方式是utf-8解码方式
responses2 = requests.get(url=urls)
datas2=responses2.content.decode()
with open("百度2.html","w",encoding="utf-8")as file2:
    file2.write(datas2)

# # 第三种方式保存文件
# responses.content 响应数据以字节类型进行返回
responses3 = requests.get(url=urls)
datas3=responses3.content
# 文件操作的第三种方式  wb 代表数据以字节类型写入
# 写入数据的重点  以字节类型对文件进行写入 不需要指定编码
with open("百度3.html","wb")as file2:
    file2.write(datas3)

'''
'''______________________________________________________________________'''
URL= "https://www.baidu.com/?tn=49055317_3_hao_pg"
# 请求信息  字典
# 默认使用headers作为请求头变量  字典
# 写useragent的重要操作步骤   不要犯的错误
# 不要在useragent的前面 加空格
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
# verify=False 绕过ssl验证
responses=requests.get(url=URL,headers=headers,verify=False)
data=responses.content.decode()
print(data)
print(type(data))
with open("百度一下.html","w",encoding="utf-8") as file1:
    file1.write(data)
time.sleep(5)
os.remove("./百度一下.html")
'''
可能会出现的问题
1.遇到百度验证
    原因 请求次数频繁会涉及封 ua 或者 严重点 ip
    解决 可以参考后面的学习内容  加cookie （构建在headers里面的字段）
2.访问百度的时候 报ssl错误
    执行 绕过ssl验证的操作
    在get方法里面 加 verify=False参数 绕过ssl验证
'''
