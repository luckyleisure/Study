"""
发现规律 每一页url的pn字段再以50进行递增
作业1 采集翻页的贴吧数据   采集5页的
        提示  pn字段在变化   循环  字符串拼接/params传参

作业2 使用面向对象改写  采集翻页贴吧数据的代码
        实例属性  静态的 headers url
        实例方法  发送请求的   保存数据的方法
通过类实例化对象  通过对象调用 类里面的方法 完成数据采集   周末的作业
2209-第一次作业-xxx(真名)
把自己写的代码复制给我
发送到 3569974821@qq.com
下周五之前交       下周一讲


作业1 采集翻页的贴吧数据   采集5页的
        提示  pn字段在变化   循环  字符串拼接/params传参
目的:采集五页的数据
流程:1.写生成五页url的代码
    2.通过循环分别向五个url发送请求
    3.保存到本地

"""

import requests
kw=input("请输入要采集的关键字:")
# # 0 1 2 3 4
for i in range(5):
    url=f"https://tieba.baidu.com/f?kw={kw}&ie=utf-8&pn={i*50}"
    print(url)
    # 请求头
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }
    # 发送请求
    response=requests.get(url=url,headers=headers)
    data=response.content.decode()
    # 注意  这里会进行数据的覆盖 !    解决方法声明不同的文件名
    with open(f"{kw}{i+1}.html","w",encoding="utf-8")as file1:
        file1.write(data)
    print(f"{kw}相关的数据采集到了第{i+1}页!")
# 第二个作业  在第一个作业的基础上 进行面向对象的改写

# 作业2 使用面向对象改写  采集翻页贴吧数据的代码
#         实例属性  静态的 headers url
#         实例方法  发送请求的   保存数据的方法

"""
目的:采集五页的数据  面向对象版本  
完成作业的步骤
面向对象 是一门编程思想 python程序员应该掌握的知识点 

需要根据要实现的功能区分静态的东西(属性) 和动态的东西(方法)  
    开发技巧 能静态的尽量静态  减少代码量
    
    静态的 headers url  (实例属性的)
    动态的 实例方法  发送请求的   保存数据的方法

在构建代码的时候差了参数  要记得写好形参进行传递 (差什么补什么)

"""
import requests

class Tieba(object):
    # 构造方法
    def __init__(self):
        # 属性!  在外面叫变量
        self.url="https://tieba.baidu.com/f?"
        # 请求头
        self.headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
        }
    #    发送请求的方法
    def crawl_data(self,params,kw,i):
        response=requests.get(url=self.url,headers=self.headers,params=params)
        data=response.content.decode()
        self.save_data(data,kw,i)
#     保存数据的方法
    def save_data(self,data,kw,i):
        # 差kw  i
        with open(f"{kw}{i+1}.html","w",encoding="utf-8")as file1:
            file1.write(data)
        print(f"{kw}相关的数据采集到了第{i + 1}页!")

    def run(self):
        # kw={kw}&ie=utf-8&pn={i*50}"
        kw = input("请输入要采集的关键字:")
        # 0 1 2 3 4
        for i in range(5):
            params={
                "kw":kw,
                "ie":"utf-8",
                "pn": i*50
            }

            self.crawl_data(params,kw,i)

# 运行 通过类实例化对象   通过对象调用类型里面的方法   run
crawl_tieba=Tieba()
crawl_tieba.run()










