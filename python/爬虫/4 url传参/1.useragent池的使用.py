"""
什么是user-agent池?
    包含了多个用户代理的容器(列表，元组，集合..)
有什么用?
    可以达到反反爬的效果1
如果使用同一个ua 去进行网页的访问  可能会出现被反扒的情况
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) Appme/105.0.0.0 Safari/537.36"

zhangsan_requests_count=100
if zhangsan_requests_count>=100:
    反扒!
如果是"全字段"的ua再次进行访问  请求次数加1
if zhangsan_requests_ua=="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Appme/106.0.0.0 Safari/537.36"
    zhangsan_requests_count+=1

如果过想反反爬 可以通过更改ua更改请求身份去再次请求!    间接性的进行了反反爬!


怎么用？  即构建useragent池
第一种方法
需要先拿一个正确的ua  然后通过理性的方法重新声明新的ua，然后放到列表
循环遍历使用 不同ua
"""
ua_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
]
for ua in ua_list:
    headers = {
        "user-agent": ua
    }
    print(headers)

"""
第二种使用随机的方法 获取ua  
1随机索引
2直接随机值    
"""
import random

ua_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
]
# 1随机索引  由于列表只有3条数据  索引0开始 2结束 就写入0 2
index = random.randint(0, 2)
print(index)
headers = {
    "user-agent": ua_list[index]
}
print(headers)
# 2直接随机值 通过random.choices随机获取ualist里面的ua   返回形式是一个包含了ua的列表
ua = random.choices(ua_list)

ua2 = random.choice(ua_list)
print(ua)
headers = {
    "user-agent": ua2
}

print(headers)

# 通过第三方模块实现生成ua的功能
# fake-useragent  默认是属于联网
# pip install fake-useragent
# 导入的时候使用下划线导入
# 导入fake_useragent模块里面的FakeUserAgent类
from fake_useragent import FakeUserAgent

# 注意FakeUserAgent是驼峰命令法
# 通过FakeUserAgent类的random方法 获取一个随机请求的ua
useragent = FakeUserAgent().random
print(useragent)

"""
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; Media Center PC 6.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C)
需要进行配置  
"""

# # 第一部运行下面的代码 查看到自己的路径
import os
import tempfile

__version__ = '0.1.11'
DB = os.path.join(
    tempfile.gettempdir(),
    'fake_useragent_{version}.json'.format(
        version=__version__,
    ),
)
print(DB)
# C:\Users\admin\AppData\Local\Temp\fake_useragent_0.1.11.json
# 第二步 切换到自己的资源管理器路径里面去
# C:\Users\admin\AppData\Local\Temp\

# 第三步 把fake_useragent_0.1.11.json放到 C:\Users\admin\AppData\Local\Temp\ 文件夹下面去
# 第四步就可以直接运行 useragent=FakeUserAgent().random

"""
适用于所有模块 导入出现以下情况  
fake-useragent 执行的时候会报没有找到方法的错误 
1可能出现的原因 是自己拿模块名作为了py文件名
    解决方法 手动更改名字 
2.模块没有下载完全  只下了一部分  
    解决方法 先卸载模块  pip uninstall fake-useragent   
#     重新下载 模块  pip install fake-useragent 加源   


"""
