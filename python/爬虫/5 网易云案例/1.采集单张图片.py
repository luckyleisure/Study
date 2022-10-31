"""
目的  通过开发者工具去定位到需要采集的资源(图片)  url

流程  本节课抓包重点  抓取url
    2 发送请求
    3 获取相应
        因为(采集的数据是图片类型的数据，不需要进行清洗的所以指定步骤的时候 这一步pass)
    4 保存数据
定位方法1 在network 全类型进行搜索   查看每个数据包    查看数据包的略缩图
1.要抓数据包 就得做生成数据包的操作       需要进行刷新，点击下一页等生成新元素的操作
2.根据要采集的类型 去不同的 响应内容标签里面查看响应内容 （图片类型的数据  可以通1过点击数据包以后 再次点击右侧的preview 标签查看 响应是不是我要的数据    response适合查看文本类型的数据   preview也支持查看json(文本)类型的数据）
定位方法2 在network  (根据要采集的数据类型进行数据包的筛选，图片为例  可以点击 筛选图标下面的 img标签进行抓包 ) png jpg
定位方法3 通过资源定位标签定位(根据不同类型的数据使用此方法  图片)  然后通过资源定位标签旁边的 Elements(网页源代码)标签
        注意点  在通过资源定位标签定位到 链接以后   不要直接在Elements复制链接  直接点击链接 在浏览器查看图片
        在导航栏顶部直接复制图片的链接
"""
#          https://p2.music.126.net/vu236KSx8gQZ4o7Qys6pRQ==/109951163414509421.jpg?param=140y140

import requests

# 图片url
url = "https://p2.music.126.net/vu236KSx8gQZ4o7Qys6pRQ==/109951163414509421.jpg?param=140y140"

# 确认请求头
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

# 发送请求 返回响应
response = requests.get(url=url, headers=headers)
# # 保存图片类型的数据  错误的写法
# data=response.content.decode()
# with open("歪果仁.png","w",encoding="utf-8")as file1:
#     file1.write(data)

# （保存数据的重点   规则） 保存图片字节类型的数据
# 图片/音视频的字节数据 不能通过decode方法进行解码
# 字符类型的字节可以通过decode方法进行解码

# （保存图片/音视频类型数据只能通过   保存字节的形式进行保存  规则）
# 这里是正确的写法
bytes_data = response.content
# with open("歪果仁.png","wb")as file1:
#     file1.write(bytes_data)
# #     pycharm 是编辑器 支持 打开图片的(机制)  但是不支持打开音视频(pycharm是编辑器不是播放器)规则


#
# ----------------------------------------------------------------------------
# 相对路径保存文件
with open("./../../歪果仁.png", "wb") as file1:
    file1.write(bytes_data)
#     pycharm 是编辑器 支持 打开图片的(机制)  但是不支持打开音视频(pycharm是编辑器不是播放器)规则
# 绝对路径保存文件
#
with open(r"D:\六星教育\2209期\2209期python\05.网易云案例\歪果仁.png", "wb") as file1:
    file1.write(bytes_data)
