"""------------------1.采集单张图片---------------------------"""
import requests

urls = "https://p1.music.126.net/QcPJfzds8ejF1FPgBaXMTw==/109951163128461676.jpg?param=140y140"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
response = requests.get(url=urls, headers=headers)
picture = response.content
with open("向日葵.png", "wb") as file:
    file.write(picture)
"""------------------2.采集单首音乐---------------------------"""
import requests

urls = "https://m701.music.126.net/20221031202712/47fcab6e14f7683808e6d3bec2c10280/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/14096627820/56d0/1998/ae51/3c117ef686804d449ef634dd19546cfa.m4a"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

response = requests.get(url=urls, headers=headers)
song = response.content
# print(song)
with open("温柔.mp3", "wb") as file1:
    file1.write(song)

"""------------------3.采集单个视频---------------------------"""
import requests

urls = "https://vodkgeyttp8.vod.126.net/cloudmusic/obj/core/10971957019/3d84bda34c4476cd58784cbbca870ea8.mp4?wsSecret=bb3dda4c43bb478f8b39b22be6a01797&wsTime=1667219538"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

response = requests.get(url=urls, headers=headers)
video = response.content
with open("如愿.mp4", "wb") as file1:
    file1.write(video)
"""------------------4.采集单页的贴吧数据---------------------------"""
import requests

URL = "https://tieba.baidu.com/f?ie=utf-8&kw=%E4%BA%94%E6%9C%88%E5%A4%A9&fr=search"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
response = requests.get(url=URL, headers=headers)
tieba = response.content.decode()
with open("tieba.html", "w", encoding="utf-8") as file:
    file.write(tieba)
"""------------------5.翻页数据的获取---------------------------"""
"""
https://tieba.baidu.com/f?kw=%E4%BA%94%E6%9C%88%E5%A4%A9&ie=utf-8&pn=0
https://tieba.baidu.com/f?kw=%E4%BA%94%E6%9C%88%E5%A4%A9&ie=utf-8&pn=50
https://tieba.baidu.com/f?kw=%E4%BA%94%E6%9C%88%E5%A4%A9&ie=utf-8&pn=100
https://tieba.baidu.com/f?kw=%E4%BA%94%E6%9C%88%E5%A4%A9&ie=utf-8&pn=150
"""
import requests

urls = "https://tieba.baidu.com/f?kw=%E4%BA%94%E6%9C%88%E5%A4%A9&ie=utf-8"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
for i in range(5):
    params = {
        "pn": i * 50
    }
    response = requests.get(url=urls, headers=headers, params=params)
    tiebas = response.content.decode()
    with open(f"五月天第{i + 1}页.html", "w", encoding="utf-8") as file1:
        file1.write(tiebas)



