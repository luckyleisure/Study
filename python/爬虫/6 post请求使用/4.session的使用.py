"""
session是requests库里面实例化出来的对象

作用 可以存储cookie，也可以发送post请求(模拟登录获取cookie)  get请求（携带之前获取的cookie发送请求  获取数据）
不手动的通过 headers={cookie:cookie值}  形式构建cookie 从而实时的获取 cookie1发送请求  避免了cookie过期的情况


1先通过requests库的session对象向服务器发送请求(method=post)获取cookie 保存到session对象里面!
2再通过该session对象向书架发送请求保存数据(method=get) 不用加cookie
"""
import requests
# 实例化session对象  使用Session 或者session实例化对象 都是一样的 指向的内存空间都是一样的!
session1=requests.session()
# 登录的url
login_url="https://www.kkkkkkkkk.com/user/user/login.html"
# 请求头
headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
# 请求主体信息  账户密码
data={
"username": "jiuhaoyyds",
"password": "qwe123.."
}
# 通过session1对象的post请求携带账户密码发送post请求  获取cookie
session1.post(url=login_url,headers=headers,data=data)
# 再通过session1对象的get方法(不用手动构建cookie请求的) 向书架发送请求获取书架的数据
# 书架url
book_url="https://www.kkkkkkkkk.com/user/bookshelf/index.html"
response=session1.get(url=book_url,headers=headers)
# 打印书籍的信息
datas=response.content.decode()
print(datas)


























