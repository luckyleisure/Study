"""
变量必须先定义才能使用
变量的定义： 变量名 = 值
在内存中创建一个变量，包括：
# 1） 变量名；
# 2） 变量保存的数据；
# 3） 变量存储的数据类型；----定义时数据类型已确定
# 4） 变量的地址。
"""
name = '张三'
print("type: ", type(name))  # <class 'str'>
print("id: ", id(name))  # id()查看数据内存地址 ：2498259741552
num = 1.5
print("type: ", type(num))  # <class 'float'> : type()查看数据类型
print("id: ", id(num))  # id:  2483744416656
num = 200
print("type: ", type(num))  # <class 'int'>
print("id: ", id(num))  # 2483691217552 ：id() 查看内存地址

# 香蕉的价格是5元/斤
price = 5
# 买了5.5斤
weight = 5.5

# 付款，老板说只要买了香蕉就返5元券
money = price * weight  # 27.5
money = money - 5
print(money)  # 22.5

"标识符----一个名字，它的主要作用是作为变量、函数、类、模块以及其他对象的名称"
"尽量做到 **见名知其意** "
# 标识符规范的规则是:
# 		1. 只能由数字, 字母, _(下划线)组成
# 		2. 不能以数字开头
# 		3. 不能是关键字
# 		4. 区分大小写


# 查看关键字
help('keywords')

Name = '王五'
print(Name)
# 6name = 'HAHA'  # 不可以
__name = 'haha'  # 不建议
print(__name)

你好 = 1000
print(你好)

"变量的命名规则"
# 大驼峰：每个单词首字母大写，如MyName
# 小驼峰：第二个（含）以后的单词首字母大写，如myName
# 下划线：如my_name

my_name = '张三'
print(my_name)
schoolname = 'sixstar'
print(schoolname)  # sixstar
print('schoolname')  # schoolname
