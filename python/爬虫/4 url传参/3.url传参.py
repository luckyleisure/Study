"""
1.什么是url传参 ？
发送请求(点击百度一下)的过程中  需要传递给服务器的详细参数(邓紫棋)  这个步骤称之为url传参？动作

2.跟爬虫有什么关系？
如果需要根据关键字采集不同的数据   那么url不可能写死   所以需要学习url传参从而变通的采集到不同的数据
url="https://www.baidu.com/s?wd=%E6%9E%97%E4%BF%8A%E6%9D%B0&rsv_spt=1&rsv_iqid=0xd4ab4dda000407cb&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3=14&rsv_sug1=10&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&prefixsug=lin%2526%252339%253Bjun%2526%252339%253Bjie&rsp=5&inputT=4571&rsv_sug4=83242"

3.如何通过python在发送http请求的时候进行url传参?

传参的方法
传参的技巧
明确参数传递在哪个位置
    1.对不同的url进行分析
    # url里面的 参数都是键值对   {key:value}   在url里面的表达形式是  https://www.baidu.com/s?name=林俊杰&age=18&sex=男
    邓紫棋url:https://www.baidu.com/s?wd=邓紫棋
    林俊杰url:https://www.baidu.com/s?wd=林俊杰
    可以尝试性的把一些（可能不重要的url参数删除） 尝试性的发送请求  看能不能获取到数据  (重点 有些url参数不是必要的)

制作一个可以根据输入的关键字采集不同关键字相关数据的程序
流程
1抓能传入不同参数的数据包
https://www.baidu.com/s?wd=邓紫棋
2写input 让用户进行输入
3.拿网址和关键字进行拼接
4.发送请求获取响应
5.保存到本地


"""
import requests
from fake_useragent import FakeUserAgent

# 1抓能传入不同参数的数据包
url="https://www.baidu.com/s?wd="
# 2写input 让用户进行输入
wd=input("请输入要采集的关键字:")
# 3.拿网址和关键字进行拼接
new_url=url+wd
print(new_url)
# 请求头编写
# 注意FakeUserAgent是驼峰命令法
# 通过FakeUserAgent类的random方法 获取一个随机请求的ua
useragent=FakeUserAgent().random
headers={
    "user-agent":useragent,
    "Cookie": "PSTM=1647264351; BIDUPSID=CBBA598AB2CF72004A27DF77A269EBEF; BD_UPN=12314753; newlogin=1; BDUSS=RVSGdESzk3S0UwUWpOeVhYRXh6T0lIaTNOUnVHc2JSd04zU014RmJ5TEhVVlpqSVFBQUFBJCQAAAAAAQAAAAEAAAAAnplcwfnQx7PJtry9zNHQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMfELmPHxC5jVn; BDUSS_BFESS=RVSGdESzk3S0UwUWpOeVhYRXh6T0lIaTNOUnVHc2JSd04zU014RmJ5TEhVVlpqSVFBQUFBJCQAAAAAAQAAAAEAAAAAnplcwfnQx7PJtry9zNHQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMfELmPHxC5jVn; BAIDUID=9CE7556020BF8320993AF17CEC6B290F:SL=0:NR=10:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; BD_CK_SAM=1; PSINO=6; COOKIE_SESSION=2199_0_8_8_6_3_1_0_8_3_0_0_18764_0_3_0_1664538800_0_1664538797%7C9%23357565_107_1664361216%7C9; BAIDUID_BFESS=9CE7556020BF8320993AF17CEC6B290F:SL=0:NR=10:FG=1; BA_HECTOR=8k0k8g048h8g81ah84a168e21hjdrc21a; ZFY=0pcAdmj4IJ6mhP0gCpyc2z9xriwTp:B7Z4pWyRrZMW6g:C; H_PS_PSSID=36550_37359_36885_34813_37403_36804_37407_36789_37499_26350_37343_37372; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; B64_BOT=1; H_PS_645EC=03cfHZU83Ou%2B%2FHk%2BN54W9aZ5Z5H0s83leI%2F7fQE3Yy5hD%2BZi7WumPhu6Rns; baikeVisitId=5fcf770f-230e-416d-9eb7-5886fdb16437; BD_HOME=1; sug=3; sugstore=0; ORIGIN=0; bdime=0"
}
# 4.发送请求获取响应
response=requests.get(url=new_url,headers=headers)
# 响应内容的查看
data=response.content.decode()
print(data)

# 5.保存到本地
with open(f"{wd}.html","w",encoding="utf-8")as file1:
    file1.write(data)
"""
html文件保存到本地以后 使用浏览器打开  会出现一些 画面和实际网页不符的情况是正常情况  
原因  网页渲染资源(图片/css/js)都是使用的相对路径   再自己的电脑上 无法访问别人服务器下面的数据 
除非把服务器下面的网页渲染资源(图片/css/js)爬到本地 手动在html文件里面声明路径
"""
# ./fake_useragent_0.1.11.json





