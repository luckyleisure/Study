"""
音乐文件后缀  mp3 m4a ts 网页上mp3/mp4

目的  通过开发者工具去定位到需要采集的资源(音频mp3)  url

流程  本节课抓包重点  抓取url
    2 发送请求
    3 获取响应
        因为(采集的数据是图片类型的数据，不需要进行清洗的所以指定步骤的时候 这一步pass)
    4 保存数据

抓取音频类型的数据包
1.抓包tips  抓包时进行数据包筛选操作以后  记得把筛选标签选回all标签
2.抓取 音频类型的数据包 不要像抓取图片类型数据包一样 通过查看数据包preview标签 查看响应内容 从而确认数据包
3.要抓音频类型的数据包 必须要使音乐加载（播放）
4.在确认数据包没有生成之前可以先把数据包清空  再做生成数据包的操作
5.可以根据音频文件的标识定位到url  xxxxxx.m4a  xxxxm4axxxx  xxxxmp3xxxx  xxxxxx.mp3 （尝试操作）
6.看到可疑的url 双击打开(针对于音视频数据包)


第二种方法
通过数据包分类 抓取url  音视频理论上来讲 是数据media分类里面的数据包 (不是100% )

第三种方法
通过数据包的Size大小进行数据包的抓取     可以联想到 一个音频数据包 的大小基本在1mB上  可以依据此条件去抓取数据包


"""
import requests

# 音频链接
mp3_url = "https://m801.music.126.net/20221007213324/e6624b9d7bf5f957b2d6cf6ad6295aa2/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/16211407351/9d4f/ed95/0b1e/2a6d8eba81a640a44f2ca3d9dbefe120.m4a"
# 请求头
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
# 发送请求 获取响应
response = requests.get(mp3_url, headers=headers)

# 保存数据   重点 不能使用字符形式保存数据  只能通过保存字节的形式保存数据
bytes_data = response.content

# 新创文件对象
# 数据包的文件类型是m4a的  保存数据的时候可以根据数据类型自定义保存的文件类型(遵循规则) m4a=音频  mp3=音频
with open("音乐.mp3", "wb") as file1:
    file1.write(bytes_data)

# pycharm 是编辑器 支持 打开图片的(机制)  但是不支持打开音视频(pycharm是编辑器不是播放器)规则
# 音视频文件 可以通过 右击文件   show in Explorer 在本地打开

# 没有show in Explorer的 是版本问题  可以通过更新pycharm实现功能
