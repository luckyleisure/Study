"""
为什么在pycharm里面 写代码 以后  计算机会帮我发送请求   并且把响应内容返回到本地呢

计算机 只能看得懂   0101010101 二进制形式的数据
python解释器会把  代码转换成 字节类型的数据 >>再转换成 计算机能看得懂的数据  010101010 解释器的功能

1bytes = 8bit    1bit == 0 1
计算机会自动的把 二进制类型的数据转换为字节类型的数据
"""

import requests
# 1.确认url (涉及网页数据包获取) 抓包
url="https://img1.baidu.com/it/u=444306396,3319778759&fm=253&app=138&size=w931&n=0&f=JPEG&fmt=auto?sec=1664038800&t=56824a4cbe52851a4883ff0716d17454"
# 2.发送请求  获取响应
response=requests.get(url)
# 图片音频视频 不需要进行清洗 直接进行保存  因为他们是二进制流的数据 bytes 类型数据
print(response.content)
# wb以字节类型写入
with open("小姐姐.png","wb")as file1:
    #已写入字节数据类型写入 小姐姐.png文件里面
    file1.write(response.content)


"""
