"""
1.学会post

post:requests库里面的请求方法
和get的区别
    get:直接获取数据的方法    1 音乐   png  MP4                   参数是在url后面  params    (字典)
    post:需要先提交一部分数据到服务器以后   服务器才会返回数据的方法!  参数是额外的表单封装的   data  （字典）
通过抓取登录的数据包 并且发送post请求进行登录  让大家知道如何抓post数据包 以及如何使用python发送post请求



抓post请求数据包时可能会出现的问题
1提交表单 以网页刷新数据包丢失!
    解决方法1 输入错误的账户密码 抓包      抓到包以后再在py文件里面构建真实的账户密码
    解决方法2 点击 preserver log 保存日志!   谨慎使用！

"""
import requests
login_url="https://www.kkkkkkkkk.com/user/user/login.html"

# 请求头
headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
# post请求需要写 data表单
data={
"username": "jiuhaoyyds",
"password": "qwe123.."
}

# 发送post请求
response=requests.post(url=login_url,headers=headers,data=data)
print(response.content.decode())
