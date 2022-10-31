"""
采集视频  mv         /mp4 ts flv ....

目的  通过开发者工具去定位到需要采集的资源(视频mp4)  url

流程  本节课抓包重点  抓取url
    2 发送请求
    3 获取响应
        因为(采集的数据是图片类型的数据，不需要进行清洗的所以指定步骤的时候 这一步pass)
    4 保存数据

第一种抓视频数据的方法
通过数据包分类 抓取url  音视频理论上来讲 是数据media分类里面的数据包 (不是100% )

第二种抓视频数据的方法
通过数据包的Size 进行抓取   抓视频类型的数据包 看到最大的数据包   尝试直接双击打开

第三种抓视频数据的方法
可以根据视频文件的标识定位到url   xxxxmp4xxxx  xxxxxx.mp4 （尝试操作）


"""
import requests

# 视频url
video_url = "https://vodkgeyttp8.vod.126.net/cloudmusic/ICAiMDAwIGAwICAgISIiJA==/mv/375130/fab51440788fca8cdfcf2726b7328947.mp4?wsSecret=6a0a2d4ac729fa30390e6d3ce0d95d41&wsTime=1665149563"
# 请求头
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
# 发送请求
response = requests.get(url=video_url, headers=headers)

# 保存数据   重点 不能使用字符形式保存数据  只能通过保存字节的形式保存数据
bytes_data = response.content
with open("可惜没如果.mp4", "wb") as file1:
    file1.write(bytes_data)
"""
采集的速度取决于(文件大小  网络速度)

"""
