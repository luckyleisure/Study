import requests
from fake_useragent import FakeUserAgent


class ClimbPostBar(object):
    def __init__(self):
        self.urls = "https://tieba.baidu.com/f?ie=utf-8"
        useragent = FakeUserAgent().random
        self.headers = {
            "User-Agent": useragent,
            'Cookie': 'BIDUPSID=35DE82EBA87F1A7939F446F0A2F94852; PSTM=1667105886; BAIDUID=35DE82EBA87F1A79220A519743E7C759:FG=1; BAIDUID_BFESS=35DE82EBA87F1A79220A519743E7C759:FG=1; BA_HECTOR=048ka0ak8ga1018h0581f9qs1hlvd3p1b; ZFY=8NbVHcxLJqBx5q9syiNudM74uCYz8lyBdPeTLLCK9aU:C; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BAIDU_WISE_UID=wapp_1667220065476_428; __bid_n=1842e0f459a34429db4207; FPTOKEN=30$/JGcJy/yrQiQpkk/NvBIaObaz0fdqEvaM/Bp/ecg3M/8FJgBSqpTBblK5ZM7/sFKJsTVtbqZQqI3txXXcsGyGauumkD2/KETbG2b7PMU8r4WN2K3yak61Q7KLC6PrHSzH2V9bBhV9ObE1+omre60qdiIpnh0O0oNeFc44xvDcashSk9rq733D2kMjV+2wYmQv4t56fJTTqS9n2ecNG97TyNMJjOIPzJDgC7hT6tbO9T9eYx07E30SO8p+GDJyi4zjDsRCzT8hwK2XT4Rj9Cmy6SqATY697xN4tsqef3T7r+yImUI8qqnDXAdI8ni5neUA1f7L/m7I3KgV13o726n5lJw8+I4l5+HtVvaMMKxW1ac+cR1imafw9suenQoUWMI|gJ3Wk6yh8B09LUVJNl4dZF8/JFEjOYiYgeQXd/LmAYc=|10|e81025a3162b2fc3090e14ea8773e953; BDRCVFR[FIXrT5n2Tgt]=mk3SLVN4HKm; H_PS_PSSID=26350; delPer=0; PSINO=3; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1667220063,1667229365; st_key_id=17; USER_JUMP=-1; tb_as_data=0737d6aa6e2816b411b652591c0a49d1aa2ee7df9c52e48aef6139785273891adf8cb54b6ea0498f22f5a7cd1877a6877fdfdb703255fd3d73eee54ed171c79fbceef2ccafea9a76f490627e658428f9eaa731ceef2208484565919953b14535ed73a267061de72caad85867c3e6d991; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1667229393; XFI=0187ded0-592f-11ed-91af-9f03c007965b; XFCS=AF3240D93E9181CC9920280BF2A777AAA44C9FFA012DD509B9F7607624DC3857; XFT=8xB4eZ4D94OON3T1gLY8JU4cnqZLYzoD4bATsbPjS+g=; video_bubble0=1; ab_sr=1.0.1_MDBmY2E3MWE0OWU5NzllMjM0ODAzOWExYzQ0NzNiMTY5YjI5N2RjOTA1OGIyY2FhMDBmOGQ0NmYyYmI2ZWNmZWRmMGI2YWIwYjU5MGExMjAzYTlmY2ViNTg2NTBmOWJkMWQyYzcwZWMxMDcyYWJiMjExNGYwMWRhMzVjNzZjNGU0NDYzZGM5NTZjYmFjNjM3MmE5NzM4MjU2YzdkZGU5Nw==; st_data=fcf795962e82fdf92591454fdc3b8a6d51dee68a88bb01f9e38f261d7583b694a1d64d61714b885f831d078de71035af27015ad97bfe194c9d5deec81eb30ad402ff04773e97c1a478609ad305ce427a7182cdb9693eb3562eaacee9d3d8d593; st_sign=064cb53e; RT="z=1&dm=baidu.com&si=78ce62f4-255c-4f28-ada0-d21a0edfe9eb&ss=l9wxbep2&sl=h&tt=fdj&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=165y&nu=cza9854l&cl=142m&ul=1hzw"'
        }

    def PosterBar(self, wd, i, params):
        response = requests.get(url=self.urls, headers=self.headers, params=params)
        tiebas = response.content.decode()
        with open(f"{wd}{i + 1}页.html", "w", encoding="utf-8") as file1:
            file1.write(tiebas)

    def run(self):
        wd = input("请输入要爬取的内容：")
        page = int(input("请输入要爬取的页数："))
        for i in range(page):
            params = {
                "pn": i * 50,
                "kw": wd
            }
            self.PosterBar(wd, i, params)


if __name__ == '__main__':
    climb = ClimbPostBar()
    climb.run()
