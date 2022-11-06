"""
json.loads    网页上采集下来的字符串str   >>>  dict|list
json.dumps    dict|list  转换成  str   用于保存

需要把本地的json文件读取出来 操作?   json>>xlsx
openpyxl   python >>excel    需要有数据
json  >>  xlsx

"""
# r 读取字符   rb读取字节
import json

with open("懂车帝2.json", "r", encoding="utf-8") as file1:
    # str_data=file1.read()
    # print(str_data)
    # # <class 'str'>   从文件读出来的数据是字符类型数据
    # print(type(str_data))
    # # 字符串转list|dict
    # dict_data=json.loads(str_data)
    # 使用jsonpath  键取值形式进行提取数据
    dict_data2 = json.load(file1)
    # <class 'list'>
    print(type(dict_data2))
    # 字符串转list|dict       loads     传递的是字符串
    #  字符串转list|dict      load      传递的是文件对象

"""
dumps
是把dict|list >>str  方法  方便进行文件写入


字典转换
"""
# with open("testdemo.json","w",encoding="utf-8")as file1:
#     item = {
#       "style": "猛士M50",
#       "peice": "66.88万"
#     }
#     # 由于写入的参数必须是字符串类型的数据 所以需要在写入之前 讲数据转换成字符串
#     str_data = json.dumps(item, ensure_ascii=False, indent=2)
#     file1.write(str_data + ",\n")
# dump  传递一个 文件对象  就能实现自动进行dict|list >>str  并且进行文件写入的操作
item = {
    "style": "猛士M50",
    "peice": "66.88万"
}
with open("testdemo.json", "w", encoding="utf-8") as file1:
    # 参数1list|dict   参数2 文件对象
    json.dump(item, file1, ensure_ascii=False, indent=2)
