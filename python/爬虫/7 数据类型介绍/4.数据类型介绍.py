"""
网页上的文本类型数据    链接   文章。。。。

1.结构化数据
    json (结构化数据的基本类型)
    如何鉴别    打开数据包   response  和preview里面都有数据  而且 preview里面是可以展开展示的数据  就是json格式数据
    不同的数据类型有不同的清洗方法
    json   jsonpath模块进行清洗(使用模块清洗前需要进行数据转换(str>dict|list))      re 清洗字符串

2非结构化数据
    html(非结构化数据的基本类型)
    如何鉴别    打开数据包   response  和preview里面都有数据  而且 response里面有html标签 preview展示的是视图 就是html格式数据
     不同的数据类型有不同的清洗方法
    html   lxml  xpath(使用模块清洗前需要进行数据转换(str>element对象))           re 清洗字符串

"""













