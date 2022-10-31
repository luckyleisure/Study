"""
翻页数据的获取 基本都是在 请求的参数里面发生了变化

要请求不同页数的数据  就要传递不同的参数 发送请求     结合之前的知识点 url传参

需要去复制不同页数的url做对照   有没有规律  变化     看python能不能模仿规律 生成变化的参数构建到 url里面去传参
第一页 https://tieba.baidu.com/f?kw=%E6%9E%97%E4%BF%8A%E6%9D%B0&ie=utf-8&pn=0
第二页 https://tieba.baidu.com/f?kw=%E6%9E%97%E4%BF%8A%E6%9D%B0&ie=utf-8&pn=50
第三页 https://tieba.baidu.com/f?kw=%E6%9E%97%E4%BF%8A%E6%9D%B0&ie=utf-8&pn=100
第四页 https://tieba.baidu.com/f?kw=%E6%9E%97%E4%BF%8A%E6%9D%B0&ie=utf-8&pn=150

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
"""
