"""--------------------------1.referer案例讲解--------------------------------"""

"""
网址:https://ke.qq.com/course/292490?tuin=d4c97e25
referer: https://ke.qq.com/course/292490?tuin=d4c97e25
目的:采集腾讯课堂数据案例
采集字段:评论人 评论的信息
保存到json文件

流程
确认数据类型
    json类型     jsonpath
确认数据位置
    都在同一网页
"""
import requests
from jsonpath import jsonpath
import json

url = "https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=292490&filter_rating=0&page=0&bkn=&r=0.1986"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "referer": "https://ke.qq.com/course/292490?tuin=d4c97e25"
}
response = requests.get(url=url, headers=headers)
str_data = response.content.decode()
# print(str_data)
data = json.loads(str_data)
nick_name = jsonpath(data, "$..result.items[*].nick_name")
print(len(nick_name))
print(nick_name)
comment = jsonpath(data, "$..result.items.*.first_comment")
print(len(comment))
print(comment)

with open("腾讯.json", "w", encoding="utf-8") as file1:
    datalst = []
    for i in zip(nick_name, comment):
        items = {
            "nick_name": i[0],
            "comment": i[1]
        }
        datalst.append(items)
    json.dump(datalst, file1, ensure_ascii=False, indent="\t")

"""---------------------2.翻页数据获取-----------------------------------"""
"""
https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=292490&filter_rating=0&page=0&bkn=&r=0.1986
https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=292490&filter_rating=0&page=1&bkn=&r=0.5015
https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=292490&filter_rating=0&page=2&bkn=&r=0.3214
https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=292490&filter_rating=0&page=3&bkn=&r=0.3508
"""
import requests
from jsonpath import jsonpath
import json

page = 2
datalst = []
with open("腾讯翻页.json", "w", encoding="utf-8") as file2:
    for i in range(page):
        url = f"https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=292490&filter_rating=0&page={i}"
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            "referer": "https://ke.qq.com/course/292490?tuin=d4c97e25"
        }
        response = requests.get(url=url, headers=headers)
        str_data = response.content.decode()
        # print(str_data)
        data = json.loads(str_data)
        nick_name = jsonpath(data, "$..result.items[*].nick_name")
        # print(len(nick_name))
        # print(nick_name)
        comment = jsonpath(data, "$..result.items.*.first_comment")
        # print(len(comment))
        # print(comment)
        for j in zip(nick_name, comment):
            items = {
                "nick_name": j[0],
                "comment": j[1]
            }
            datalst.append(items)
    json.dump(datalst, file2, ensure_ascii=False, indent="\t")

"""-------------------------3.项目实战采集某素材网站-------------------------------------"""
"""
1.目的 采集 https://shareae.com/after-effects-project
2.数据类型  1图片  2视频    bytes


数据类型
    bytes类型数据  直接写入文件
数据位置
    在三级目录
    涉及多级目录数据采集
    1.在一级目录的响应内容匹配到 二级目录url
    2.向二级目录的url发送请求获取响应  在二级目录的响应内容里面获取三级目录的url
    3.向三级目录二代url发送请求获取响应   再在三极目录的响应内容里面获取  视频链接  图片链接
    4 再向视频链接  图片链接 发送请求 保存到本地！

"""
import requests
from lxml import etree
import re
from jsonpath import jsonpath


class Crawler(object):
    def __init__(self):
        self.url = "https://shareae.com/after-effects-project"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
        }

    def first_url_req(self):  # 发送第一次请求清洗出二级目录的url
        first_response = requests.get(url=self.url, headers=self.headers)
        first_data = first_response.content.decode()
        # print(first_data)
        html = etree.HTML(first_data)
        second_url = html.xpath('//div[@class="block"]/h2/a/@href')
        print(second_url)
        self.second_url_req(second_url)

    def second_url_req(self, second_url):  # 发送第二次请求清洗出三级级目录的url
        for u in second_url[0:1]:
            second_response = requests.get(url=u, headers=self.headers)
            second_data = second_response.text
            # print(second_data)
            third_url = re.findall('href="(https://videohive.net/item/.*?/\d*)"', second_data)[0]
            # print(third_url)
            self.third_url_req(third_url)

    def third_url_req(self, third_url):  # 发送第三次请求清洗出资源url
        third_response = requests.get(url=third_url, headers=self.headers)
        third_data = third_response.content.decode()
        # print(third_data)
        video_url = re.findall('js-video-player" href="(.*?)"', third_data)[0]
        print(video_url)
        html = etree.HTML(third_data)
        photo_url = html.xpath('//div[@class="box--no-padding"]/div/div[1]/a/img/@src')[0]
        print(photo_url)
        self.Save_VideoAndPhoto(photo_url, video_url)

    def Save_VideoAndPhoto(self, photo_url, video_url):
        print("正在保存图片！")
        photo_response = requests.get(url=photo_url, headers=self.headers)
        photo = photo_response.content
        with open("图片.png", "wb") as file1:
            file1.write(photo)
        print("图片保存完毕！")
        print("正在保存视频！")
        video_response = requests.get(url=video_url, headers=self.headers)
        video = video_response.content
        with open("视频.mp4", "wb") as file2:
            file2.write(video)
        print("视频保存完毕！")

    def Run(self):
        self.first_url_req()


if __name__ == '__main__':
    crawler = Crawler()
    crawler.Run()
