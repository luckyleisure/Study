# @Time   : 2022/4/26
# @Author : Wilia
"import 模块名"
# import random
# print(random.randint(1,10))

"from 模块/包 import 函数名/属性……"
# from random import randint
# from random import * 导入 random模块下的所有
# print(randint(1,10))
# print(random())


"导入多模块"
# import random
# import os
# import time

"导入自定义模块"
# import aa
# print(aa.s)

# from  aa import funa,funb
# funa()
# funb()


"""
py文件的两种功能
1.脚本：一个文件就是整个程序，用来被执行
2.模块:文件中存放着一堆功能，用来被导入使用
"""

# python为我们内置了全局变量__name__
"""
当文件被当做脚本执行时，__name__ 等于"__main__"
当文件被当做模块执行时，__name__ 等于模块名
"""

# print(123)
# print(__name__)   # __main__

# 导入aa模块
# import aa
# print(aa.__name__)  # aa


"包"
# __init__.py 初始化文件---导入包时会自动执行
# import zhifu

# from zhifu import zhifubao,weixin

from zhifu import *  # 导入所有

# __all__ 用来设置上面*所代表的内容


