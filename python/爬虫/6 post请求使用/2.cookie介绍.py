"""
1.目的采集某小说网站的(自己书架)的书籍数据    被人不能获取的数据
    get



"""

import requests

url="https://www.kkkkkkkkk.com/user/bookshelf/index.html"
# 请求头
headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "cookie": "lf___forward__=%2F; Hm_lvt_bd48ecec99527fc609704be7dcf3fe88=1665407363; lf_user_auth=think%3A%7B%22uid%22%3A%22602%22%2C%22username%22%3A%22jiuhaoyyds%22%7D; lf_user_auth_sign=d91a0114ce350b1e7aa9ec7b6bf017599fddd80b; Hm_lpvt_bd48ecec99527fc609704be7dcf3fe88=1665407490"
}
# 发送请求
response=requests.get(url=url,headers=headers)
datas=response.content.decode()
# 打印响应内容
print(datas)
#发送请求发现 出现了 l">免费注册< 登录 等关键字      被反扒了
""" qwe123.. """
"""
cookie  饼干   在介于服务器和客户端之间连接确认身份的令牌  


生成:第一次客户端在网页上登录 服务器就会在返回数据的过程中 夹带一个字段叫cookie 传递到浏览器!
# 用途在于第二次 浏览器去访问网页的时候 就不用登录了  

如何给py代码添加cookie访问？
需要到数据包复制!    获取方式和复制useragent的方式是一样的  requests headers标签里面的字段

注意 每一个人的cookie是不一样的  
长度不一定 字符也会不一样!      相当于是每个人银行卡密码   

不要随意的暴露cookie！   很危险  

但是能够模拟浏览器请求数据时携带cookie
   
cookie有缺点
有时效性   


解决方法  
实时获取cookie  再请求个人数据！

关键点:实时获取cookie 
流程:
1先通过requests库的session对象向服务器发送请求(method=post)获取cookie 保存到session对象里面!
2再通过该session对象向书架发送请求保存数据(method=get) 不用加cookie

session对象是一个保存cookie的对象   并且还可以支持发送post请求和get请求   

session模仿浏览器保存cookie的   







"""









