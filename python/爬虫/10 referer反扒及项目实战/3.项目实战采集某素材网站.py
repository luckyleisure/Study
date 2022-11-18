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
"""

1.在一级目录的响应内容匹配到 二级目录url
2.向二级目录的url发送请求获取响应  在二级目录的响应内容里面获取三级目录的url
3.向三级目录二代url发送请求获取响应   再在三极目录的响应内容里面获取  视频链接  图片链接
4 再向视频链接  图片链接 发送请求 保存到本地！

报错  
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xab in position 4411: invalid start byte
原因  是因为响应文本里面有一些特殊字符不能通过 utf-8解码    
解决方法  使用原生的解码 即可 
使用代码 response.text     
 �Copy link�
 
 
网页上的url能直接访问到的数据(图片)  
用程序匹配url不能访问   （及时放到浏览器依然不能访问）
考虑url参数变化！！ 
网页上的url
https://videohive.img.customer.envatousercontent.com/files/404737602/Preview.png?auto=compress%2Cformat&fit=crop&crop=top&max-h=8000&max-w=590&s=f1f20818c2d0194b93e53fd35e61c947
匹配到的url
https://videohive.img.customer.envatousercontent.com/files/404737602/Preview.png?auto=compress%2Cformat&fit=crop&crop=top&max-h=8000&max-w=590&s=f1f20818c2d0194b93e53fd35e61c947
对比发现 图片的url参数  多了  多了参数 
解决方法 替换掉字符再发送请求



可能会遇到的问题
使用requests向图片发送请求会失败! 
可以重新实例化session对象发送请求 
"""
import requests
from lxml import etree
import re

class crawl():
    def __init__(self):
        # 初始请求地址
        self.url="https://shareae.com/after-effects-project"
#         请求头
        self.headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
            "cookie": "_ga=GA1.2.1292249770.1648125313; _gid=GA1.2.1191603686.1666177914; PHPSESSID=j4o6mmrhfb6g4m579g6dmsi3l7; _gat=1",
        }
        # self.session1=requests.session()
#    向一级目录发送请求的方法     获取二级目录的链接
    def first_crawl(self):
        first_response=requests.get(url=self.url,headers=self.headers)
        res_data=first_response.content.decode()
        # print(res_data)
        # str>>element
        html=etree.HTML(res_data)
        second_url_list=html.xpath('//div[@class="block"]/h2/a/@href')
        # print(second_url_list)
        # print(len(second_url_list))
        self.second_crawl(second_url_list)
#    向二级目录发送请求的方法    获取三级目录的链接
    def second_crawl(self,second_url_list):
        # 遍历包含50个链接的列表
        for second_url in second_url_list[0:1]:
            second_response=requests.get(url=second_url,headers=self.headers)
            second_res=second_response.text
            # print(second_res)
            # 语法不行   通配性太强了！
            # third_url=re.findall('href="(.*?)"',second_res)
#             这个语法可以
            third_url=re.findall('href="(https://videohive.net/item/clean-website-promo/\d*)"',second_res)[0]
            print(third_url)
            self.third_crawl(third_url)
#    向三级目录发送请求的方法    目的获取视频，图片链接
    def third_crawl(self,third_url):
        third_response=requests.get(url=third_url,headers=self.headers)
        third_res=third_response.content.decode()
        print(third_res)
        photo_url=re.findall('width="590" height="332" src="(.*?)"',third_res)[0]
        # repalce是替换字符串的方法 参数1 需要替换什么字符     参数2 需要替换成什么字符
        new_photo_url=photo_url.replace("amp;","")
        video_url=re.findall('js-video-player" href="(.*?)"',third_res)[0]
        print(new_photo_url)
        print(video_url)
#     向图片视频发送请求的方法
        self.crawl_media(new_photo_url,video_url)
    def crawl_media(self,new_photo_url,video_url):
        # 采集图片
        print("正在采集图片！")
        photo_res=requests.get(new_photo_url,headers=self.headers)
        bytes_photo_data=photo_res.content
        with open("./图片/图片1.jpg","wb")as file1:
            file1.write(bytes_photo_data)
    #      采集视频
        print("图片采集完毕!")
        print("正在采集视频!")
        video_res=requests.get(video_url,headers=self.headers)
        bytes_video_data=video_res.content
        with open("./视频/视频1.mp4","wb")as file2:
            file2.write(bytes_video_data)
        print("视频采集完毕!")
    # 调用 向一级目录发送请求的方法
    def run(self):
        self.first_crawl()
if __name__ == '__main__':
    # 通过类实例化对象
    paqu=crawl()
    paqu.run()









