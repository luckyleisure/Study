"""
jsonpath是提取json格式数据的方法
主要针对于  list 或者说是dict数据进行跨界点匹配数据的操作！

缺点   跨节点匹配有匹配不精确的情况！
解决方法  可以指定其绝对路径进行匹配!


重点语法介绍
$ 根节点   从哪个节点开始   $book
.或者[]   取子节点    节点与节点之间的过度
* 选取全部的意思     可以和[] 配合使用
..  不管在娜个位置  选择所有符合条件的条件   跨节点匹配最常用的语法符号!   最常和$配合使用

语法匹配price
"""
word = """
{"store": {
    "book": [
        {"category": "reference",
         "author": "Nigel Rees",
         "title": "Sayings of the Century",
         "price": 8.95
         },
        {"category": "fiction",
         "author": "Evelyn Waugh",
         "title": "Sword of Honour",
         "price": 12.99
         },
        {"category": "fiction",
         "author": "Herman Melville",
         "title": "Moby Dick",
         "isbn": "0-553-21311-3",
         "price": 8.99
         },
        {"category": "fiction",
         "author": "J. R. R. Tolkien",
         "title": "The Lord of the Rings",
         "isbn": "0-395-19395-8",
         "price": 22.99
         }
    ],
    "bicycle": {
        "color": "red",
        "price": 19.95
    }
}
}"""
# 使用jsonpath提取  title  author  price     认识jsonpath有点 缺点
"""
下载模块  
pip install jsonpath 
"""
# 从jsonpath模块导入jsonpath方法   使用的是方法
from jsonpath import jsonpath
import json

# 传递的参数1dict|list  参数2语法  字符串类型的
dict_data = json.loads(word)
# title  jsonpath匹配数据的机制    匹配到数据  返回包含数据的列表  没有匹配到数据 返回false jsonpath的重点
# 直接匹配到json格式数据里面 title对应的值   不管节点在哪个位置!  全部匹配
title = jsonpath(dict_data, "$..book[*].title")
print(title)
# author
author = jsonpath(dict_data, "$..book[*].author")
print(author)
# price
# 当发现匹配数据有问题时 可以指定其数据的父节点
price = jsonpath(dict_data, "$..book[*].price")
print(price)
