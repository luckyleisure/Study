"""
urllib 库
requests 库
共同的作用 都可以发送http请求 （可以访问网页的数据）

为什么学习 requests 而不是学习  urllib
1.requests 封装了 urllib 里面的功能  包含的功能越多
2.使用方法 更便捷


安装
requests 是python第三方库
(-i https://pypi.tuna.tsinghua.edu.cn/simple) 这个是下载源   即使用pip到这个网站下面去下载requests库
三种下载方式
前两种下载命令公式 pip install 库名 -i https://pypi.tuna.tsinghua.edu.cn/simple
1.Terminal(pycharm控制台下载)  命令
    pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
    可能出线问题
            'pip' 不是内部或外部命令，也不是可运行的程序或批处理文件。
    产生原因  没有配置pip的环境变量    pip是给python(解释器)下载模块用的
    解决方法  通过视频  找到 python下面的Scripts文件夹 配置环境变量     重新打开窗口 下载
    配置环境变量的目的:可以在任一的cmd路径下面使用到 这个Scripts路径下面的文件.exe
2.通过cmd安装   win + r  >>>cmd >>>  pip install requests 加源
   pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
    可能出线问题
            'pip' 不是内部或外部命令，也不是可运行的程序或批处理文件。
    产生原因  没有配置pip的环境变量    pip是给python(解释器)下载模块用的
    解决方法  通过视频  找到 python下面的Scripts文件夹 配置环境变量     重新打开窗口 下载
    配置环境变量的目的:可以在任一的cmd路径下面使用到 这个Scripts路径下面的文件.exe

3.在pycharm下载  pycharm左上角 File >>>settings>>解释器>>右上角+号 搜索requests >>>install package

下载时出现了黄色提示信息   代表可以更新pip
python -m pip install --upgrade pip  通过这个 命令
python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
可以支持加源更新


可能出现问题
在控制台已经提示下载成功  也更新好了pip
但是  导入的时候报错
产生原因 自己有两个python.exe   把 requests库下载到了A_python  在pycharm里面使用的是B_python
    如何查看自己有几个python   命令 win+R  >>>cmd >>>where python
    如何解决:查看自己pycharm里面的 python是 A_python B_python

产生问题
     'where' 不是内部或外部命令，也不是可运行的程序
        where.exe
    原因是因为没有 C:\Windows\System32 环境变量
    解决方法
    将 C:\Windows\System32 路径配置环境变量

"""
# 导入requests 库
import requests










