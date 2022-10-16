import requests

# 确认数据的资源地址（抓包） 注：网址要全
urls = "https://img2.baidu.com/it/u=1121490367,413195985&fm=253&app=138&size=w931&n=0&f=JPEG&fmt=auto?sec=1666026000&t=f8634fc9bf0fa4a06e93660c613dabef"
# 发送请求，获取响应
responses = requests.get(urls)
# 清洗数据 注：图片音视频不需要清洗，直接保存，因为它们是二进制流的数据 bytes
# pass
# 保存数据
contents = responses.content
# print(contents)
with open("lady.png", "wb") as files:
    # 以写入字节数据类型写入 到 lady.png 文件里面
    files.write(contents)
# tips    pycharm 只支持图片文件预览  不支持 MP3 mp4 文件类型的预览
