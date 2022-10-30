"""
基于需要传递多个参数  进行字符串拼接 不是很好使用


可以使用 params关键字参数 进行传参
params参数   传参是get方法 特有的

post data   构建形式  字典

get params  构建形式  字典


如何通过url复制(构建)？

https://www.baidu.com/s?wd=%E9%82%93%E7%B4%AB%E6%A3%8B
wd=%E9%82%93%E7%B4%AB%E6%A3%8B&
wd  ==  键
=   ==   :
%E9%82%93%E7%B4%AB%E6%A3%8B& ==值
键值对之间使用 &分割从而构建新的  参数
https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=%E9%82%93%E7%B4%AB%E6%A3%8B&oq=%25E9%2582%2593%25E7%25B4%25AB%25E6%25A3%258B&rsv_pq=ef518fb20001e3e8&rsv_t=bdc3FKhTHEARJ%2BeBM9bSWvLPVhz6sy%2BlzJnpUsduW8XjC%2BIA8fyc%2FW762yQ&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_btype=t
"""
# 规范编写都是写的params
import requests
from fake_useragent import FakeUserAgent
wd=input("请输入要采集的关键字:")
params={
    "wd": wd,
    "ie" :"utf-8",  #不数据关键参数     （以后如果要构建多个参数可以以这种形式构建）
    "rsv_bp": 1
}
# 确认url
url="https://www.baidu.com/s?"
# 确认请求头
useragent=FakeUserAgent().random
headers={
    "user-agent":useragent,
    "Cookie": "PSTM=1647264351; BIDUPSID=CBBA598AB2CF72004A27DF77A269EBEF; BD_UPN=12314753; newlogin=1; BDUSS=RVSGdESzk3S0UwUWpOeVhYRXh6T0lIaTNOUnVHc2JSd04zU014RmJ5TEhVVlpqSVFBQUFBJCQAAAAAAQAAAAEAAAAAnplcwfnQx7PJtry9zNHQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMfELmPHxC5jVn; BDUSS_BFESS=RVSGdESzk3S0UwUWpOeVhYRXh6T0lIaTNOUnVHc2JSd04zU014RmJ5TEhVVlpqSVFBQUFBJCQAAAAAAQAAAAEAAAAAnplcwfnQx7PJtry9zNHQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMfELmPHxC5jVn; BAIDUID=9CE7556020BF8320993AF17CEC6B290F:SL=0:NR=10:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; BD_CK_SAM=1; PSINO=6; COOKIE_SESSION=2199_0_8_8_6_3_1_0_8_3_0_0_18764_0_3_0_1664538800_0_1664538797%7C9%23357565_107_1664361216%7C9; BAIDUID_BFESS=9CE7556020BF8320993AF17CEC6B290F:SL=0:NR=10:FG=1; BA_HECTOR=8k0k8g048h8g81ah84a168e21hjdrc21a; ZFY=0pcAdmj4IJ6mhP0gCpyc2z9xriwTp:B7Z4pWyRrZMW6g:C; H_PS_PSSID=36550_37359_36885_34813_37403_36804_37407_36789_37499_26350_37343_37372; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; B64_BOT=1; H_PS_645EC=03cfHZU83Ou%2B%2FHk%2BN54W9aZ5Z5H0s83leI%2F7fQE3Yy5hD%2BZi7WumPhu6Rns; baikeVisitId=5fcf770f-230e-416d-9eb7-5886fdb16437; BD_HOME=1; sug=3; sugstore=0; ORIGIN=0; bdime=0"
}
# 发送请求
# 向https://www.baidu.com/s?发送请求   同时携带了headers请求头   而且 还会 自动的将params参数里面参数（键值对）
# 自动镶嵌到 https://www.baidu.com/s?后面 发送请求
response=requests.get(url=url,headers=headers,params=params)

data=response.content.decode()

print(data)

with open(f"{wd}.html","w",encoding="utf-8")as file1:
    file1.write(data)






