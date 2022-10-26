"""
1.为什么从网页导航栏上复制下来的url里面的中文变成了（所谓的密文）？
    看到的密文  %E6%9E%97%E4%BF%8A%E6%9D%B0
    是因为进行了urlencode编码  不是加密

2.影不影响正常的发送请求 获取响应呢？
不影响发送请求获取响应

3.意义是在于什么？
在于为了让 pycharm编辑器  浏览器 更好的解析链接
以及更快的访问网页    通过按住ctrl +鼠标左键 点击链接 就能直接访问       流量

https://www.baidu.com/s?wd=%E6%9E%97%E4%BF%8A%E6%9D%B0&rsv_spt=1&rsv_iqid=0xd4ab4dda000407cb&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3=14&rsv_sug1=10&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&prefixsug=lin%2526%252339%253Bjun%2526%252339%253Bjie&rsp=5&inputT=4571&rsv_sug4=83242
url里面的 参数都是键值对   {key:value}   在url里面的表达形式是  https://www.baidu.com/s?name=林俊杰&age=18&sex=男

即使把url里面已经经过urlencode编码的字符串 改成中文  也是能够通过更改后的url去请求网页数据的！



urlencode是验证
"""
# 导入 quote,unquote方法
from urllib.parse import quote,unquote
# quote进行中文转urlencode编码的方法
name="林俊杰"
encodedata=quote(name)
print(encodedata)
# unquote进行 urlencode编码转中文的方法
mingdata=unquote(encodedata)
print(mingdata)











